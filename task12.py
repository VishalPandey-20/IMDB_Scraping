import requests , os , json
from pprint import pprint as pp
from bs4 import BeautifulSoup


main_list = []
def scrape_movie_cast():
    if os.path.exists("movie_list.json"):
        with open("movie_list.json","r") as file:
            data = json.load(file)
        # pp(data)
        for i in data[0:5]:
            url = i['url_link']
            # pp(url)
            detail = requests.get(url)
            soup = BeautifulSoup(detail.text,"html.parser")
            movie_cast = soup.find('table' , class_ = "cast_list")
            trs = movie_cast.find_all('td' , class_ = "")
            # pp(trs)
            list_1 = []
            Dict = {}
            for tr in trs:
                # dict = {}

                name = tr.text.strip()
                # pp(name)
                imdb_id = tr.find('a')['href'][6:15]
                # pp(imdb_id)
                Dict={'name':name,"imdb_id":imdb_id}
                list_1.append(Dict)
    #         # pp(list_1)

            main_list.append(list_1)


        return main_list
                
    # pp(main_list)




# scrape_movie_cast()
# pp(scrape_movie_cast())