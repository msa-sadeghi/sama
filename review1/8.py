from tkinter import *


def click_button():
    username_label.config({
        'bg':"red",
        'text' : 'خداحافظ'
    })


window = Tk()
window.geometry("400x600")
username_label = Label(window, text="سلام", bg="white", font=12, width=30)
username_label.pack()

my_button = Button(window, text="کلیک کن",command=click_button)
my_button.pack(pady=12)
window.mainloop()