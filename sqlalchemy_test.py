from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
base = declarative_base()

class Person(base):
    __tablename__ = "people"
    ssn = Column("ssn",Integer,primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)

    def __init__(self,ssn,firstname,lastname,gender,age):
        self.ssn=ssn
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname}  ({self.gender},{self.age})"


engine = create_engine("sqlite:///mydb.db",echo=True)
base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
for i in range(8):
    random_number = random.randrange(10000)
    age = random.randrange(100)
    j = random.randrange(1)
    k = random.randrange(5)
    m = random.randrange(5)
    fnam =["James","John","Jake","Josh","Jerry",] 
    lnam =["Smith","Allen","McAllister","Chester","Bellingham",]
    gndr=["M","F"]
    p=Person(random_number,fnam(k),lnam(m),gndr(j),age)
    session.add(p)
    session.commit()

results = session.query(Person).all()
