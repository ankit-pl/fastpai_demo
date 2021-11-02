from fastapi import FastAPI
from routes import router

app = FastAPI(title="Demo APIs")

app.include_router(router)
