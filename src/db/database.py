from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from core.database import get_settings

settings = get_settings()


engine = create_async_engine(
    settings.postgres.url,
    pool_size=settings.postgres.pool_size,
    max_overflow=settings.postgres.max_overflow,
    pool_timeout=settings.postgres.pool_timeout,
    pool_recycle=settings.postgres.pool_recycle,
    pool_pre_ping=settings.postgres.pool_pre_ping,
)

async_session = async_sessionmaker(
    bind=engine,
    autocommit=settings.async_sessionmaker.autocommit,
    autoflush=settings.async_sessionmaker.autoflush,
    expire_on_commit=settings.async_sessionmaker.expire_on_commit,
    class_=AsyncSession,
)

Base = declarative_base()
