from peewee import *
import keyring
from init import db_args_last

db = PostgresqlDatabase(**db_args_last, password=keyring.get_password('cats_service', 'user'))

# Test connection
def test_db_connection():
    try:
        db.connect()
        return True
    except OperationalError:
        print("Database not available. Check credientals in config.json or start application with arguments (--help)")
        

# Model
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
