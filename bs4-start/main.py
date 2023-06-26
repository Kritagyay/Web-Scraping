# from bs4 import BeautifulSoup
# import lxml
#
# with open("website.html",encoding="utf-8") as file:
#     content=file.read()
#
# soup = BeautifulSoup(content,"lxml")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.p)
# # print(soup.prettify())
# # print(soup)
# # print(soup.get_text())
# # print(soup.get())
#
# # print(soup.find_all("p"))
# # print(soup.find("p"))


from bs4 import BeautifulSoup
import lxml
import requests

response=requests.get("https://news.ycombinator.com/")
web_page=response.text
# print(web_page)
soup=BeautifulSoup(web_page,"html.parser")
article_tag=soup.find_all(name="span",class_="titleline")
# article_text=[]
# article_link=[]
# for articles in article_tag:
#     text=articles.get_text()
#     article_text.append(text)
#     link=articles.find("a")["href"]
#     article_link.append(link)
# article_upvote=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# # print(article_text)
# # print(article_link)
# # print(article_upvote)
# index=(article_upvote.index(max(article_upvote)))
# print(article_link[index],article_text[index])

a_tag=soup.find(name="a",class_="title")
print(a_tag)

