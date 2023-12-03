import requests
from bs4 import BeautifulSoup

url = 'https://www.clarin.com'
print (url)
response = requests.get(url)
html = response.text

soup =BeautifulSoup(html, 'html_parser')
soup.find_all('h1')[-1].text.strip()