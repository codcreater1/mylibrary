from library import Library
from book import Book
# I want to create a library and display its name

our_library = Library('Wseiz Library', 'Rejtana 17, Warsaw')

print("The name: ", our_library.name)

our_book = Book('Robinson Cruzeo', 300, 'adventure', 'J.J Rowling', '3423-kdsjflkdsjfkl')
our_library.add_book(our_book)
