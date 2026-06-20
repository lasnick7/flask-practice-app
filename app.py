from database import add_quote, get_all_quotes, init_database

from flask import Flask, redirect, render_template, request

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


@app.route("/add", methods=["GET", "POST"])
def add_quote_page():
    if request.method == "POST":
        text = request.form["text"]
        author = request.form["author"]

        add_quote(text, author)

        return redirect("/quotes")

    return render_template("add_quote.html")


if __name__ == "__main__":
    init_database()
    app.run(debug=True)