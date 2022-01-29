import requests
from bs4 import BeautifulSoup

load_url = "https://www.nikkei.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

for element in soup.find_all("p"):
    print(element.text)
    
    break

for element in hcap2 : soup.find(class_="k-card__title-piece"):
    print(hcap2.text)