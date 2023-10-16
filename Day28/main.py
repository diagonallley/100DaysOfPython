
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
Timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps 
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark+="✔️"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('Pomodoro')
canvas = Canvas(width=220, height=226)


image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=image)
canvas.config(bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(
    103, 132, text="00.00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
# count_down(5)


# Timer Label

timer_label = Label()
timer_label.config(text='Timer', bg=YELLOW, fg=GREEN,
                   font=(FONT_NAME, 45, 'bold'))
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


# Reset Button
reset_button = Button(text='Reset', highlightthickness=0,command=reset)
reset_button.grid(column=2, row=2)


# Check marks
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_marks.grid(column=1, row=3)

window.mainloop()
