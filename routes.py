from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def say_hello_world():
    """
    Function to return hello world json object on call
    """
    return {"Hello": "World!"}
