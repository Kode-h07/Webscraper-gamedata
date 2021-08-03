from flask import Flask, render_template, request, redirect
from scrapper import get_articles


app = Flask('Football_news_Scrapper')

db = {}

@app.route("/")
def home():
    return render_template("article_searching.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        article_exist = db.get(word)
        if article_exist:
            articles = article_exist
        else:
            articles = get_articles(word)
            db[word] = articles
    else:
        return redirect("/")
    return render_template("results.html",
                           Search_by=word,
                           process='loading',
                           result_number=len(articles),
                           articles = articles
                           )

@app.route("/export")
def export():
    #use try and except to raise error when user searches
    # for invalid "word" or there is no articles in db for that word
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        articles = db.get(word)
        if not articles:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")



app.run()