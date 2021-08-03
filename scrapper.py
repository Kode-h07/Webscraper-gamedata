from TalkSports_extract import extract_ts_articles, extract_ts_news
from FFT_extract import extract_442_articles, extract_442_news

def get_articles(word):
    ts_url = f"https://talksport.com/?s={word}"
    ts_articles = extract_ts_articles(ts_url)
    fft_url = f"https://www.fourfourtwo.com/search?searchTerm={word}"
    fft_articles = extract_442_articles(fft_url)

    articles = fft_articles + ts_articles
    return articles



