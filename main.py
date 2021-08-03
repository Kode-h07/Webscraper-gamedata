from extract_data import extract_articles, extract_news


from save import save_to_file
articles = extract_articles()
save_to_file(articles)



