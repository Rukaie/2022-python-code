import requests
from bs4 import BeautifulSoup

load_url = "https://www.nikkei.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

for element in soup.find_all("p"):
    print(element.text)