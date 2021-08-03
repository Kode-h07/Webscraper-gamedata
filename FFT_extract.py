import requests
from bs4 import BeautifulSoup


def extract_442_news(html):
    title = html.find('h3', {'class': 'article-name'}).text
    date = html.find('time', {'class': 'published-date relative-date'}).text
    for a in html.find_all('a', {'class':'article-link'}, href=True):
        link = a['href']
    return {
        'title': title,
        'date': date,
        'link': link
    }





def extract_442_articles(url):
    news = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {"data-page": '1'})
    for result in results:
        article = extract_442_news(result)
        news.append(article)
    return news

