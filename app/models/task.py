from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id:Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

