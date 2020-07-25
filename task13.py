from task4 import scrape_movie_details
from scraping import scrap_top_list
from task12 import scrape_movie_cast

import json
from pprint import pprint as pp
# scrap = scrap_top_list()[0:5]

# pp(scrape_movie_details(scrap))
# pp(scrape_movie_cast())

# pp(scrap_top_list())
# print(scrap_top_list())





def get_movie_list_details(movies):
    # pp(movies)
    main_list = []
    for movie in movies:
        # pp(movie)
        for cast in task_12:
            # pp(cast)
            movie["Cast"]=cast
        # pp(movie)
        main_list.append(movie)
        with open ("task_13.json","w") as file:
            json.dump(main_list,file)
            print("succesful")
    # return main_list

scrap = scrap_top_list()[0:5]
task_4 = scrape_movie_details(scrap)
task_12 = scrape_movie_cast()
pp(get_movie_list_details(task_4))
# get_movie_list_details(task_4)
# get_movie_list_details(task_12)



