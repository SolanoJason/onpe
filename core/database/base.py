from sqlalchemy import URL, create_engine, make_url, MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from core.settings import settings
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.sql.sqltypes import JSON

url = make_url(settings.DB.URI.unicode_string())

engine = create_async_engine(
    url,
    echo=True,
    echo_pool=True,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=15,
)

SessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)

metadata = MetaData()


class Base(AsyncAttrs, MappedAsDataclass, DeclarativeBase, kw_only=True):
    metadata = metadata

    type_annotation_map = {
        dict: JSON(none_as_null=True),  # Diccionarios como JSON
    }
