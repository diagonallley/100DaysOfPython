from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/login", methods=["POST"])
def log_in():
    if request.method == "POST":
        username = request.form["name"]
        pwd = request.form["password"]
        print(username, pwd)
    return "YES"


if __name__ == "__main__":
    app.run(debug=True)
