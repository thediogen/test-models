from typing import AsyncIterator, Annotated
import contextlib

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncConnection,
    AsyncSession,
    AsyncEngine
)
from fastapi import Depends


class DatabaseManager:
    '''
    This is PostgreSQL database manager. Here you can see different classes those are used in this project to `initialize`,
    `connect`, `close` database and get `database session`.
    '''

    def __init__(self):
        self._sessionmaker: async_sessionmaker | None = None
        self._engine: AsyncEngine | None = None


    def init(self, host: str, echo: bool = False):
        self._engine = create_async_engine(host, echo=echo)
        self._sessionmaker = async_sessionmaker(
            autocommit=False,
            expire_on_commit=False,
            bind=self._engine
        )


    async def close(self):
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None


    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise


    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        session = self._sessionmaker()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


pg_manager = DatabaseManager()


async def get_db_session():
    async with pg_manager.session() as session:
        yield session


Session_dp = Annotated[AsyncSession, Depends(get_db_session)]
