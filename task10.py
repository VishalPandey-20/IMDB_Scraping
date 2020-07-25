from scraping import scrap_top_list
# from bs4 import 
from pprint import pprint as pp
from task4 import scrape_movie_details

# scrap = scrap_top_list()[0:1]
# pp(scrape_movie_details(scrap))


def analyse_language_and_directors(movies):
    # pp(movies)
    dir_list = []
    for movie in movies:
        movie_dir = movie['directer_name']
        for j in movie_dir:
            if j not in dir_list:

                dir_list.append(j)
    # pp(dir_list)
    dir_dict = {}
    for k in dir_list:
        emp_list = []
        emp_list_1 = []
        for movie_1 in movies:
            movie_dir_1 = movie_1['directer_name']
            for l in movie_dir_1:
                if l == k:
                    movie_lan = movie_1['langauge']
                    for lan in movie_lan:
                        emp_list.append(lan)
        # pp(emp_list)
                        if lan not in emp_list_1:
                            emp_list_1.append(lan)
                            # pp(emp_list_1)
        lan_dict = {}
        for p in emp_list_1:
            count = 0
            for q in emp_list:
                if q == p:
                    count+=1
                lan_dict[p] = count
        dir_dict[k] = lan_dict
    pp(dir_dict)


scrap = scrap_top_list()[0:30]
task_4 = scrape_movie_details(scrap)
analyse_language_and_directors(task_4)