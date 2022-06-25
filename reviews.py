

from tkinter import *
window = Tk()
import json




is_filter_applied = False

def apply_filters():
	
	is_filter_applied = True
	window.destroy()


window.geometry('325x250')
window.configure(background = "white")


order_by_rating_var = StringVar(window)
order_by_rating_var.set("Highest first") # default value
w1 = OptionMenu(window, order_by_rating_var, "Highest first", "Lowest first")

min_rating = StringVar(window)
min_rating.set(1)
w2 = OptionMenu(window, min_rating, 1, 2, 3, 4, 5)

date_order = StringVar(window)
date_order.set('Oldest first')
w3 = OptionMenu(window, date_order, 'Oldest first', 'Newest first')

prioritize_by_text = StringVar(window)
prioritize_by_text.set('Yes')
w4 = OptionMenu(window, prioritize_by_text, 'Yes', 'No')
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


def order_by_has_text(reviews):

	return sorted(reviews, key=lambda review: bool(review['reviewText']), reverse=True) 

def order_by_rating(reviews, selected_order_by_rating1):
	is_reverse = False
	if selected_order_by_rating1 == "Highest first":
		is_reverse = True
	return sorted(reviews, key=lambda review: review['rating'], reverse=is_reverse)

def order_by_date(reviews,selected_by_date1):
	is_reverse = False
	if selected_by_date1 == "Highest first":
		is_reverse = True

	return sorted(reviews, key=lambda review: review['reviewCreatedOnDate'],reverse=is_reverse)
	

def filter_by_stars(reviews, min_review):
	helper_list = []
	for item in reviews:
		if item['rating'] >= min_review:
			helper_list.append(item)
	
	return helper_list

reviews_list = filter_by_stars(reviews_list, int(min_rating.get()))
reviews_list = order_by_date(reviews_list,date_order.get())
reviews_list = order_by_rating(reviews_list, order_by_rating_var.get())


if prioritize_by_text.get() == 'Yes':
	reviews_list = order_by_has_text(reviews_list)

print(reviews_list)

