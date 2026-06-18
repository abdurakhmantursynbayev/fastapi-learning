from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class Author(Base):

    id: Mapped[int] = mapped_column(primary_key= True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    bio: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))

class Student(Base):
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(50))


class Courses(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    student_id: Mapped[int] = mapped_column(ForeignKey(Student.id))    