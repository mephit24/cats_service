import os
import keyring
import argparse
import json

argparse_ = argparse.ArgumentParser()
argparse_.add_argument('--host')
argparse_.add_argument('--database')
argparse_.add_argument('--user')
# argparse_.add_argument('--password')
db_args_new = vars(argparse_.parse_args())

PATH, _ = os.path.split(os.path.abspath(__file__)) # TODO: use pathlib
db_args_default = {'database': 'db'}

if not os.path.exists(f'{PATH}/config.json'):
    with open(f'{PATH}/config.json', 'w', encoding='UTF-8') as config:
        config.write(db_args_default)

try:
    with open(f'{PATH}/config.json', 'r', encoding='UTF-8') as config:
        db_args_last = json.load(config)
        for val in db_args_new:
            if db_args_new[val]:
                db_args_last[val] = db_args_new[val]
except json.decoder.JSONDecodeError:
    print('Configuration file corruted.')
    db_args_last = db_args_default
finally:    
    with open(f'{PATH}/config.json', 'w', encoding='UTF-8') as config:
        config.write(json.dumps(db_args_last))

### TODO: security keeping password
#keyring.set_password('systemname', 'username', DB_PASS)
