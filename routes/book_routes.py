from fastapi import APIRouter, Body, HTTPException
from database.book_db import BooksDBManager

bdbm = BooksDBManager()

router = APIRouter()

@router.post("/books",status_code=201)
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

@router.get("/books/{id}")
def get_book_via_id(id:int):
    try:
        return bdbm.get_book_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/books/{id}")
def update_book_via_id(id:int, data:dict = Body(...)):
    try:
        return bdbm.update_book(id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/books/{id}/borrow/{member_id}")
def borrow_book(id, member_id):
    try:
        return bdbm.set_available(id, True, member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/books/{id}/return/{member_id}")
def return_book(id, member_id):
    try:
        return bdbm.set_available(id, True, member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))