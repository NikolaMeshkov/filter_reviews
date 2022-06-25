

from tkinter import *
window = Tk()
import json




is_filter_applied = False
selected_low_high = ""
selected_min_rating = ""
selected_by_date = ""
selected_priority = ""

def apply_filters():
    
    is_filter_applied = True
    window.destroy()

def select_low_high(selected):
    
    selected_low_high = selected

def select_min_rating(selected):
    
    selected_min_rating = selected


def select_by_date(selected):
    
    selected_by_date = selected

def select_priority(selected):
    
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

button = Button(window, text='Filter', command=apply_filters)
button.pack()

mainloop()





json_file = open('reviews.json', 'r', encoding='utf-8-sig')

file_content = json_file.read()

reviews_list = json.loads(file_content)


def filter_reviews(reviews):
	return sorted(reviews, key=lambda review: bool(review['reviewText']), reverse=True) 

def order_by_rating(reviews):
	return sorted(reviews, key=lambda review: review['rating'], reverse=True)

def order_by_date(reviews):
	return sorted(reviews, key=lambda review: review['reviewCreatedOnDate'])
	

def filter_by_stars(reviews, min_review):
	helper_list = []
	for item in reviews:
		if item['rating'] >= min_review:
			helper_list.append(item)
	
	return helper_list


reviews_list = filter_by_stars(reviews_list, 3)
reviews_list = order_by_date(reviews_list)
reviews_list = order_by_rating(reviews_list)


# if selected_priority == 'Yes':
if True:
	reviews_list = filter_reviews(reviews_list)

print(reviews_list)

