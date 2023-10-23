from flask import Flask
from random import randint
app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        return_val = func()
        return f"<b>{return_val}</b>"
    return wrapper_function


# def make_emp(func):
#     def wrapper_function():
#         return_val = func()
#         return f"<em>{return_val}</em>"
#     return wrapper_function


# def make_underline(func):
#     def wrapper_function():
#         return_val = func()
#         return f"<u>{return_val}<u>"
#     return wrapper_function


# @app.route("/")
# def hello_world():
#     return "<h1>Hello</h1>"\
#         "<p>This is a </p>"\
#         '<iframe src="https://giphy.com/embed/gyRWkLSQVqlPi" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/need-nom-gyRWkLSQVqlPi">via GIPHY</a></p>'


# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name}, you are {number}"


# @app.route("/bye")

# @make_bold

# def bye():
#     return "bye"


@app.route("/")
@make_bold
def home():

    return "<div>Guess a number between 0 and 9</div>"\
        '<iframe src="https://giphy.com/embed/fDUOY00YvlhvtvJIVm" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/countdown-jmz-count-down-fDUOY00YvlhvtvJIVm">via GIPHY</a></p>'


random_number = randint(0, 9)


@app.route("/<int:number>")
def number(number):
    print(random_number)
    if number == random_number:
        return "<div><b style='color:pink'>YOU GOT ME</b></div><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number > random_number:
        return "<div><b style='color:blue'>Too high, try again</b></div><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < random_number:
        return "<div><b style='color:teal'>Too low, try again</b></div><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
