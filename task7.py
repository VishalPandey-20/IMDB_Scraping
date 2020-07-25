from scraping import scrap_top_list
from task4 import scrape_movie_details
from pprint import pprint as pp

# pp(scrap_top_list())
# scrap_list = scrap_top_list()[0:5]
# pp(scrape_movie_details(scrap_list))

def analyse_movies_directors(movies):
    # pp(movies)
    list_1 = []
    list_2 = []
    for director in movies:
        # pp(director)
        director_1 = director['directer_name']
        # pp(director_1)
        dict = {}
        for i in director_1:
            # pp(i)
            list_1.append(i)
    # pp(list_1)
    for j in list_1:
        if j not in list_2:
            list_2.append(j)
    for k in list_2:
        count = 0
        for l in list_1:
            if k == l:
                count+=1
        dict[k]=count
    pp(dict)



scrap_list = scrap_top_list()[0:10]
analyse_movies = scrape_movie_details(scrap_list)
analyse_movies_directors(analyse_movies)
