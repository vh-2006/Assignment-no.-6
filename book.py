books = []
issued_books = {}

def add_book(book_id, title, author, copies=1):
    if not str(book_id).strip() or not title.strip() or not author.strip():
        return False
    if not isinstance(copies, int) or copies < 1:
        return False
    if search_book(book_id) is not None:
        return False

    book = {
        "book_id": str(book_id),
        "title": title,
        "author": author,
        "copies": copies,
        "available": copies
    }
    books.append(book)
    return True

def search_book(book_id):
    for book in books:
        if book["book_id"] == str(book_id):
            return book
    return None
