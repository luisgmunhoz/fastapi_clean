from fastapi import APIRouter, Depends, status

from schemas.pydantic.author_schema import AuthorSchema
from schemas.pydantic.book_schema import (
    BookAuthorPostRequestSchema,
    BookPostRequestSchema,
    BookSchema,
)
from services.book_service import BookService

BookRouter = APIRouter(prefix="/v1/books", tags=["book"])


@BookRouter.get("/", response_model=list[BookSchema])
def index(
    name: str | None = None,
    page_size: int = 100,
    start_index: int = 0,
    book_service: BookService = Depends(),
) -> list[dict[str, str]]:
    return [
        book.normalize()
        for book in book_service.list_items(name, page_size, start_index)
    ]


@BookRouter.get("/{id}", response_model=BookSchema)
def get(id: int, book_service: BookService = Depends()) -> dict[str, str]:
    book: dict[str, str] = book_service.get(id).normalize()
    return book


@BookRouter.post(
    "/",
    response_model=BookSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    book: BookPostRequestSchema,
    book_service: BookService = Depends(),
) -> dict[str, str]:
    created_book: dict[str, str] = book_service.create(book).normalize()
    return created_book


@BookRouter.patch("/{id}", response_model=BookSchema)
def update(
    id: int,
    book: BookPostRequestSchema,
    book_service: BookService = Depends(),
) -> dict[str, str]:
    updated_book: dict[str, str] = book_service.update(id, book).normalize()
    return updated_book


@BookRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, book_service: BookService = Depends()) -> None:
    return book_service.delete(id)


@BookRouter.get("/{id}/authors/", response_model=list[AuthorSchema])
def get_authors(id: int, book_service: BookService = Depends()) -> list[dict[str, str]]:
    return [author.normalize() for author in book_service.get_authors(id)]


@BookRouter.post("/{id}/authors/", response_model=list[AuthorSchema])
def add_author(
    id: int,
    author: BookAuthorPostRequestSchema,
    book_service: BookService = Depends(),
) -> list[dict[str, str]]:
    return [author.normalize() for author in book_service.add_author(id, author)]


@BookRouter.delete(
    "/{id}/authors/{author_id}",
    response_model=list[AuthorSchema],
)
def remove_author(
    id: int,
    author_id: int,
    book_service: BookService = Depends(),
) -> list[dict[str, str]]:
    return [author.normalize() for author in book_service.remove_author(id, author_id)]
