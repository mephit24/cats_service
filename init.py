import os
import keyring
import getpass

PATH, _ = os.path.split(os.path.abspath(__file__))  # Get path to script

    # Get DB name and username TODO: use configparser
if not os.path.exists(f'{PATH}/config.ini'): # TODO: use pathlib
    DB_HOST = input('Enter host: ')
    DB_NAME = input('Enter name of database: ')
    DB_USERNAME = input('Enter username: ')
    # Get password and save it to store
    DB_PASS = getpass.getpass(prompt = 'Enter password: ')
    keyring.set_password('systemname', 'username', DB_PASS)
    # Save DB name and username to file
    with open(f'{PATH}/config.ini', 'w', encoding='UTF-8') as config:
        config.write(f'DB_HOST={DB_HOST}\nDB_NAME={DB_NAME}\nDB_USERNAME={DB_USERNAME}')
else:
    with open(f'{PATH}/config.ini', 'r', encoding='UTF-8') as config:
        DB_HOST = config.readline().rstrip().lstrip('DB_HOST=')
        DB_NAME = config.readline().rstrip().lstrip('DB_NAME=')
        DB_USERNAME = config.readline().rstrip().lstrip('DB_USERNAME=')
        DB_PASS = config.readline().rstrip().lstrip('DB_PASS=') # keyring.get_password('systemname', 'username')
