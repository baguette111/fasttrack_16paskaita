
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base #truputį pakitęs bibliotekos įkėlimas
import datetime

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()

class Projektas(Base):
    
    __tablename__ =  'Projektas'
    id = Column(Integer,primary_key=True)
    name = Column("Pavadinimas",String)
    price = Column("Kaina",Float)
    created_date = Column("Sukūrimo data", DateTime, default= datetime.datetime.today())
    ### kita datetime funkcija
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"
    
Base.metadata.create_all(engine)