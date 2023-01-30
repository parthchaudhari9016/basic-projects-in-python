import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"

r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)
title = soup.title
print(type(title))