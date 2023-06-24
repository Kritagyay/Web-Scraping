import requests
from bs4 import BeautifulSoup
import lxml
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
responses=requests.get(URL)
website_html=responses.text

soup=BeautifulSoup(website_html,"html.parser")

all_movies=soup.find_all(name="h3",class_="title")
movies=[movies.get_text() for movies in all_movies]
# print(article_text)
movies=movies[::-1]
print(len(movies))


with open ("movies.txt", mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
