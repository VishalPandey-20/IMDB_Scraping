import requests
import pprint,json,os
from bs4 import BeautifulSoup
from pprint import pprint as pp

def scrap_top_list():
    if os.path.exists('movie_list.json'):
        with open('movie_list.json','r') as file:
            new_file= json.load(file)
            return new_file
    else:
        url = requests.get("https://www.imdb.com/india/top-rated-indian-movies")
        # print(url.text)
        soup = BeautifulSoup(url.text,"html.parser")
        # print(soup)


        # main_div = soup.find('div' , class_ = "lister")
        main_div = soup.find('div' , class_ = "lister")
        t_body = main_div.find( 'tbody' , class_ = "lister-list")
        trs = t_body.find_all('tr')
        movie_list=[]
        rank=1
        for tr in trs:
            movie_Dict={}
            
            position = tr.find('td' , class_ = 'titleColumn')        
            movie_name=position.find('a').text

            movie_Dict['name']=movie_name  
            movie_Dict['position']=rank
            rank+=1      
            movie_year1=position.find('span',class_="secondaryInfo").text
            movie_year=movie_year1[1:5]
            movie_Dict['movie_year']=movie_year
            movie_rating = tr.find('td' , class_='ratingColumn imdbRating')
            rating=movie_rating.find('strong').text
            
            movie_Dict['rating']=rating
            url=tr.find('td' , class_ = 'titleColumn').a['href']
            url_link = "https://WWW.imdb.com"+url
            movie_Dict['url_link']=url_link
            # return movie_link
            movie_list.append(movie_Dict)
        # pprint.pprint(movie_list)
            # return(movie_list)
            with open('movie_list.json','w+')as file:
                json.dump(movie_list,file)
        return movie_list
pprint.pprint(scrap_top_list())
# scrap_top_list()