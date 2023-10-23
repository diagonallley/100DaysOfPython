from flask import Flask, request
import smtplib
from flask.templating import render_template
import requests
import os

app = Flask(__name__)
data = requests.get("https://api.npoint.io/a12c46f1bbf1fd616cce")
blogs = data.json()
USER = os.environ.get("GMAIL_USER")
PWD = os.environ.get("GMAIL_PWD")
print(USER, PWD)


@app.route("/")
def get_all_posts():
    # blogs = blogs
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    print(USER, PWD)
    if request.method == "POST":
        mail_id = request.form["email"]
        message = request.form["message"]
        send_mail(mail_id, message)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


@app.route("/blog/<int:index>")
def get_blog(index):
    requested_blog = None
    for blog in blogs:
        if blog["id"] == index:
            requested_blog = blog
    return render_template("post.html", blog=requested_blog)


def send_mail(email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PWD)
        connection.sendmail(
            to_addrs="pythont481@gmail.com", from_addr=USER, msg=message)


# @app.route("/form-accept", methods=["POST"])
# def get_form_data():
#     if request.method == "POST":


if __name__ == "__main__":
    app.run(debug=True)
