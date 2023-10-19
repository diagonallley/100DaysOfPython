import requests
from bs4 import BeautifulSoup
import re
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

web_page = requests.get(URL)

soup = BeautifulSoup(web_page.text, "html.parser")
movies = soup.find_all("div", class_="listicle_listicle__item__OCDTx")

movie_list = []

# for movie in movies:
#     movie_name = movie.find(
#         "h3", class_="listicleItem_listicle-item__title__hW_Kn").getText()
#     movie_list.append(movie_name)

movie_list = [(movie.find(
    "h3", class_="listicleItem_listicle-item__title__hW_Kn").getText()) for movie in movies]
movie_list = movie_list[::-1]


# with open("100movies.txt", "a", encoding="utf-8") as file:
#     # for i in range(len(movie_list)-1, -1, -1):
#     #     file.write(movie_list[i]+"\n")

with open("100movies.txt", "a", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(movie+"\n")
