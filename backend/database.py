from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

# create engine and session 
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)