from fastapi import Depends
from strawberry.types import Info

from models.author_model import Author
from models.book_model import Book
from services import Service
from services.author_service import AuthorService
from services.book_service import BookService


# GraphQL Dependency Context
async def get_graphql_context(
    author_service: AuthorService = Depends(),
    book_service: BookService = Depends(),
) -> dict[str, Service[Book | Author, int]]:
    return {
        "author_service": author_service,
        "book_service": book_service,
    }


# Extract AuthorService instance from GraphQL context
def get_author_service(info: Info) -> AuthorService:
    author_service: AuthorService = info.context["author_service"]
    return author_service


# Extract BookService instance from GraphQL context
def get_book_service(info: Info) -> BookService:
    book_service: BookService = info.context["book_service"]
    return book_service
