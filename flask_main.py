from flask import Flask, render_template, request, redirect
from scrapper import extract_player


app = Flask('FIFA_Scrapper')

@app.route("/")
def home():
    return render_template("futbin.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
    else:
        return redirect("/")
    return render_template("results.html", Search_by=word, process='loading')


app.run()