from tkinter import *
import pandas
import random
to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    # print((current_card["French"], current_card["English"]))
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # to_learn.remove(current_card)
    canvas.itemconfig(card_bg, image=card_front_img)

    flip_time = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# next_card()
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash_Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_time = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")


canvas.grid(row=0, column=0, columnspan=2)

card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="word", font=("Ariel", 40, "italic"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()
