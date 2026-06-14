from fastapi import APIRouter, Body, HTTPException
from database.book_db import BooksDBManager

bdbm = BooksDBManager()

router = APIRouter()

@router.post("/books")
def add_book_to_library(data:dict = Body(...)):
    try:
        title:str = data["title"]
        author:str = data["author"]
        genre:str =  data["genre"]
        bdbm.create_book(title=title, author=author, genre=genre)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/books")
def get_all_books():
    return bdbm.get_all_books()