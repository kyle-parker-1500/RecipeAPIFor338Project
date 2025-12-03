from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# setup database
def get_db():
    connector = sqlite3.connect('recipes.db')
    # returns rows as dicts
    connector.row_factory = sqlite3.Row

    return connector

# create table on startup
def init_db():
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        instructions TEXT,
        ingredients TEXT
        )
        ''')
    connector.commit()
    connector.close()

# initialize database
init_db()

# pydantic model for request validation
class Recipe(BaseModel):
    title: str
    description: str
    instructions: str
    ingredients: str

@app.get("/")
def read_root():
    return {"message": "Recipe API"}

@app.get("/recipes")
def get_recipes():
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM recipes")
    recipes = [dict(row) for row in cursor.fetchall()]
    connector.close()
    return {"recipes": recipes}

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()
    connector.close()

    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return dict(recipe)

@app.post("/recipes")
def create_recipe(recipe: Recipe):
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute(
        "INSERT INTO recipes (title, description, instructions, ingredients) VALUES (?, ?, ?, ?)",
        (recipe.title, recipe.description, recipe.instructions, recipe.ingredients)
    )
    connector.commit()
    recipe_id = cursor.lastrowid
    connector.close()

    return {"message": "Recipe created", "id": recipe_id}

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id))
    connector.commit()
    connector.close()

    return {"message": "Recipe deleted"}
