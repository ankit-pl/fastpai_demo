from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine(
    "postgresql://ankit:Ankitpal181@localhost/fast_api_project",
    encoding="latin1",
    echo=True
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
