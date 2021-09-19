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
2. Run `black {script} .` to auto-reformat code.
3. Run `isort {script}.` to auto-sort all imports
---
### Environment Variables Setup:

User environment variables file (.env) should be created as described below:  

`Mailbox_credentials`  
HOST={imap server}
MAIL_USERNAME={mailbox login}
PASSWORD={mailbox password}
DOWNLOAD_FOLDER={download_folder_directory}
---
### Make script executable

1. Get inside project workdirectory: `cd {path_to_work_directory}`
2. Run pyinstaller command: `pyinstaller --onefile main.py`
3. Executable script is inside {dist} directory
---
### Special thanx to imbox author

Special thanks to imbox library author: https://github.com/martinrusev/imbox
This is imbox library customization project
---