from datetime import datetime

from sqlalchemy import func, Text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from Eyes.api.config import get_db_url


DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
   pass

class BaseOrm(AsyncAttrs, Model):
    __tablename__ = "mails"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    domain: Mapped[str] = mapped_column(Text, nullable=False)
    protonmail: Mapped[str]
    mailru: Mapped[str]
    duolingo: Mapped[str]
    gravatar: Mapped[str]
    imgur: Mapped[str]
    bitmoji: Mapped[str]
    x: Mapped[str]
    github: Mapped[str]
    ig: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "domain": self.domain,
            "protonmail": self.protonmail,
            "name": self.name,
            "mailru": self.mailru,
            "duolingo": self.duolingo,
            "gravatar": self.gravatar,
            "imgur": self.imgur,
            "bitmoji": self.bitmoji,
            "x": self.x,
            "github": self.github,
            "ig": self.ig,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(BaseOrm.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(BaseOrm.metadata.drop_all)