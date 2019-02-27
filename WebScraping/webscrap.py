import requests
from bs4 import BeautifulSoup
import lxml
import csv 

pages = []

headers = {
    'User-Agent' : 'Ricardo',
    'From' : 'ricardogleitao@hotmail.com'
}

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121010201041/http://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

    for item in pages:
        page = requests.get(item, headers = headers)
        soup = BeautifulSoup(page.text, 'lxml')
        # print(soup)

        last_links = soup.find(class_='AlphaNav')
        last_links.decompose()

        archiveCSV = csv.writer(open('C:\\Users\\ricardo.leitao\\Desktop\\WebScraping\\z-artists-names-links.csv', 'w'))
        archiveCSV.writerow(['Name', 'Link'])

        frameArtistName = soup.find(class_='BodyText')
        listArtistName = frameArtistName.find_all('a')

        for artistNames in listArtistName:
            names = artistNames.contents[0]
            links = 'https://web.archive.org/' + artistNames.get('href')
            archiveCSV.writerow([names, links])

















