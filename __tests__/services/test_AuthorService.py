from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from schemas.pydantic.AuthorSchema import AuthorSchema
from services.AuthorService import AuthorService


class TestAuthorService(TestCase):
    author_repository: AuthorRepository
    author_service: AuthorService

    def setUp(self) -> None:
        super().setUp()
        self.author_repository = create_autospec(AuthorRepository)
        self.author_repository = create_autospec(BookRepository)
        self.author_service = AuthorService(self.author_repository)

    @patch(
        "schemas.pydantic.AuthorSchema.AuthorSchema",
        autospec=True,
    )
    def test_create(self, AuthorSchema: AuthorSchema) -> None:
        author = AuthorSchema()
        author.name = "JK Rowling"

        self.author_service.create(author)

        # Should call create method on Author Repository
        self.author_repository.create.assert_called_once()

    def test_delete(self) -> None:
        self.author_service.delete(author_id=1)

        # Should call delete method on Author Repository
        self.author_repository.delete.assert_called_once()

    def test_get(self) -> None:
        self.author_service.get(author_id=1)

        # Should call get method on Author Repository
        self.author_repository.get.assert_called_once()

    def test_list(self) -> None:
        name = "Rowling"
        pageSize = 10
        startIndex = 2

        self.author_service.list_items(name, pageSize, startIndex)

        # Should call list method on Author Repository
        self.author_repository.list_items.assert_called_once_with(
            name, pageSize, startIndex
        )

    @patch(
        "schemas.pydantic.AuthorSchema.AuthorSchema",
        autospec=True,
    )
    def test_update(self, AuthorSchema: AuthorSchema) -> None:
        author = AuthorSchema()
        author.name = "JRR Tokein"

        self.author_service.update(author_id=1, author_body=author)

        # Should call update method on Book Repository
        self.author_repository.update.assert_called_once()
