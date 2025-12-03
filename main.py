
from fastapi import FastAPI, Depends
from models import Book
from database import session, engine
import database_models

app = FastAPI()

database_models.base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


books = [
    Book(id=2, title="book 1", author="physics book", year=2000, isbn="abc", available = True),
    Book(id=6, title="book 2", author="math book", year=2014, isbn="xyz", available = True),
    Book(id=8, title="book 3", author="science book", year=2016, isbn="pqw", available = True),
    Book(id=10, title="book 4", author="java book", year=1992, isbn="sql", available = True),
]


def init_db():
    db = session()

    existing_count = db.query(database_models.Book).count()

    if existing_count == 0:
        for book in books:
            db.add(database_models.Book(**book.model_dump()))
        db.commit()
        print("Database initialized with sample book.")
        
    db.close()



@app.get("/books/")
def get_all_products(db: session = Depends(get_db)):
    products = db.query(database_models.Book).all()
    return books


@app.get("/books/{book_id}")
def get_product_by_id(book_id: int, db: session = Depends(get_db)):
    book = db.query(database_models.Book).filter(database_models.Book.id == book_id).first()
    if book:
        return book
    return {"error": "book not found"}


@app.post("/books/")
def create_product(book: Book, db: session = Depends(get_db)):
    db.add(database_models.Book(**book.model_dump()))
    db.commit()
    return {"message": "book created successfully", "book": book}
