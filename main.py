from fastapi import FastAPI
from routes import router
from models import post
from db.session import db_engine

post.Base.metadata.create_all(bind=db_engine)

app = FastAPI(title="Demo APIs")

app.include_router(router)
