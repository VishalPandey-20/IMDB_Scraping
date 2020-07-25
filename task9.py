from scraping import scrap_top_list
from bs4 import BeautifulSoup
from pprint import pprint
import requests,os,json,time,random
# pp(scrap_top_list())


def get_movie_list_details_1(movies):
    # pp(movies)
    for movie in movies:
        # pp(movie['url_link'])
        movie_url = movie['url_link']
        movie_id = ''
        for i in movie_url[27:36]:
            # pp(i)
            movie_id+=i
        file_name_1 = movie_id + "detail" + ".json"
        # pp(file_name_1)
        detail = requests.get(movie_url)
        movie_detail = detail.text
        # pp(movie_detail)
        if os.path.exists(file_name_1):           
            with open (file_name_1,"r") as file:
                data_1 = json.load(file)
            # pprint(data_1)

        else:
            with open(file_name_1,"w") as file_1:
                json.dump(movie_detail,file_1)
                print("succesfully")
                random_time = random.randint(3,6)
                time.sleep(random_time)


            




scraping = scrap_top_list()[0:60]
# print(scraping)
get_movie_list_details_1(scraping)
# rondam_time = random.randint(3,5)
# print(rondam_time)
