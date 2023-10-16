import tkinter

window=tkinter.Tk()


window.title('GUI Program')
window.minsize(width=500, height=300)
window.config(padx=200,pady=200)

# Label
my_lable=tkinter.Label(text='this is a label',font=("Arial",24,"bold"))
# my_lable.pack()
# my_lable.place(x=100,y=200)
my_lable.grid(column=0,row=0)
my_lable.config(padx=20,pady=20)
# my_lable.pack(side='left',expand=True) # Places a component on the screen and automatically decides its position
my_lable["text"]="new_text"
my_lable.config(text="this_text")


# Button

def button_click():
    txt=input.get()
    my_lable.config(text=txt)

button=tkinter.Button(text='Click',command=button_click)
# button.pack(side='top')
button.grid(column=1,row=1)
button.config()





# Entry 
input=tkinter.Entry(width=10)
# input.pack()

input.grid(column=2,row=2)
choice=input.get()
window.mainloop()