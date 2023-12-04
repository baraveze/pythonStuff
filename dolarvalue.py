import requests
from bs4 import BeautifulSoup

url = 'https://www.ambito.com/contenidos/dolar-cl.html'
print (url)
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
for element in range(soup.find_all('span').count):
    print(element.text.strip())