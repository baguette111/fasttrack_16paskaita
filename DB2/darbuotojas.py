
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base
import datetime

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()


class Darbuotojas(Base):
    __tablename__ =  'Darbuotojas'
    id = Column(Integer,primary_key=True)
    name = Column("Vardas",String)
    surname = Column("Pavardė",String)
    position = Column("Pareigos",String)
    salary = Column("Atlyginimas",Float)
    start_date = Column("Sukūrimo data", DateTime, default= datetime.datetime.today())
    
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
    
        
    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname}, {self.position} - {self.salary} {self.start_date}"
    
Base.metadata.create_all(engine)