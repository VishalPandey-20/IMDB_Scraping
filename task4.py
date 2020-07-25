# import requests , json
# from bs4 import BeautifulSoup
# from pprint import pprint as pp
# from scraping import scrap_top_list
# # for i in vishal:
# #     print(i)


# # vishal = scrap_top_list()

# # pp(scrap_top_list())
# mainList=[]
# def scrape_movie_details(movies):
#     for movie in movies:
#         dict = {}
#         link = movie['url_link']  
#         # pp(link)

#         data = requests.get(link)

#         soup = BeautifulSoup(data.text , 'html.parser')


# # # poster url of each movie

#         poster_url = soup.find('div' , class_ = 'poster').a['href']
#         dict['poster_image_url'] = []
#         dict['poster_image_url'].append(poster_url)

# # # directer name of each movie

#         directer = soup.find('div' , class_ = 'credit_summary_item')
#         directer_name = directer.find('a').text
#         dict['directer_name'] = []
#         dict['directer_name'].append(directer_name)

# #  country name  of each movie

#         detail = soup.find('div' , attrs={"class":"article","id":"titleDetails"})
#         # pp(detail)
#         country = detail.find_all('div' , class_ = 'txt-block')
#         for i in country:
#                 h4 = i.find('h4').text
#                 # print(h4)
#                 if h4 == "Country:":
#                         country7 = i.find_all('a')
#                         # print(country7)
#                         for j in country7:
#                                 country8 = j.text
#                         # print(country8)
#                         break
#         dict['country_name'] = []
#         dict['country_name'].append(country8)

# # movie name of each movie

#         movie = soup.find('div' , class_ = 'title_wrapper').text
#         movie_name = ''
#         for i in movie:
#             if i in '(':
#                 break
#             else:
#                 movie_name+=i

#         dict['movie_name'] = []
#         dict['movie_name'].append(movie_name)
    
# # #  langauge of each movie
#         langauge = soup.find('div' , attrs={"class":"article","id":"titleDetails"})
#         langauge_1 = langauge.find_all('div' , class_ = "txt-block")
#         # print(langauge_1)
#         for i in langauge_1:
#                 # print(i.text)
#                 h4 = i.find_all("h4",class_ = "inline")
#                 for j in h4:
#                         langauge_2 = j.text
#                         # print(langauge_2)
#                         if "Language" in langauge_2:
#                                 langauge_3 = i.find('a').text
#                                 # print(langauge_3)
#                         break
#         dict['langauge'] = []
#         dict['langauge'].append(langauge_3)
        
# # #  biodata of each movie

#         bio = soup.find('div' , class_ = 'summary_text').text.strip() 

# # #  genre of each movie

#         emp_list = []
#         tem_genre = soup.find('div' , class_ = 'subtext')
#         genre = tem_genre.find_all('a')
#         for i in genre:
#             emp_list.append(i.text)
#         last = emp_list[-1]
#         emp_list.remove(last)
#         dict['genre'] = emp_list

# # #  runtime of each movie

#         runtime = tem_genre.find('time').text.strip()
#         dict['runtime'] = []
#         dict['runtime'].append(runtime)
#         # print(runtime)
#         mainList.append(dict)
#         with open("task_4.json","w") as file:
#                 data = json.dump(mainList,file)
#                 # print("succesfully")

#     return mainList


# # scrap_list = scrap_top_list()[0:20]
# # pp(scrape_movie_details(scrap_list))
# # scrape_movie_details(scrap_list)


from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint as pp
import json,os

url = ('https://www.flipkart.com/search?q=Oppo%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
driver = webdriver.Chrome("\\Users\\Pandit\\Desktop\\chromedriver_win32\\webdriver")
driver.get(url)

all_opp = driver.find_elements_by_tag_name("flex-grow:1;overflow:auto")
pp(all_opp)
# res = driver.execute_script("return document.documentElement.outerHTML")
# soup = BeautifulSoup(res,"html.parser")
# all_main_div = soup.find_all(class_="bhgxx2 col-12-12")
# # print(all_main_div)
# main_list=[]
# for i in all_main_div:
#     dict_1 = {}
#     # pp(i)
#     mob = i.find_all("div" , class_ = "_3wU53n")
#     price = i.find_all("div" , class_ = "_1vC4OE _2rQ-NK")
#     for c in price:
#         # print(c.text)
#         dict_1['price'] = c.text
#     # pp(mob)
#     for j in mob:
#         # pp(j.text)
#         mobile = ""
#         for k in j.text:
#             if "(" in k:
#                 break
#             else:
#                 mobile+=k
#         mobile_name = mobile.strip()
#         # pp(mobile_name)
#         dict_1['mobile_name'] = mobile_name
#     details = i.find_all("ul" , class_ = "vFw0gD")
#     for a in details:
#         # pp(a.text)
#         det = a.text
#         # print(len(det))
#         ram = det[0:8]
#         rom = det[11:21]
#         dict_1["ram"] = ram
#         dict_1['rom'] = rom
#         q = a.find_all("li" , class_ = 'tVe95H')
#         dis = q[1].text
#         pro = q[4].text
#         dict_1['display'] = dis
#         dict_1['processor'] = pro
#         pp(dict_1)
# # driver.close()
