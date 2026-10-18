import pytest
import book
from library import issue_book, return_book


@pytest.fixture(autouse=True)
def clear_library_state():
    book.books.clear()
    book.issued_books.clear()


def test_add_book_then_search():
    assert book.add_book(
        "B301",
        "Operating Systems",
        "Silberschatz",
        3) is True
    found = book.search_book("B301")
    assert found is not None
    assert found["title"] == "Operating Systems"
    assert found["available"] == 3


def test_complete_issue_and_return_workflow():
    book.add_book("B302", "Computer Networks", "Tanenbaum", 1)

    assert issue_book("B302", "ST10") is True
    assert book.search_book("B302")["available"] == 0

    assert return_book("B302", "ST10") is True
    assert book.search_book("B302")["available"] == 1


def test_issue_book_updates_student_record():
    book.add_book("B303", "Software Engineering", "Pressman", 2)
    assert issue_book("B303", "ST11") is True
    assert book.issued_books["ST11"] == ["B303"]
