import pytest

from library import Book

# @pytest.mark.skip
def test_add_books(library):

    book1 = Book("Python", 100)
    book2 = Book("Pytest", 200)

    library.add_book(book1)
    library.add_book(book2)

    assert library.get_all_books() == ["Python", "Pytest"]

# @pytest.mark.xfail
@pytest.mark.smoke
def test_total_pages(library):

    book1 = Book("Python", 100)
    book2 = Book("Pytest", 200)

    library.add_book(book1)
    library.add_book(book2)

    assert library.get_total_pages() == 300

@pytest.mark.smoke
def test_remove_books(library):

    book1 = Book("Python", 100)
    book2 = Book("Pytest", 200)

    library.add_book(book1)
    library.add_book(book2)

    library.remove_book("Pytest")

    assert library.get_all_books() == ["Python"]



