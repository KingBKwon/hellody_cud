from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.CRUD.review import *

router = APIRouter(prefix='/review')

class Review_info(BaseModel):
    RATING : str
    COMMENT : str

@router.post('/{user_id}')
def insert_review(user_id: int, id: int, title: str, review_info: Review_info):
    result = insert_reviewinfo(user_id, id, title, review_info)
    if result:
        return JSONResponse(content={'response': 'FINISH INSERT REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

@router.put('/{user_id}')
def update_review(user_id: int, id: int, title: str, review_info: Review_info):
    result = update_reviewinfo(user_id, id, title, review_info)
    if result:
        return JSONResponse(content={'response': 'FINISH UPDATE REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

@router.delete('/{user_id}')
def update_review(review_id: int):
    result = delete_reviewinfo(review_id)
    if result:
        return JSONResponse(content={'response': 'FINISH UPDATE REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)
