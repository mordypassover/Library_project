from fastapi import APIRouter, Body, HTTPException
from database.member_db import MemberDBManager
from database.db_connection import DBConnection
from mysql.connector import errors

mdbm = MemberDBManager()

router = APIRouter()

connector = DBConnection()

@router.post("/members",status_code=201)
def add_member_to_library(data:dict = Body(...)):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        mdbm.create_member(data,conn)
    except (KeyError, errors.IntegrityError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/members")
def get_all_members():
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.get_all_members(conn)
    finally:
        conn.close()

@router.get("/members/{id}")
def get_book_via_id(id:int):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.get_member_by_id(id, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.put("/members/{id}")

def update_member_by_id(id,  data:dict = Body(...)):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.update_member(id, data, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.put("/members/{id}/deactivate")
def deactivate_member(id):
    conn = False
    try:
        conn = connector.get_connection_to_db()
        return mdbm.deactivate_member(id, conn)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        if conn:
            conn.close()