from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.database import get_db_connection
from models.book_model import Book
from repositories import RepositoryMeta


class BookRepository(RepositoryMeta[Book, int]):
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list_items(
        self,
        name: str | None = None,
        limit: int | None = None,
        start: int | None = None,
    ) -> list[Book]:
        query = self.db.query(Book)
        if name:
            query = query.filter_by(name=name)

        books: list[Book] = query.offset(start).limit(limit).all()
        return books

    def get(self, book: Book) -> Book:
        return self.db.get(Book, book.id, options=[lazyload(Book.authors)])

    def create(self, book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, id: int, book: Book) -> Book:
        book.id = id
        self.db.merge(book)
        self.db.commit()
        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
