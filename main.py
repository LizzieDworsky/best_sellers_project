from book import Book
from data import data_list

def create_book_list(book_class, data_set={}):
    temp_list = []
    for book in data_set:
        temp_list.append(book_class(book))
    return temp_list

def custom_filter(lambda_function, book_list):
    temp_list = []
    for book in book_list:
        bool_check = lambda_function(book)
        if bool_check:
            temp_list.append(book)
    return temp_list

book_list = create_book_list(Book, data_list)

books_2018 = [book for book in book_list if book.year == 2018]

# least_reviews_2018 = custom_filter_get(lambda x : x.number_of_reviews, books_2018)
books_2018_2 = custom_filter(lambda item : item.year == 2018, book_list)

# for book in books_2018_2:
#     print(book.year)

current_book = books_2018[0]
for book in books_2018:
    if current_book.number_of_reviews > book.number_of_reviews:
        current_book = book
print(current_book.name)