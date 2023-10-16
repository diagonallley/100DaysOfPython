from tkinter import *
from tkinter import messagebox
import pyperclip

import json
# Password


# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password = ""
    password_letters = [random.choice(letters)
                        for character in range(nr_letters)]

    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    # for i in range(0, nr_letters):
    #     password += random.choice(letters)

    # for j in range(0, nr_symbols):
    #     password += random.choice(symbols)

    # for i in range(0, nr_numbers):
    #     password += random.choice(numbers)

    password_list = password_letters+password_numbers+password_symbols

    random.shuffle(password_list)
    newpassword = "".join(password_list)
    password_entry.insert(0, newpassword)
    pyperclip.copy(newpassword)
    # return newpassword


def search_password():
    website_ = website.get()
    email_ = email.get()
    password_ = None
    try:
        with open("password.json", "r") as data:
            json_data = json.load(data)
            password_ = json_data[website_]["password"]
            messagebox.showinfo(
                title=website_, message=f"Email: {email_}\nPassword: {password_}")
            # password_entry.delete(0, END)
            # password_entry.insert(0, password_)
    except FileNotFoundError:
        messagebox.showerror(message="File not found")
    except KeyError:
        messagebox.showerror(message=f"Password not found for {website_}")
# Save Password


def save_password():
    website_ = website.get()
    email_ = email.get()
    password_ = password_entry.get()
    new_data = {website_: {
        "email": email_,
        "password": password_

    }}
    if len(website_) == 0 or len(password_) == 0:
        messagebox.showerror(
            message="You must enter the password and/or website")
    else:
        # is_ok = messagebox.askokcancel(
        #     title=website, message=f"These are the details entered: \nEmail:{email_} \nPassword: {password_}\nIs it ok to save? ")
        try:
            with open("password.json", "r") as data:  # Reading old data
                # json.dump(new_data, data, indent=2)
                json_data = json.load(data)  # returns a python dict

                # Updating old data with new data
        except FileNotFoundError:
            with open("password.json", "w") as data:
                json.dump(new_data, data, indent=2)
        else:
            json_data.update(new_data)

            with open('password.json', 'w') as data:
                # Saving update data
                json.dump(json_data, data, indent=2)
        finally:
            website.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title('Password Manager')

canvas = Canvas(height=200, width=200)


logo = PhotoImage(file='logo.png')


canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Website Entry
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
# website_label.config(padx=10)

website = Entry()
website.grid(column=1, row=1, columnspan=2)
website.config(width=35)
website.focus()


# Email Username

Email_username_label = Label(text="Email / Username:")
Email_username_label.grid(column=0, row=2)
# Email_username_label.config(padx=10)
email = Entry()
email.grid(column=1, row=2, columnspan=2)
email.config(width=35)
email.insert(0, "newgmail@gmail.com")
# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# password_label.config(padx=10)

password_entry = Entry()
password_entry.grid(column=1, row=3, columnspan=2)
# password.config(width=35)
password_entry.config(width=35)

add = Button(text='Add ', width=15, command=save_password)
add.grid(column=2, row=4, sticky='w')

search_button = Button(text='Search', command=search_password)
search_button.grid(row=4, column=0)
generate_password = Button(text='Generate Password',
                           width=26, command=generate_password)
generate_password.grid(row=4, column=1, sticky='e')

window.config(padx=50, pady=50)
window.mainloop()
