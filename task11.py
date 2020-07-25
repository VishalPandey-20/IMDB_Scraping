# from scraping import scrap_top_list
# from task4 import scrape_movie_details
from pprint import pprint as pp
# scrap = scrap_top_list()[0:5]
# pp(scrape_movie_details(scrap))
import os,json

def analyse_movies_genre():
    list_1 = []
    list_2 = []
    if os.path.exists("task_4.json"):
        with open("task_4.json","r") as file:
            data = json.load(file)

        for i in data:
            genre = i["genre"]
            # pp(genre)

            for j in genre:
                list_1.append(j)
                # pp(list_1)
                if j not in list_2:
                    list_2.append(j)
        # pp(list_2)
        # pp(list_1)
        dict_1 = {}
        for k in list_2:
            count = 0
            for l in list_1:
                if k == l :
                    count+=1
                dict_1[k] = count
        pp(dict_1)


analyse_movies_genre()