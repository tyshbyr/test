from app.db.database import session


async def get_session():
    db = session()
    try:
        yield db
    finally:
        await db.close()
