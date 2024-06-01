import strawberry
from strawberry.types import Info

from configs.GraphQL import get_author_service, get_book_service
from schemas.graphql.Author import AuthorMutationSchema, AuthorSchema
from schemas.graphql.Book import BookMutationSchema, BookSchema


@strawberry.type(description="Mutate all Entity")
class Mutation:
    @strawberry.field(description="Adds a new Author")
    def add_author(self, author: AuthorMutationSchema, info: Info) -> AuthorSchema:
        author_service = get_author_service(info)
        return author_service.create(author)

    @strawberry.field(description="Delets an existing Author")
    def delete_author(self, author_id: int, info: Info) -> None:
        author_service = get_author_service(info)
        return author_service.delete(author_id)

    @strawberry.field(description="Updates an existing Author")
    def update_author(
        self,
        author_id: int,
        author: AuthorMutationSchema,
        info: Info,
    ) -> AuthorSchema:
        author_service = get_author_service(info)
        return author_service.update(author_id, author)

    @strawberry.field(description="Add a new Book")
    def add_book(self, book: BookMutationSchema, info: Info) -> BookSchema:
        book_service = get_book_service(info)
        return book_service.create(book)

    @strawberry.field(description="Deletes an existing Book")
    def delete_book(self, book_id: int, info: Info) -> None:
        book_service = get_book_service(info)
        return book_service.delete(book_id)

    @strawberry.field(description="Deletes an existing Book")
    def update_book(
        self,
        book_id: int,
        book: BookMutationSchema,
        info: Info,
    ) -> BookSchema:
        book_service = get_book_service(info)
        return book_service.update(book_id, book)
