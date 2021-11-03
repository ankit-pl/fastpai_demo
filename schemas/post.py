from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    title: Optional[str] = None


class Post(PostBase):
    date_posted: str

    class config:
        orm_mode = True
