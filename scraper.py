import json
import re
import requests
from bs4 import BeautifulSoup

def get_item(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [ item.get_text().strip() for item in ancestor.select( selector)]

        if attribute:
            return ancestor.select_one(selector)[attribute]

        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError,TypeError):
        return None

selectors = {
            "author": ["span.user-post__author-name"],
            "recommendation": ["span.user-post__author-recomendation > em"],
            "stars": ["span.user-post__score-count"],
            "content": ["div.user-post__text"],
            "useful": ["button.vote-yes > span"],
            "useless": ["button.vote-no > span"],
            "published": ["span.user-post__published > time:nth-child(1)","datetime"],
            "purchased": ["span.user-post__published > time:nth-child(2)","datetime"],
            "pros": ["div[class$=positives] ~ div.review-feature__item", None, True],
            "cons": ["div[class$=negatives] ~ div.review-feature__item", None, True]
        }
    


source=input("Your product id, or the full link: ")
if not isinstance(source, int):
    source="".join(map(str,re.findall(r"\d", source)))

url= "https://www.ceneo.pl/"+source+"#tab=reviews"
all_opinions = []
while(url):
    response=requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")
    opinions = page.select("div.js_product-review")

    for opinion in opinions:
        single_opinion = {
            key: get_item(opinion, *value)
                for key, value in selectors.items()
        }
        single_opinion["opinion_id"] = opinion["data-entry-id"]
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None
file_attributes="opinions/"+source+".json"
with open(file_attributes, "w", encoding="UTF-8") as  jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
