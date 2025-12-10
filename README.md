Steps to making this work (for my 338 Final Project team):
1. Clone the repo
   - You can use `git clone https://github.com/kyle-parker-1500/RecipeAPIFor338Project.git` in a terminal to clone the project (it should, hopefully, work)
2. Once it's successfully cloned, enter the directory in your terminal/command prompt
3. Make sure you have python installed with `python -V` or `python3 -V`, then do `py -m venv .venv` (for python3) or `python -m venv .venv` (for other versions)
   - Once it's successfully installed navigate to its directory using `cd .venv/Scripts`
4. Type `activate` to activate the virtual environment then cd back to the main directory using `cd ..` until you're there (you can use `ls` to list the files in your current directory if you're using a terminal or `dir` if using cmd on Windows)
   - A little thing should pop up on the left of your current line in the terminal that looks like `(venv)` (or something similar
   - This means that you're in the virtual environment and can use libraries installed on the virtual environment
   - Now type in `pip install fastapi uvicorn` and wait for it to install
5. Now type: `uvicorn main:app --reload` and hold *ctrl+click* to open up the localhost url
6. In Android Studio: Run your app, then either swipe up and click on the little android at the top of the hovering app->click on app info->then click *uninstall* or long click the app where it shows up in the home screen->click on app info->click on uninstall
    - Then clean the app -> assemble it and wipe the current data from your emulator (this api currently only works with the emulator -> let me know if you are using a physical device)
   - Make sure you keep the API open and available on your local machine (if you close it, the app won't be able to access the data from it)
7. When you rerun the project the api database should load (it may take a little bit so give it some time)
   - If it's not working at all let me know
If it's the Dr. trying to make this work (don't want to mention you by name in case you get mad at me) -> If you can't get a hold of me because I don't check my email just ask the TA :)
