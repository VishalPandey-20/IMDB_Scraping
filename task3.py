from scraping import scrap_top_list
from pprint import pprint as pp

# pprint.pprint(scrap_top_list())
again_dict = {}
def group_by_decade(movies):
    for movie in movies:
        if movie['movie_year'][:-1]+'0' not in again_dict:
            again_dict[movie['movie_year'][:-1]+'0'] = []
        again_dict[movie['movie_year'][:-1]+'0'].append(movie)
    pp(again_dict)     
group_by_decade(scrap_top_list())



