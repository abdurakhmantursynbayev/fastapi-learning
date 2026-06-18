from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import String, ForeignKey, create_engine
from typing import Optional
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key= True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    bio: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default= lambda: datetime.now(timezone.utc))

class Student(Base):

    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(50))

    courses: Mapped[list["Course"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )


class Course(Base):

    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))   

    student: Mapped["Student"] = relationship(
        back_populates="courses"
    ) 

engine = create_engine(
    "sqlite:///students.db",
    echo= True
)

Base.metadata.create_all(engine)

with Session(engine) as session:
    student1 = Student(name = "abdurakhman", courses = [Course(title="FastApi"), Course(title="SQLAlchemy")])

    student2 = Student(
        name= "Beksultan",
        courses = [Course(title="SE")]
    )

    session.add_all([student1, student2])
    session.commit()