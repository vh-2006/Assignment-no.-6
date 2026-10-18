from book import search_book, issued_books


def issue_book(book_id, student_id):
    book = search_book(book_id)
    if book is None or not str(student_id).strip():
        return False
    if book["available"] <= 0:
        return False

    book["available"] -= 1
    issued_books.setdefault(str(student_id), []).append(str(book_id))
    return True


def return_book(book_id, student_id):
    book = search_book(book_id)
    student_id = str(student_id)
    book_id = str(book_id)

    if book is None or student_id not in issued_books:
        return False
    if book_id not in issued_books[student_id]:
        return False

    issued_books[student_id].remove(book_id)
    book["available"] += 1
    if not issued_books[student_id]:
        del issued_books[student_id]
    return True
