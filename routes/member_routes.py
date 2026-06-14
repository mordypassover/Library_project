from fastapi import APIRouter, Body, HTTPException
from database.member_db import MemberDBManager

mdbm = MemberDBManager()

router = APIRouter()

@router.post("/members",status_code=201)
def add_member_to_library(data:dict = Body(...)):
    try:
        mdbm.create_member(data)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
