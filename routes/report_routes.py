from fastapi import APIRouter, Body, HTTPException
from database.book_db import BooksDBManager
from database.member_db import MemberDBManager
from database.db_connection import DBConnection


bdbm = BooksDBManager()
mdbm = MemberDBManager()

router = APIRouter()

connector = DBConnection()

@router.get("/reports/summary")
def get_summery():
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return {"total_books":bdbm.books_total_count(conn)[0],
                "available_books":bdbm.count_available_books(conn)[0],
                "currently_borrowed":bdbm.count_borrowed_books(conn)[0],
                "active_members": mdbm.count_active_members(conn)[0]}
    finally:
        if conn:
            conn.close()

@router.get("/reports/books-by-genre")
def get_book_by_gener(genre:str):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return {genre:bdbm.count_by_genre(genre, conn)}
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/reports/top-member")
def get_top_member():
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.get_top_member(conn)
    finally:
        if conn:
            conn.close()