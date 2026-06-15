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
    pass

@router.get("/reports/books-by-genre")
def get_book_by_gener(enre:str):
    pass

@router.get("/reports/top-member")
def get_top_member():
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.get_top_member(conn)
    finally:
        if conn:
            conn.close()