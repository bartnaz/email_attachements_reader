# Email Attachements Reader Project
---
### System Setup:

1. Install requirements from requirements.txt file `pip install -r requirements.txt`
---
### Project Setup:

1. Clone project directory: `git clone`
2. Create environment variables file in main directory typing command: `touch .env`
3. Populate .env according to the *Environment Variables Setup* section.
4. Run from script `python main.py`
---
### Dev Tools:

1. Run `pytest {test_directory}` to start tests.

2. Run `black {script}` to auto-reformat code.
3. Run `isort {script}` to auto-sort all imports.
---
### Environment Variables Setup:

User environment variables file (.env) should be created as described below:  


HOST=IMAP SERVER DATA

MAIL_USERNAME=MAILBOX LOGIN

PASSWORD=MAILBOX PASSWORD

DOWNLOAD_FOLDER=DOWNLOAD PATH FOLDER
---
### Make script executable

1. Get inside project workdirectory: `cd {path_to_work_directory}`
2. Run pyinstaller command: `pyinstaller --onefile main.py`
3. Executable script is inside {dist} directory
---
### Special thanx to imbox author

1. Special thanks to imbox library author: https://github.com/martinrusev/imbox
---
### Docs/ followups

__(technical)__ Project should contain Tkinter GUI.

__(technical)__ Currently datetime filter is not implemented yet.

__(technical)__ Script currently run on Gmail mailbox, more integrations should be tested/ implemented.

__(technical)__ Complex error handler should be implemented.

---