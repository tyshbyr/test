from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import users as models
from app.schemas import users as schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db: AsyncSession, user_id: int):
    return await db.execute(select(models.User).where(models.User.id == user_id))


async def get_user_by_email(db: AsyncSession, email: str):
    user = await db.execute(select(models.User).where(models.User.email == email))
    return user.scalars().first()
