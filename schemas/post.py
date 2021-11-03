from fastapi.param_functions import File
from pydantic import BaseModel, Field
from fastapi_localization import TranslatableStringField


class PostBase(BaseModel):
    title: str = Field(..., max_length=200)
    content: str = Field(None, max_length=1000)


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    title: str = Field(None, max_length=200)


class Post(BaseModel):
    title: TranslatableStringField
    content: TranslatableStringField
    date_posted: str = Field(None)

    class Config:
        orm_mode = True
