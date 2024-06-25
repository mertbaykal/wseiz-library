from library import Library
from book import Book
from member import Member

def main():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    member1 = Member("John Doe")

    library.add_book(book1)
    library.add_member(member1)

    print(f"Books in library: {[book.title for book in library.books]}")
    print(f"Members of library: {[member.name for member in library.members]}")

if __name__ == "__main__":
    main()
