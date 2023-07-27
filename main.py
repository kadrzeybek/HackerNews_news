import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
for link in soup.findAll('a'):
    x =  link.get('href')
    if 'http' in x:
        print(x)

