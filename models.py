from pydantic import BaseModel

class Book(BaseModel):

    id: int
    title: str
    author: str
    year: int
    isbn: str
    available: bool
    