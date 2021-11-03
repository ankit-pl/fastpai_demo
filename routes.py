from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from schemas.post import PostCreate, PostUpdate, Post as PostDisplay
from sqlalchemy.orm import Session
from models.post import Post as PostModel
from db.session import session_local
from fastapi_localization import TranslateJsonResponse, lazy_gettext as _
from typing import List

router = APIRouter()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


# @router.get("/", response_class=TranslateJsonResponse, response_model=List[PostDisplay])
# def display_all_posts(db: Session = Depends(get_db)):
#     posts = db.query(PostModel).all()
#     if not posts:
#         raise HTTPException(status_code=404, detail=_("NO POSTS CREATED YET"))
#     return posts


# @router.post("/posts", response_class=TranslateJsonResponse, response_model=PostDisplay)
# def create_post(request: PostCreate, db: Session = Depends(get_db)):
#     post = PostModel(title=request.title, content=request.content)
#     if not post:
#         raise HTTPException(status_code=500, detail=_("INTERNAL SERVER ERROR"))
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post


# @router.get("/posts/{id}", response_class=TranslateJsonResponse, response_model=PostDisplay)
# def read_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(PostModel).filter(PostModel.id == id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=_(f"NO POST FOUND WITH ID: {id}"))
#     return post


# @router.put("/posts/{id}", response_class=TranslateJsonResponse, response_model=PostDisplay)
# def update_post(id: int, request: PostUpdate, db: Session = Depends(get_db)):
#     post = db.query(PostModel).filter(PostModel.id == id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=_(f"NO POST FOUND WITH ID: {id}"))
#     post.title = request.title if request.title else post.title
#     post.content = request.content if request.content else post.content
#     db.commit()
#     return post


# @router.delete("/posts/{id}", response_class=TranslateJsonResponse, response_model=PostDisplay)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(PostModel).filter(PostModel.id == id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=_(f"NO POST FOUND WITH ID: {id}"))
#     db.delete(post)
#     db.commit()
#     return post


@router.post("/posts")
def create_post(request: PostCreate, db: Session = Depends(get_db)):
    post = PostModel(title=request.title, content=request.content)
    if not post:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
