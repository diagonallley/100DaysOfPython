from flask import Flask
from flask import render_template
import random
import datetime
import requests
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 9)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, y=year)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    URL = "https://api.npoint.io/82784a5b6b198ef68cf9"
    data = requests.get(URL)
    blogs = data.json()
    return render_template("blog.html", blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
