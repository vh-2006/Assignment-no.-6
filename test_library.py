import pytest
import book
from library import issue_book, return_book

@pytest.fixture(autouse=True)
def clear_library_state():
    book.books.clear()
    book.issued_books.clear()

def test_issue_book_reduces_availability():
    book.add_book("B201", "Networks", "A. Author", 2)
    assert issue_book("B201", "ST01") is True
    assert book.search_book("B201")["available"] == 1

def test_cannot_issue_unavailable_book():
    book.add_book("B202", "Security", "B. Author", 1)
    assert issue_book("B202", "ST01") is True
    assert issue_book("B202", "ST02") is False

def test_cannot_issue_nonexistent_book():
    assert issue_book("MISSING", "ST01") is False

def test_return_book_restores_availability():
    book.add_book("B203", "Agile", "C. Author", 1)
    issue_book("B203", "ST03")
    assert return_book("B203", "ST03") is True
    assert book.search_book("B203")["available"] == 1

def test_reject_return_if_not_issued_to_student():
    book.add_book("B204", "Databases", "D. Author", 1)
    assert return_book("B204", "ST04") is False
