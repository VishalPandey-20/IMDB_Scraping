from scraping import scrap_top_list
import pprint

from pprint import pprint as pp
# pp(scrap_top_list())
def group_by_year(movies):
    # new_dict = {}
    new_dict = {}
    for movie in movies:
        new_list = []
        for i in movies:
            if movie['movie_year'] == i['movie_year']:
                new_list.append(i)
        new_dict[movie['movie_year']]=new_list


    pprint.pprint(new_dict)

        # print(i['o_movie_year'])
   

group_by_year(scrap_top_list())


# years = []
# for movie in movies:
#     if movie['year'] not in years:
#         years.append(movie['year'])

