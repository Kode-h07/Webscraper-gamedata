import csv

def save_to_file(articles):
    file = open('articles.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(['name', 'date', 'link'])
    for article in articles:
        writer.writerow(article.values())
    return