from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

db_name = 'db_icar'

DATABASE_URL = "postgresql://postgres:Qwerty!23456@localhost:5432/db_icar"

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# engine = create_engine(f"mysql://{username}:{password}@{host}:{port}")

# with engine.connect() as conn:
#     # Do not substitute user-supplied database names here.
#     conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")