from orm_model import *

#Form requests and get data from DB
cats = Cats.select(Cats.catcolor).tuples().execute() #List of cats
colors = Colors.select().tuples().execute() #List of existing colors

counted = Cats.select(Cats.catcolor, fn.Count(Cats.catcolor)).group_by(Cats.catcolor).dicts().execute() #Execute request
for i in counted:
    statcolor = Cats_info(color = i['catcolor'], count = i['count'])
    statcolor.save()

print('Ready')