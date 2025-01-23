from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projektas import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


"""Įsiterpkite įvairių įrašų, kad veiktų pagal visus filtrus skirtingai"""
#projektas1 = Projektas(name='kažkoks apleistas projektėlis', price=10000)
#session.add(projektas1)
#session.commit()

#projektas11 = session.query(Projektas).get(1)
#print(projektas11.id, 
#      projektas11.name, 
#      projektas11.price, 
#      projektas11.created_date)

#projektas2 = session.query(Projektas).filter_by(name='Ketvirtasis projektas').one()
#print(projektas2)


#projektai = session.query(Projektas).all()

#for projektas in projektai:
#    print(projektas)


#search = session.query(Projektas).filter(Projektas.name.ilike("2%"))
#search2 = session.query(Projektas).filter(Projektas.price>2000)
#search3 = session.query(Projektas).filter(Projektas.price>2000, Projektas.name.ilike("2%"))


#print([i for i in search3])