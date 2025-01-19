
class Book:
    """Represents a book.

    Attributes:
        id_ (int): The unique identifier of the book.
        name (str): The title of the book.
        pages (int): The number of pages in the book. Must be a non-negative integer.

    """
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id_ must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("pages must be a non-negative integer")

        self.id_: int = id_
        self.name: str = name
        self.pages: int = pages

    def __str__(self) -> str:
        """Returns a string representation of the book."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Returns a string that can be used to recreate the Book object."""
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


if __name__ == '__main__':
    # Initialize a list of books
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Test __str__ method

    print(list_books)  # Test __repr__ method - shows how to recreate the objects

