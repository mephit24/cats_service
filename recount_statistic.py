from orm_model import *
import statistics

def recount_statistic():

    #Count color (SELECT colors, COUNT(*) FROM cats GROUP BY colors)
    counted = Cats.select(Cats.catcolor, fn.Count(Cats.catcolor)).group_by(Cats.catcolor).dicts().execute()
    #write to DB
    for i in counted:
        statcolor = Cats_info(color = i['catcolor'], count = i['count'])
        statcolor.save()

    #To form statistic

    #Get tails
    tails_obj = Cats.select(Cats.tail).tuples().execute()
    tails_lst = [value[0] for value in tails_obj]
    #Get whiskers
    whiskers_obj = Cats.select(Cats.whiskers).tuples().execute()
    whiskers_lst = [value[0] for value in whiskers_obj]

    #Calculate mean
    tails_mean = round(statistics.mean(tails_lst), 2)
    whiskers_mean = round(statistics.mean(whiskers_lst), 2)
    #Calculate median
    tails_median = round(statistics.median(tails_lst), 2)
    whiskers_median = round(statistics.median(whiskers_lst), 2)
    #Calculate mode
    tails_mode = statistics.multimode(tails_lst)
    tails_mode = str(tails_mode).replace('[', '{').replace(']', '}') #type conversion
    whiskers_mode = statistics.multimode(whiskers_lst)
    whiskers_mode = str(whiskers_mode).replace('[', '{').replace(']', '}') #type conversion

    #Write to DB
    Cats_stat.delete().execute() #clear table
    Cats_stat(tail_length_mean = tails_mean,
            tail_length_median = tails_median,
            tail_length_mode = tails_mode,
            whiskers_length_mean = whiskers_mean,
            whiskers_length_median = whiskers_median,
            whiskers_length_mode = whiskers_mode).save()

    db.close()
    return "OK"
