from peewee import *
from init import DB_NAME, DB_USERNAME, DB_PASS

db = PostgresqlDatabase(DB_NAME, user=DB_USERNAME, password=DB_PASS)

#Test connection
try:
    db.connect()
except OperationalError:
    import os
    from init import PATH
    print('Removed configuration, restart application!')
    os.remove(f'{PATH}\\config.ini')
    
#Model
class BaseModel(Model):
    class Meta:
        database = db
        
class Cats(BaseModel):
    catname = AutoField(column_name = 'name')
    catcolor = TextField(column_name = 'color')
    tail = IntegerField(column_name = 'tail_length')
    whiskers = IntegerField(column_name = 'whiskers_length')
    class Meta:
        table_name = 'cats' 
        
class Colors(BaseModel):
    color = AutoField(column_name  = 'enumlabel')
    class Meta:
        table_name = 'pg_enum'
        
class Cats_info(BaseModel):
    color = AutoField(column_name = 'color')
    count = IntegerField(column_name= 'count')
    class Meta:
        table_name = 'cat_colors_info'
        
