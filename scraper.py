import requests

from bs4 import BeautifulSoup

url = input()
r = requests.get(url)

def parse_site():
    soup = BeautifulSoup(r.content, 'html.parser')
    h1 = soup.find('h1')
    desc = soup.find('span', {'data-testid': 'plot-l'})
    info = {'title': h1.text, 'description': desc.text}
    print(info)

if url.find('title') == -1:
    print("Invalid movie page!")
else:
    parse_site()
