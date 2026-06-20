from database import get_all_quotes, init_database

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/quotes")
def quotes_list():
    quotes = get_all_quotes()
    return render_template("quotes.html", quotes=quotes)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    init_database()
    app.run(debug=True)