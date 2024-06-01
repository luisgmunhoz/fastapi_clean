from fastapi import Depends

from models.author_model import Author
from models.book_model import Book
from repositories.author_repository import AuthorRepository
from schemas.graphql.author import AuthorMutationSchema
from schemas.pydantic.author_schema import AuthorSchema
from services import Service


class AuthorService(Service[Author, int]):
    author_repository: AuthorRepository

    def __init__(self, author_repository: AuthorRepository = Depends()) -> None:
        self.author_repository = author_repository

    def create(self, author_body: AuthorSchema | AuthorMutationSchema) -> Author:
        return self.author_repository.create(Author(name=author_body.name))

    def delete(self, author_id: int) -> None:
        return self.author_repository.delete(Author(id=author_id))

    def get(self, author_id: int) -> Author:
        return self.author_repository.get(Author(id=author_id))

    def list_items(
        self,
        name: str | None = None,
        page_size: int = 100,
        start_index: int = 0,
    ) -> list[Author]:
        return self.author_repository.list_items(name, page_size, start_index)

    def update(
        self, author_id: int, author_body: AuthorSchema | AuthorMutationSchema
    ) -> Author:
        return self.author_repository.update(author_id, Author(name=author_body.name))

    def get_books(self, author_id: int) -> list[Book]:
        author = self.author_repository.get(Author(id=author_id))
        books: list[Book] = author.books
        return books
