from orm_model import *
import json

#response for /cats
def get_cats_json(limit=None, offset=None):
    cats = []
    for cat in Cats.select().limit(limit).offset(offset).dicts():
        cats.append(cat)
    return cats

#create new cat on /cat
def create_cat(json_of_cat):
    json_of_cat = json.loads(json_of_cat)
    try:
        Cats.insert(catname = json_of_cat["name"],
            catcolor = json_of_cat["color"],
            tail = json_of_cat["tail_length"],
            whiskers = json_of_cat["whiskers_length"],
            ).execute()
        db.close()
        return "OK"
    except IntegrityError:
        db.close()
        return "existing"
    except DataError:
        db.close()
        return "incorrect"
    