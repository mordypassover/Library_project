from fastapi import APIRouter, Body, HTTPException
from database.member_db import MemberDBManager
from database.db_connection import DBConnection

mdbm = MemberDBManager()

router = APIRouter()

connector = DBConnection()

@router.post("/members",status_code=201)
def add_member_to_library(data:dict = Body(...)):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        mdbm.create_member(data,conn)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn:
            conn.close()