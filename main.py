from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
news_website = response.text
soup = BeautifulSoup(news_website, "html.parser")

list_of_links = []
list_of_articles = []
list_of_score = []

article = soup.find_all(class_="titleline")

for heading_or_link_and_score in article:
    Titles = heading_or_link_and_score.find(name="a").getText()
    links = heading_or_link_and_score.find(name="a").get("href")
    list_of_articles.append(Titles)
    list_of_links.append(links)

score = soup.find_all(class_="score")
for scores in score:
    scoring = scores.getText()
    list_of_score.append(scoring)

make_score_int = [int(score.split()[0]) for score in list_of_score]

# print(list_of_articles)
# print(list_of_links)
# print(make_score_int)

max_score = max(make_score_int)
max_score_index = make_score_int.index(max_score)

top_news = list_of_articles[max_score_index]
top_news_link = list_of_links[max_score_index]

print(top_news)
print(top_news_link)
