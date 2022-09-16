from book import Book
from data import data_list

# Should be using both lambda and list comprehension for each evaluation

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

# books_2018_2 = custom_filter(lambda item : item.year == 2018, book_list)

# for book in books_2018_2:
#     print(book.year)

# (5 points): As a data analyst, I want to determine what book had the lowest number of reviews in 2018. (Analysis 1)

def least_reviews_2018(list_of_books):
    books_2018 = [book for book in list_of_books if book.year == 2018]
    current_book = books_2018[0]
    for book in books_2018:
        if current_book.number_of_reviews > book.number_of_reviews:
            current_book = book
    return current_book

# results = least_reviews_2018(book_list)
# print(f"The book with the least amount of reviews in 2018 is {results.name}.")


# (5 points): As a data analyst, I want to determine which genre (fiction/non-fiction) has appeared the most in the top 50s list and print the result to the terminal. (Analysis 2)

def get_top_50(list_of_books):
    user_ratings = 4.9
    top_50_books = []
    while len(top_50_books) <= 50:
        temp_list = custom_filter(lambda item : item.user_rating > user_ratings, list_of_books)
        top_50_books.extend(temp_list)
        user_ratings -= .1
    while len(top_50_books) != 50:
        current_book = top_50_books[0]
        for book in top_50_books:
            if book.number_of_reviews < current_book.number_of_reviews:
                current_book = book
        top_50_books.remove(current_book)
    return top_50_books    

def most_popular_genre(book_list):
    





# (5 points): As a data analyst, I want to determine what book has been in the top 50s list for the most years and print the book’s title and the number of times 
# it has appeared in the list to the terminal. (Analysis 3)

# (10 points): As a data analyst, I want to utilize lambda functions and list comprehension within the code responsible for executing each evaluation question solution.


# Bonus

# (5 points): As a data analyst, I want to determine what author has shown up on the top 50’s list the most and display the author in the terminal. (Bonus Analysis 1)
# HINT: Only count distinct books by that author - Do not include the same book in different years within the calculation

# (5 points): As a data analyst, I want to display the top book for each year based on the book’s user rating & the number of reviews. (Bonus Analysis 2)
# HINT: Find the top book by ordering by user rating and then ordering by number of reviews. Print the year and the book’s title to the terminal. 

# (5 points): As a data analyst, I want to determine which book has appeared the most in the top 50s list consecutively. (Bonus Analysis 2)