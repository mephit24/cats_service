from orm_model import *
import json
from recount_statistic import recount_statistic

#response for /cats
def get_cats_json(limit=None, offset=None, attribute=None, order=None): # TODO: need order by desc
    sort_attrs = {'name': Cats.catname,
                'color': Cats.catcolor,
                'tail': Cats.tail,
                'whiskers': Cats.whiskers,
                }
    cats = []
    for cat in Cats.select(). \
            limit(limit).     \
            offset(offset).   \
            order_by(sort_attrs.get(attribute, Cats.catname)). \
            dicts():
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
        recount_statistic()
        return "OK"
    except IntegrityError:
        db.close()
        return "existing"
    except DataError:
        db.close()
        return "incorrect"
