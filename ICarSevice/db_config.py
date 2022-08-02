import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_ADRESS = os.environ.get("DB_ADRESS")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADRESS}/{DB_NAME}"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# engine = create_engine(f"mysql://{username}:{password}@{host}:{port}")

# with engine.connect() as conn:
#     # Do not substitute user-supplied database names here.
#     conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")