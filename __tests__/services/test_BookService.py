from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from schemas.pydantic.BookSchema import BookAuthorPostRequestSchema, BookSchema
from services.BookService import BookService


class TestBookService(TestCase):
    author_repository: AuthorRepository
    book_repository: BookRepository
    book_service: BookService

    def setUp(self) -> None:
        super().setUp()
        self.author_repository = create_autospec(AuthorRepository)
        self.book_repository = create_autospec(BookRepository)
        self.book_service = BookService(self.author_repository, self.book_repository)

    @patch(
        "schemas.pydantic.BookSchema.BookSchema",
        autospec=True,
    )
    def test_create(self, BookSchema: BookSchema) -> None:
        book = BookSchema()
        book.name = "Harry Potter and The Order of Phoenix"

        self.book_service.create(book)

        # Should call create method on Book Repository
        self.book_repository.create.assert_called_once()

    def test_delete(self) -> None:
        self.book_service.delete(book_id=1)

        # Should call delete method on Book Repository
        self.book_repository.delete.assert_called_once()

    def test_get(self) -> None:
        self.book_service.get(book_id=1)

        # Should call get method on Book Repository
        self.book_repository.get.assert_called_once()

    def test_list(self) -> None:
        name = "The Richest Man in Babylon"
        pageSize = 10
        startIndex = 2

        self.book_service.list_items(name, pageSize, startIndex)

        # Should call list method on Book Repository
        self.book_repository.list_items.assert_called_once_with(
            name, pageSize, startIndex
        )

    @patch(
        "schemas.pydantic.BookSchema.BookSchema",
        autospec=True,
    )
    def test_update(self, BookSchema: BookSchema) -> None:
        book = BookSchema()
        book.name = "Harry Potter and The Order of Phoenix"

        self.book_service.update(book_id=1, book_body=book)

        # Should call update method on Book Repository
        self.book_repository.update.assert_called_once()

    def test_get_authors(self) -> None:
        self.book_service.get_authors(book_id=1)

        # Should call get method on Book Repository
        self.book_repository.get.assert_called_once()

    @patch(
        "schemas.pydantic.BookSchema.BookAuthorPostRequestSchema",
        autospec=True,
    )
    def test_add_author(
        self, BookAuthorPostRequestSchema: BookAuthorPostRequestSchema
    ) -> None:
        author = BookAuthorPostRequestSchema()
        author.author_id = 3

        self.book_service.add_author(book_id=1, author_body=author)

        # Should call get method on Author Repository
        self.author_repository.get.assert_called_once()

        # Should call get method on Book Repository
        self.book_repository.get.assert_called_once()

        # Should call update method on Book Repository
        self.book_repository.update.assert_called_once()

    def test_remove_author(self) -> None:
        self.book_service.remove_author(book_id=1, author_id=2)

        # Should call get method on Book Repository
        self.book_repository.get.assert_called_once()

        # Should call update method on Book Repository
        self.book_repository.update.assert_called_once()
