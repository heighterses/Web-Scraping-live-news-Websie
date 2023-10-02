from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
news_website = response.text
soup = BeautifulSoup(news_website, "html.parser")


scores = soup.find_all(class_ = "score")

for score_list in scores:
    score_listing =score_list.text
    print(score_listing)


titles = soup.find_all(class_="titleline")
for title_list in titles:
    print(title_list.text)

















'''
with open("home.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

lists = soup.find_all(name="li")
for list in lists:
    print(list)
'''
