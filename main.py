from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
import sqlite3

# create api link
app = FastAPI()

# setup database
def get_db():
    # find .db file inside computer files
    connector = sqlite3.connect('recipes.db')

    # returns rows as dicts
    connector.row_factory = sqlite3.Row

    return connector

# create table on startup
def init_db():
    # get database file
    connector = get_db()

    # define sql interaction object
    cursor = connector.cursor()

    # create a table for recipes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        ingredients TEXT,
        instructions TEXT
        )
        ''')
    connector.commit()
    connector.close()

# initialize database
init_db()

# pydantic model -> request validation
class Recipe(BaseModel):
    title: str
    ingredients: str
    instructions: str

# just returning api title
@app.get("/")
def read_root():
    return {"message": "Recipe API"}

# returns the data gotten from .db file
@app.get("/recipes")
def get_recipes():
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM recipes")

    # reads all rows in recipes db and puts each row into a dict
    recipes = [dict(row) for row in cursor.fetchall()]
    connector.close()

    # return list/array of recipe dicts:
    # keys:
    # id
    # title
    # ingredients
    # instructions
    return {"recipes" : recipes}

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    connector = get_db()
    cursor = connector.cursor()
    
    # find a single recipe at given id
    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()
    connector.close()

    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return dict(recipe)

# write new recipes to db
@app.post("/recipes")
def create_recipe(recipe: Recipe):
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute(
        "INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
        (recipe.title, recipe.ingredients, recipe.instructions)
    )
    connector.commit()
    recipe_id = cursor.lastrowid
    connector.close()

    return {"message": "Recipe created", "id": recipe_id}

# deletes recipe at specified id
@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    connector = get_db()
    cursor = connector.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id))
    connector.commit()
    connector.close()

    return {"message": "Recipe deleted"}
