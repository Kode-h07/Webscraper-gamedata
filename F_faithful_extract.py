import requests
from bs4 import BeautifulSoup


def extract_F_faithful_news(html):
    title = html.find('a', {'rel':'bookmark'}).text
    date = html.find('time', {'class': 'entry-date'}).text
    for a in html.find_all('a', href=True):
        link = a['href']
    return {
        'title': title,
        'date': date,
        'link': link
    }





def extract_F_faithful_articles(url):
    news = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('li', {"class": 'g1-collection-item'})
    for result in results:
        article = extract_F_faithful_news(result)
        news.append(article)
    return news
