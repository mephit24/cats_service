import os

PATH, _ = os.path.split(os.path.abspath(__file__))  #Get path to script

#Get credientals and save it as file
if not os.path.exists(f'{PATH}\\config.ini'):
    DB_NAME = input('Enter name of database: ')
    DB_USERNAME = input('Enter username: ')
    DB_PASS = input('Enter password: ') #temporary
    with open(f'{PATH}\\config.ini', 'w', encoding='UTF-8') as config:
        config.write(f'{DB_NAME}\n{DB_USERNAME}\n{DB_PASS}')
else:
    with open(f'{PATH}\\config.ini', 'r', encoding='UTF-8') as config:
        DB_NAME = config.readline().strip()
        DB_USERNAME = config.readline().strip()
        DB_PASS = config.readline().strip()
        

        
        
        
        

        
