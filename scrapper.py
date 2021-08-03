from bs4 import BeautifulSoup
import requests

def extract_data(html):
    name = html.find('div', {'class': 'pcdisplay-name'}).text
    overall = html.find('div', {'class': 'pcdisplay-rat'}).text
    position = html.find('div', {'class': 'pcdisplay-pos'}).text
    for a in html.find_all('a', href=True):
        link = 'https://www.futbin.com/'+a['href']
    return {
        'name': name,
        'overall': overall,
        'position': position,
        'link': link
    }





def extract_player(word):
    players = []
    result = requests.get("https://www.futbin.com/popular")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('li', {"class": 'popular-box'})
    for result in results:
        player = extract_data(result)
        players.append(player)
    return players



