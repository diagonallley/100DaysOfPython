from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from email_validator import validate_email, EmailNotValidError
import os
from flask_bootstrap import Bootstrap5

SECRET_KEY = os.urandom(32)


class MyForm(FlaskForm):
    email = StringField("email", validators=[
        DataRequired()])
    password = PasswordField("password", validators=[
                             DataRequired(), Length(min=8, max=30)])
    submit = SubmitField(label="log in")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app=app)


@app.route("/")
def home():
    return render_template("index_.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    form = MyForm()

    if form.validate_on_submit():
        print(form.email.data)
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            print("sdfejekljfk;fewjfkewfjewkjf")
            return render_template("yes.html")
        else:
            return render_template("denied.html")
    return render_template("form.html", form=form)


app.secret_key = "any-string"


if __name__ == "__main__":
    app.run(debug=True)
