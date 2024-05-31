import strawberry
from strawberry.types import Info

from configs.GraphQL import get_author_service, get_book_service
from models.AuthorModel import Author
from models.BookModel import Book


@strawberry.type(description="Query all entities")
class Query:
    @strawberry.field(description="Get an Author")
    def author(self, id: int, info: Info) -> Author:
        author_service = get_author_service(info)
        return author_service.get(id)

    @strawberry.field(description="List all Authors")
    def authors(self, info: Info) -> list[Author]:
        author_service = get_author_service(info)
        return author_service.list_items()

    @strawberry.field(description="Get a Book")
    def book(self, id: int, info: Info) -> Book:
        book_service = get_book_service(info)
        return book_service.get(id)

    @strawberry.field(description="List all Books")
    def books(self, info: Info) -> list[Book]:
        book_service = get_book_service(info)
        return book_service.list_items()
