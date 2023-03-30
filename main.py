from tkinter import *
import random
import pyperclip
from data import data
COLOR = "#F9F5EB"

current_pair = {}


def next_pair():
    global current_pair
    current_pair = data[random.randint(0, len(data) - 1)]
    canvas.itemconfig(text, text=current_pair["english"])


def get_chinese():
    canvas.itemconfig(text, text=current_pair["mandarin"])


def copy_chinese():
    chinese_phrase = current_pair["mandarin"]
    pyperclip.copy(chinese_phrase)


window = Tk()
window.title("Mandarin Panda")
window.config(padx=50, pady=50, bg=COLOR)

canvas = Canvas(width=600, height=378, bg=COLOR, highlightthickness=0)
eng_img = PhotoImage(file="images/quoteBG.png")
canvas.create_image(300, 189, image=eng_img)
canvas.grid(row=0, column=0, columnspan=2)
text = canvas.create_text(300, 189, text="Text Filler", width=280, font=("Courier", 30, "bold"), fill=COLOR)


translate_img = PhotoImage(file="images/Translate.png")
translate_button = Button(image=translate_img, command=get_chinese, highlightthickness=0, borderwidth=0)
translate_button.grid(row=1, column=0, pady=30)

learn_more_img = PhotoImage(file="images/LearnMore.png")
learn_more_button = Button(image=learn_more_img, command=next_pair, highlightthickness=0, borderwidth=0)
learn_more_button.grid(row=2, column=0)

copy_img = PhotoImage(file="images/copy.png")
copy_button = Button(image=copy_img, command=copy_chinese, highlightthickness=0, borderwidth=0)
copy_button.grid(rowspan=2, row=1, column=1)

next_pair()

window.mainloop()
