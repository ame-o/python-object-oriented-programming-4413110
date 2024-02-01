# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Bless Me Ultima")
book2 = Book("Like Water for Chocolate")

# TODO: print the class and property
print(Book)
print(book1.title)