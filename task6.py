from task4 import scrape_movie_details
from scraping import scrap_top_list
from pprint import pprint as pp



# scrap_list = scrap_top_list()[0:10]
# pp(scrape_movie_details(scrap_list))

def analyse_movies_language(movies):
    list_1 = []
    list_2 = []
    dict = {}
    for movie in movies:
        movie_langauge = movie['langauge']
        for lang_1 in movie_langauge:
            list_1.append(lang_1)
    # print(list_1)

    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    for j in list_2:
        count = 0
        for k in list_1:
            if j == k:
                count+=1
        dict[j] = count
    print(dict)






scrap_list = scrap_top_list()[0:30]
# pp(scrape_movie_details(scrap_list))
vishal = scrape_movie_details(scrap_list)


analyse_movies_language(vishal)


# print(scrape_movie_details(scrap_list))

