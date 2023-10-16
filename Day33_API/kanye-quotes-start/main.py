# from tkinter import *
import requests
import datetime


# def get_quote():
#     data = requests.get("https://api.kanye.rest")
#     data.raise_for_status()
#     data = data.json()
#     # print(data["quote"])
#     canvas.itemconfig(quote_text, text=data["quote"])
#     # Write your code here.


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
#     "Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)


# window.mainloop()


res = requests.get("https://api.sunrise-sunset.org/json", params={
    "lat": 19.075983,
    "lng": 72.877655,
    "formatted": 0
})
res.raise_for_status()
data = res.json()
sunrise_set = (data["results"]["sunrise"], data["results"]["sunset"])


time_now = datetime.datetime.now()
sunrise = sunrise_set[0].split("T")[1].split(":")[0]
sunset = sunrise_set[1].split("T")[1].split(":")[0]
print(sunrise, sunset)
print(time_now.hour)
