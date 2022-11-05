import requests
from bs4 import BeautifulSoup

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = [h3.text for h3 in soup.findAll('h3')]
print(items)
