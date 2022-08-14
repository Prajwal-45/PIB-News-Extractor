import requests
from bs4 import BeautifulSoup
import feedparser

def get_desc(url):
    res = requests.get(url)
    feed = feedparser.parse(res.text)
    data = BeautifulSoup(feed["feed"]["summary"])
    res = []
    desc = []
    data = data.find_all("p")
    for i in data:
        if i not in res:
            res.append(i)
 
    for i in res: 
        desc.append(i.text)
        
    return desc