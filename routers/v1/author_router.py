from fastapi import APIRouter, Depends, status

from schemas.pydantic.author_schema import AuthorPostRequestSchema, AuthorSchema
from schemas.pydantic.book_schema import BookSchema
from services.author_service import AuthorService

AuthorRouter = APIRouter(prefix="/v1/authors", tags=["author"])


@AuthorRouter.get("/", response_model=list[AuthorSchema])
def index(
    name: str | None = None,
    page_size: int = 100,
    start_index: int = 0,
    author_service: AuthorService = Depends(),
) -> list[dict[str, str]]:
    return [
        author.normalize()
        for author in author_service.list_items(name, page_size, start_index)
    ]


@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: int, author_service: AuthorService = Depends()) -> dict[str, str]:
    author: dict[str, str] = author_service.get(id).normalize()
    return author


@AuthorRouter.post(
    "/",
    response_model=AuthorSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    author: AuthorPostRequestSchema,
    author_service: AuthorService = Depends(),
) -> dict[str, str]:
    created_author: dict[str, str] = author_service.create(author).normalize()
    return created_author


@AuthorRouter.patch("/{id}", response_model=AuthorSchema)
def update(
    id: int,
    author: AuthorPostRequestSchema,
    author_service: AuthorService = Depends(),
) -> dict[str, str]:
    updated_author: dict[str, str] = author_service.update(id, author).normalize()
    return updated_author


@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, author_service: AuthorService = Depends()) -> None:
    return author_service.delete(id)


@AuthorRouter.get("/{id}/books/", response_model=list[BookSchema])
def get_books(
    id: int, author_service: AuthorService = Depends()
) -> list[dict[str, str]]:
    return [book.normalize() for book in author_service.get_books(id)]
