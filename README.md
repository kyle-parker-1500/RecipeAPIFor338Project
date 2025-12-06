Steps to making this work (for my 338 Final Project team):
1. Clone the repo
   - You can use `git clone https://github.com/kyle-parker-1500/RecipeAPIFor338Project.git` in a terminal to clone the project (it should, hopefully, work)
2. Once it's successfully cloned, enter the directory in your terminal/command prompt
3. `cd .venv/Scripts`
4. Type `activate` then cd back to the main directory using `cd ..`
   - A little thing should pop up on the left of your current line in the terminal that looks like `(venv)` (or something similar
   - This means that you're in the virtual machine and can use libraries installed on the VM
5. Now type: `uvicorn main:app --reload` and hold *ctrl+click* to open up the localhost url
6. Clean the app -> assemble it, then wipe the current data from your emulator (this api currently only works with the emulator -> let me know if you are using a physical device)
   - Make sure you keep the API open and available on your local machine (if you close it, the app won't be able to access the data from it)
7. When you rerun the project the api database should load (it may take a little bit so give it some time)
   - If it's not working at all let me know
