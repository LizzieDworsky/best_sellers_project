

class Book:
    def __init__(self, book={}):
        self.name = book["name"]
        self.author = book["author"]
        self.user_rating = book["user_rating"]
        self.number_of_reviews = book["number_of_reviews"]
        self.price = book["price"]
        self.year = book["year"]
        self.genre = book["genre"]