from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# The URL pointing to our local database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

# The engine is the actual connection hub
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal creates temporary workspaces for our database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the blueprint factory that our models will inherit from
Base = declarative_base()