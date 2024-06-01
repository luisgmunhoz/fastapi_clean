from fastapi import Depends

from models.author_model import Author
from models.book_model import Book
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from schemas.graphql.book import BookMutationSchema
from schemas.pydantic.book_schema import BookAuthorPostRequestSchema, BookSchema
from services import Service


class BookService(Service[Book, int]):
    author_repository: AuthorRepository
    book_repository: BookRepository

    def __init__(
        self,
        author_repository: AuthorRepository = Depends(),
        book_repository: BookRepository = Depends(),
    ) -> None:
        self.author_repository = author_repository
        self.book_repository = book_repository

    def create(self, book_body: BookSchema | BookMutationSchema) -> Book:
        return self.book_repository.create(Book(name=book_body.name))

    def delete(self, book_id: int) -> None:
        return self.book_repository.delete(Book(id=book_id))

    def get(self, book_id: int) -> Book:
        return self.book_repository.get(Book(id=book_id))

    def list_items(
        self,
        name: str | None = None,
        page_size: int = 100,
        start_index: int = 0,
    ) -> list[Book]:
        return self.book_repository.list_items(name, page_size, start_index)

    def update(self, book_id: int, book_body: BookSchema | BookMutationSchema) -> Book:
        return self.book_repository.update(book_id, Book(name=book_body.name))

    def get_authors(self, book_id: int) -> list[Author]:
        book: Book = self.book_repository.get(Book(id=book_id))
        authors: list[Author] = book.authors
        return authors

    def add_author(
        self,
        book_id: int,
        author_body: BookAuthorPostRequestSchema,
    ) -> list[Author]:
        author = self.author_repository.get(Author(id=author_body.author_id))
        book = self.book_repository.get(Book(id=book_id))
        book.authors.append(author)
        self.book_repository.update(book_id, book)

        authors: list[Author] = book.authors
        return authors

    def remove_author(self, book_id: int, author_id: int) -> list[Author]:
        book = self.book_repository.get(Book(id=book_id))
        book.authors = list(
            filter(
                lambda author: author.id != author_id,
                book.authors,
            )
        )
        self.book_repository.update(book_id, book)
        authors: list[Author] = book.authors
        return authors
