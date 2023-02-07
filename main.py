from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "Departments" 
    ID : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Financing : Mapped[int] = mapped_column()
    Name : Mapped[str] = mapped_column()
    def __repr__(self) -> str:
        return f"Department(ID={self.ID!r}, Financing={self.Financing!r}, Name={self.Name!r})"
    
class Facultie(Base):
    __tablename__ = "Faculties" 
    ID : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Dean : Mapped[str] = mapped_column()
    Name : Mapped[str] = mapped_column()
    def __repr__(self) -> str:
        return f"Facultie(ID={self.ID!r}, Dean={self.Dean!r}, Name={self.Name!r})"

class Group(Base):
    __tablename__ = "Groups" 
    ID : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name : Mapped[str] = mapped_column()
    Rating : Mapped[int] = mapped_column()
    Year : Mapped[int] = mapped_column()
    def __repr__(self) -> str:
        return f"Group(ID={self.ID!r}, Name={self.Name!r}, Rating={self.Rating!r}, Year={self.Year!r})"
    
class Teacher(Base):
    __tablename__ = "Teachers" 
    ID : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    FirstName : Mapped[str] = mapped_column()
    LastName : Mapped[str] = mapped_column()
    EmploymentDate : Mapped[str] = mapped_column()
    IsAssistant : Mapped[int] = mapped_column()
    IsProfessor : Mapped[int] = mapped_column()
    Position : Mapped[str] = mapped_column()
    Premium : Mapped[int] = mapped_column()
    Salary : Mapped[int] = mapped_column()
    def __repr__(self) -> str:
        return f"Teacher(ID={self.ID!r}, FirstName={self.FirstName!r}, LastName={self.LastName!r}, EmploymentDate={self.EmploymentDate!r}, IsAssistant={self.IsAssistant!r}, IsProfessor={self.IsProfessor!r}, Position={self.Position!r}, Premium={self.Premium!r}, Salary={self.Salary!r})"

engine = create_engine("sqlite:///db.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    Student1 = Department(FirstName="Student1", LastName="1850", Rating=1)
    Student2 = Student(FirstName="Student2", LastName="1850", Rating=2)
    Student3 = Student(FirstName="Alexey", LastName="Lozovoy", Rating=3)
    Student4 = Student(FirstName="Student4", LastName="1850", Rating=4)
    Student5 = Student(FirstName="Student5", LastName="1850", Rating=5)
    Student6 = Student(FirstName="Student6", LastName="1850", Rating=6)
    Student7 = Student(FirstName="Student7", LastName="1850", Rating=7)

    session.add_all([Student1, Student2, Student3, Student4, Student5, Student6, Student7])
    session.commit()

    # Student3.Rating = Student3.Rating +2
    # session.commit()

    # SR = session.query(Student).filter(Student.Rating > Student3.Rating).all()
    # print(SR)

    # session.query(Student).filter(Student.Rating < 5).delete()
    # session.commit()
    


