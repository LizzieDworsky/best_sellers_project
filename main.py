from book import Book
from data import data_list

def create_book_list(book_class, data_set={}):
    temp_list = []
    for book in data_set:
        temp_list.append(book_class(book))
    return temp_list

def custom_filter(lambda_function, book_list):
    pass

book_list = create_book_list(Book, data_list)
