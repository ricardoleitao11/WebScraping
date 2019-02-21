import requests
from bs4 import BeautifulSoup
import lxml

page = requests.get('https://web.archive.org/web/20121010201041/http://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

















