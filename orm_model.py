from peewee import *
from init import DB_NAME, DB_USERNAME, DB_PASS

db = PostgresqlDatabase(DB_NAME, user=DB_USERNAME, password=DB_PASS)

#Test connection
try:
    db.connect()
except OperationalError:
    import os
    from init import PATH
    os.remove(f'{PATH}\\config.ini')
    print('Removed configuration, restart application!')
    
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
        
class Cats_stat(BaseModel):
    tail_length_mean = DecimalField(column_name='tail_length_mean')
    tail_length_median = DecimalField(column_name='tail_length_median')
    tail_length_mode = IntegerField(column_name='tail_length_mode')
    whiskers_length_mean = DecimalField(column_name='whiskers_length_mean')
    whiskers_length_median = DecimalField(column_name='whiskers_length_median')
    whiskers_length_mode = IntegerField(column_name='whiskers_length_mode')
    class Meta:
        table_name = 'cats_stat'
        primary_key = False
      
