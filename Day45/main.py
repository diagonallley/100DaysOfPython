from bs4 import BeautifulSoup
import lxml
import requests
import re

# with open("./website.html", encoding="utf-8") as file:
#     site = file.read()


# soup = BeautifulSoup(site, "html.parser")
# # print(soup.head.title.get_text())

# # print(soup.prettify())


# # getting all the tags:

# all_p = soup.find_all("p")
# for p in all_p:
#     print(p.get_text())
#     print(p.getText())


# for a in soup.find_all("a"):
#     print(a["href"])
#     print(a.get("href"))


# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# print(heading)
# print(section_heading.get("class"))


# a_app_link = soup.select(selector="p a")

# print(a_app_link)

# print(soup.select(".heading"))


html = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(html.text, "html.parser")
spans = soup.find_all("span", class_="titleline")
scores = soup.find_all("span", class_="score")
# print(len(spans))

articles = []
links = []
scores_list = []
for span in spans:
    a = span.find("a")
    articles.append(a.getText())
    links.append(a.get("href"))


# article_upvotes = [int(score.getText().split(" ")[0]) for score in scores]
article_upvotes = [int(score.getText().split(" ")[0])
                   for score in soup.find_all("span", class_="score")]
# for score in scores:
#     score_ = score.get_text().split(" ")[0]
#     # print(score_)
#     # regex = re.compile(r"^[0-9]+")
#     # score_int = regex.search(score.get_text())
#     # score_ = int(score_int.group())

#     scores_list.append(int(score_))


# print(articles)
# print(links)
index_highest = article_upvotes.index(max(article_upvotes))

print(
    f"This is the article with the highest upvotes: {articles[index_highest]} and the link is : {links[index_highest]}")
