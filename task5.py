from scraping import scrap_top_list
import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup


def get_movie_list_details (movie) :
    list_of_item = []
    for i in movie:
        dict_of_item = {}
        new_url = i['url_link']
        detail = requests.get(new_url)
        soup = BeautifulSoup(detail.text, 'html.parser')
        movie_rating = soup.find ('span' , itemprop = 'ratingValue').text


        name = soup.find('div' , class_ = 'title_wrapper')
        movie_year = name.find('span' , id = 'titleYear').text

        movie = name.find('h1').text
        movie_name=""
        for i in movie:
            if i=="(":
                break
            else:
                movie_name+=i
        
        dict_of_item ['url'] = new_url
        dict_of_item['movie_rating'] = movie_rating
        dict_of_item['movie_name'] = movie_name
        dict_of_item['movie_year'] = movie_year
        list_of_item.append(dict_of_item)
    return list_of_item
    # pp(list_of_item)

new_link = scrap_top_list()[0:10]
pp(get_movie_list_details(new_link))
