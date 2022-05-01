import json
import re
import requests
from bs4 import BeautifulSoup

source=input("Your product id from the link, or the full link: ")
if not isinstance(source, int):
    source="".join(map(str,re.findall(r"\d", source)))

url= "https://www.ceneo.pl/"+source+"#tab=reviews"
all_opinions = []
while(url):
    #print(url)
    response=requests.get(url)
    #print(response.status_code)

    page = BeautifulSoup(response.text, "html.parser")

    opinions = page.select("div.js_product-review")

    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recommendation = opinion.select_one("span.user-post__author-recomendation").get_text().strip()
        except AttributeError:
            recommendation = None
        stars = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text().strip()
        useful = opinion.select_one("button.vote-yes > span").get_text().strip()
        useless = opinion.select_one("button.vote-no > span").get_text().strip()
        published = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            purchased = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchased = None
        pros = opinion.select( "div[class$=positives] ~ div.review-feature__item")
        pros = [ item.get_text().strip() for item in pros]
        cons = opinion.select( "div[class$=negatives] ~ div.review-feature__item")
        cons = [ item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_id": opinion_id,
            "author":author,
            "recommendation":recommendation,
            "stars":stars,
            "content":content,
            "useful":useful,
            "useless":useless,
            "published":published,
            "purchased":purchased,
            "pros":pros,
            "cons":cons
        }

    #print(content, useful, useless, sep="\n")
    #print(type(content))
    #print(pros, cons, sep="\n")
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None
file_attributes="opinions/"+source+".json"
with open(file_attributes, "w", encoding="UTF-8") as  jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
