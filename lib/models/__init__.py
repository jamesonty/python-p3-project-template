from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///parking_lot.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def initialize_db():
    from .car import Car
    from .owner import Owner
    Base.metadata.create_all(engine)
