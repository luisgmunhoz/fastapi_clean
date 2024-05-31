from unittest import TestCase
from unittest.mock import create_autospec, patch

from sqlalchemy.orm import Session

from models.AuthorModel import Author
from repositories.AuthorRepository import AuthorRepository


class TestAuthorRepository(TestCase):
    session: Session
    author_repository: AuthorRepository

    def setUp(self) -> None:
        super().setUp()
        self.session = create_autospec(Session)
        self.author_repository = AuthorRepository(self.session)

    @patch("models.AuthorModel.Author", autospec=True)
    def test_create(self, Author: Author) -> None:
        author = Author(name="JK Rowling")
        self.author_repository.create(author)

        # Should call add method on Session
        self.session.add.assert_called_once_with(author)

    @patch("models.AuthorModel.Author", autospec=True)
    def test_delete(self, Author: Author) -> None:
        author = Author(id=1)
        self.author_repository.delete(author)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(author)

    @patch("models.AuthorModel.Author", autospec=True)
    def test_get(self, Author: Author) -> None:
        author = Author(id=1)
        self.author_repository.get(author)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.AuthorModel.Author", autospec=True)
    def test_list(self, Author: Author) -> None:
        self.author_repository.list_items(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.author_repository.list_items("Stephen Knight", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(Author).filter_by.assert_called_once_with(
            name="Stephen Knight"
        )

    @patch("models.AuthorModel.Author", autospec=True)
    def test_update(self, Author: Author) -> None:
        author = Author(name="Ray Dalio")
        self.author_repository.update(id=1, author=author)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(author)
