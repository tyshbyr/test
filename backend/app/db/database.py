from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config.project_config import app_config


SQLALCHEMY_DATABASE_URL = app_config.sqlalchemy_database_url

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

session = async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)
