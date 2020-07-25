# from scraping import scrap_top_list
# from task4 import scrape_movie_details
# from task12 import scrape_movie_cast
# from task13 import get_movie_list_details
from pprint import pprint as pp
import json,os
# scrap = scrap_top_list()[0:5]
# task_4 = scrape_movie_details(scrap)
# task_12 = scrape_movie_cast(task_4)
# pp(get_movie_list_details(task_12))
# pp(scrape_movie_cast())


def analyse_actors(): 
    dict ={}
    list_1 = []
    if os.path.exists("task_13.json"):
        with open("task_13.json","r") as file:
            data = json.load(file)
        # pp(data)
        for i in data:
            # pp(i)
            cast = i['Cast']
            list_1+=cast
        # pp(list_1)
        for j in list_1:
            # pp(j)
            cast_id = j['imdb_id']
            # pp(cast_id)
            if cast_id not in dict:
                dict[cast_id] = {}
                dict[cast_id]["name"] = j["name"]
                dict[cast_id]["number_of_movie"] = 1
            else:
                dict[cast_id]["number_of_movie"] += 1
        pp(dict)

analyse_actors()
