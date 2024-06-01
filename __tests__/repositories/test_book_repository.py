from unittest import TestCase
from unittest.mock import create_autospec, patch

from sqlalchemy.orm import Session

from models.book_model import Book
from repositories.book_repository import BookRepository


class TestBookRepository(TestCase):
    session: Session
    book_repository: BookRepository

    def setUp(self) -> None:
        super().setUp()
        self.session = create_autospec(Session)
        self.book_repository = BookRepository(self.session)

    @patch("models.book_model.Book", autospec=True)
    def test_create(self, Book: Book) -> None:
        book = Book(name="Harry Potter and The Order of Phoenix")
        self.book_repository.create(book)

        # Should call add method on Session
        self.session.add.assert_called_once_with(book)

    @patch("models.book_model.Book", autospec=True)
    def test_delete(self, Book: Book) -> None:
        book = Book(id=1)
        self.book_repository.delete(book)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(book)

    @patch("models.book_model.Book", autospec=True)
    def test_get(self, Book: Book) -> None:
        book = Book(id=1)
        self.book_repository.get(book)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.book_model.Book", autospec=True)
    def test_list(self, Book: Book) -> None:
        self.book_repository.list_items(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.book_repository.list_items("Peaky Blinders", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(Book).filter_by.assert_called_once_with(
            name="Peaky Blinders"
        )

    @patch("models.book_model.Book", autospec=True)
    def test_update(self, Book: Book) -> None:
        book = Book(name="The Wealth of Nations")
        self.book_repository.update(id=1, book=book)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(book)
