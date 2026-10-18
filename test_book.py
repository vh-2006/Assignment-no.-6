import pytest
import book


@pytest.fixture(autouse=True)
def clear_books():
    book.books.clear()
    book.issued_books.clear()


def test_add_valid_book():
    assert book.add_book("B101", "Clean Code", "Robert Martin") is True


def test_reject_empty_title():
    assert book.add_book("B102", "", "Some Author") is False


def test_reject_invalid_copies():
    assert book.add_book("B103", "Python Basics", "A. Writer", 0) is False


def test_search_existing_book():
    book.add_book("B104", "Atomic Habits", "James Clear")
    found = book.search_book("B104")
    assert found is not None
    assert found["title"] == "Atomic Habits"


def test_search_missing_book():
    assert book.search_book("NOPE") is None


def test_reject_duplicate_book_id():
    book.add_book("B105", "Book One", "Author One")
    assert book.add_book("B105", "Book Two", "Author Two") is False
