import requests,json,os
from bs4 import BeautifulSoup
from pprint import pprint as pp
from scraping import scrap_top_list
from task4 import scrape_movie_details

url = scrap_top_list()[0:5]

# pp(scrape_movie_details(url))

# pp(scrap_top_list())

def scrape_movie_details_1(movies):
    # pp(movies)
    for movie in movies:
        movie_url = movie['poster_image_url']
        for url in movie_url:
            movie_url_1 = url[7:16]
        file_name = movie_url_1 + ".json"
        # pp(file_name)
        if os.path.isfile(file_name):
            with open (file_name,"r") as file:
                data = json.load(file)
            # pp(data)
        else:
            file_1 = open(file_name,"w")
            json.dump(movie,file_1)
            print("succesfully")

url = scrap_top_list()[0:50]
detail_movie = scrape_movie_details(url)
# scrape_movie_details_1(detail_movie)