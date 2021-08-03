import requests
from bs4 import BeautifulSoup


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





def extract_articles(url):
    news = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {"class": 'sun-row teaser'})
    for result in results:
        article = extract_news(result)
        news.append(article)
    return news

def get_articles(word):
    url = f"https://talksport.com/?s={word}"
    articles = extract_articles(url)
    return articles


