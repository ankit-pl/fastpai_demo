from fastapi import APIRouter
from fastapi.params import Depends
from schemas.post import PostCreate, PostUpdate
from sqlalchemy.orm import Session
from models.post import Post as PostModel
from db.session import session_local

router = APIRouter()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def display_all_posts(db: Session = Depends(get_db)):
    posts = db.query(PostModel).all()
    return posts


@router.post("/posts")
def create_post(request: PostCreate, db: Session = Depends(get_db)):
    post = PostModel(title=request.title, content=request.content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("/posts/{id}")
def read_post(id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == id).first()
    return post


@router.put("/posts/{id}")
def update_post(id: int, request: PostUpdate, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == id).first()
    post.title = request.title if request.title else post.title
    post.content = request.content if request.content else post.content
    db.commit()
    return post


@router.delete("/posts/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == id).first()
    db.delete(post)
    db.commit()
    return post
