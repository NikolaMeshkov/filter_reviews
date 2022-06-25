

from tkinter import *
window = Tk()
import json




is_filter_applied = False
selected_low_high = ""
selected_min_rating = ""
selected_by_date = ""
selected_priority = ""

def callback():
    print ('You clicked the button!')
    is_filter_applied = True
    window.destroy()

def select_low_high(selected):
    print(selected)
    selected_low_high = selected

def select_min_rating(selected):
    print(selected)
    selected_min_rating = selected


def select_by_date(selected):
    print(selected)
    selected_by_date = selected

def select_priority(selected):
    print(selected)
    selected_priority = selected


window.geometry('325x250')
window.configure(background = "white")


low_high = StringVar(window)
low_high.set("") # default value
w1 = OptionMenu(window, low_high, "Highest first", "Lowest first", command=select_low_high)

min_rating = StringVar(window)
min_rating.set('')
w2 = OptionMenu(window, min_rating, '1', '2', '3', '4', '5', command=select_low_high)

date_order = StringVar(window)
date_order.set('')
w3 = OptionMenu(window, date_order, 'Oldest first', 'Newest first', command=select_by_date)

prioritize_by_text = StringVar(window)
prioritize_by_text.set('')
w4 = OptionMenu(window, prioritize_by_text, 'Yes', 'No', command=select_priority)
w1.pack()
w2.pack()
w3.pack()
w4.pack()

text = StringVar(window)
text.set('Filter')

button = Button(window, text='Filter', command=callback)
button.pack()

mainloop()



