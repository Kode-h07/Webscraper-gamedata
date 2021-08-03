from bs4 import BeautifulSoup
import requests


def extract_news(html):
    title = html.find('p', {'class': 'teaser__subdeck'}).text
    title = str(title)
    title = title[4: -2]
    date = html.find('div', {'class': 'search-date'}).text
    for a in html.find_all('a', {'class':'teaser-anchor teaser-anchor--search'}, href=True):
        link = a['href']
    return {
        'title': title,
        'date': date,
        'link': link
    }





def extract_articles():
    news = []
    result = requests.get("https://talksport.com/?s=manchester%20united")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {"class": 'sun-row teaser'})
    for result in results:
        article = extract_news(result)
        news.append(article)
    return news




