from random import choice

from flask import Flask, render_template

app = Flask(__name__)

quotes = [
    "Computer science is no more about computers than astronomy is about telescopes.",
    "To understand recursion you must first understand recursion.",
    "The limits of my language are the limits of my mind.",
    "Mathematics is the key and door to the sciences.",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/quotes")
def random_quote():
    quote = choice(quotes)
    return render_template("quotes.html", quote=quote)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)