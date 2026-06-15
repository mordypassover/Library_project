from fastapi import APIRouter, Body, HTTPException
from database.book_db import BooksDBManager
from database.member_db import MemberDBManager
from database.db_connection import DBConnection

bdbm = BooksDBManager()
mdbm = MemberDBManager()

router = APIRouter()

connector = DBConnection()

@router.post("/books",status_code=201)
def add_book_to_library(data:dict = Body(...)):
    conn = False
    try:
        title:str = data["title"]
        author:str = data["author"]
        genre:str =  data["genre"]
        conn = connector.get_connection_to_db()
        bdbm.create_book(title=title, author=author, genre=genre, conn=conn)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/books")
def get_all_books():
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return bdbm.get_all_books(conn)
    finally:
        if conn:
            conn.close()

@router.get("/books/{id}")
def get_book_via_id(id:int):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return bdbm.get_book_by_id(id, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.put("/books/{id}")
def update_book_via_id(id:int, data:dict = Body(...)):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return bdbm.update_book(id, data, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.put("/books/{id}/borrow/{member_id}")
def borrow_book(id:int, member_id:int):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        update_success =  bdbm.set_available(id, False, member_id, conn)
        mdbm.increment_borrows(member_id, conn)
        return update_success
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:

        if conn:
            conn.close()

@router.put("/books/{id}/return/{member_id}")
def return_book(id:int, member_id:int):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return bdbm.set_available(id, True, member_id, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()