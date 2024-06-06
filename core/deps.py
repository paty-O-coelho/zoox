from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> AsyncGenerator[Any, None]:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()