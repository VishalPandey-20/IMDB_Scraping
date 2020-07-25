import os,json
from pprint import pprint as pp
from task12 import scrape_movie_cast
# pp(scrape_movie_cast())


def analyse_co_actors(details):
    # pp(details)
    dict = {}
    for i in details:
        # pp(i)
        for j in i:
            pp(j)
            cast_id = j["imdb_id"]
            dict[cast_id] = j["name"]
    pp(dict)


task_12 = scrape_movie_cast()
analyse_co_actors(task_12)