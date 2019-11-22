import requests
from bs4 import BeautifulSoup

#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

page = requests.get('https://www.allrecipes.com/recipe/18352/whipped-cream/')

soup = BeautifulSoup(page.text, 'html.parser')

#last_links = soup.find('div', class_='directions--section__steps')
#last_links.decompose()

directions = soup.find('span', class_='recipe-directions__list--item')
"""artist_name_list_items = directions.find_all('a')

# Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)"""