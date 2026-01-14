from fastapi import APIRouter, HTTPException
from storage import *

router = APIRouter()


@router.post("/coordinates")
def saving_in_db(ip_json:dict):
    try:
        writing(ip_json)
        return {"status": "ok", "data": ip_json}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get-all")
def get_all():
    try:
        return get_all_ip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

