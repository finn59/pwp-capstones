#   author  : Finn Busk Sørensen
#   date    : Jan. 4th, 2019
#
#   project : TomeRater.py
#   path    : C:\Users\fbs\PycharmProjects\Capstone-project>
#   ver     : 0.9
#
#   description  :  class TomeRater manages the many methods of class User and class Book,
#                   keeps records of users and books, and has methods to analyze object data
#
#                   class User handles attributes associated with users
#
#                   class Book handles attributes associated with books
#
#                   class Fiction is a subclass of book, and inherits title and author attributes,
#                   defines a class Fiction specific attribute: author
#
#                   class Non_Fiction is a subclass of book, and inherits title and author attributes,
#                   defines a class Non_Fiction specific attributes: subject, and level
#
#   known issues :  method highest_rated_book in class TomeRater fails when calling
#                   method get_average_rating in class Books
#                   haven't been able to solve this problem so far.
#

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_nonfict = Non_Fiction(title, subject, level, isbn)
        return new_nonfict

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        high_read = float("-inf")
        most_read = None
        for book in self.books:
            num_read = self.books[book]
            if num_read > high_read:
                high_read = num_read
                most_read = book
        return most_read

    #   known issues :  method highest_rated_book in class TomeRater fails when calling
    #                   method get_average_rating in class Books
    #                   haven't been able to solve this problem so far /fbs.
    def highest_rated_book(self):
        highest_rating = float("-inf")
        best_book = None
        for book in self.books:
            average = book.get_average_rating()
            if average >= highest_rating:
                highest_rating = average
                best_book = book
                return (best_book)

    def most_positive_user(self):
        highest_rating = float("-inf")
        pos_user = None
        for user in self.users.values():
            average = user.get_average_rating()
            if average >  highest_rating:
                highest_rating = average
                pos_user = user
        return pos_user


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("email address for " + self.name + " has been updated to : " + self.email)

    def read_book(self, book, rating=None):
        if type(rating) == int or type(rating) == float:
            if rating >= 0 and rating <= 4:
                self.books[book] = rating
            else:
                print("Invalid rating")
                self.books[book] = None
        else:
            self.books[book] = None

    def get_average_rating(self):
        ave_rating = 0
        for rating in self.books.values():
            if type(rating) == int or type(rating) == float:
                if rating >= 0 and rating <= 4:
                    ave_rating += rating
                else:
                    print("Invalid rating")
        return ave_rating / len(self.books)

    def __repr__(self):
        return ("User: " + self.name + ", email: " + self.email + ", books read: " + (str(len(self.books))))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def add_rating(self, rating):
        if type(rating) == int or type(rating) == float:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
                return("Added rating : " + str(rating) + "  for book : " + self.title)
            else:
                return("Invalid Rating")
        else:
            return("Invalid Rating")

    def get_average_rating(self):
        ave_rating = 0
        rated_books = 0
        for rating in self.ratings:
            ave_rating += rating
            rated_books +=1
        ave_rating = ave_rating / rated_books
        return ave_rating

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return (self.title + " by " + self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return (self.title + ", a " + self.level + " manual on " + self.subject)

