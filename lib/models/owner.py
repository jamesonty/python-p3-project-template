from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    cars = relationship('Car', back_populates='owner', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f"<Owner(name={self.name})>"

    @classmethod
    def create(cls, session, name):
        owner = cls(name=name)
        session.add(owner)
        session.commit()
        return owner

    @classmethod
    def delete(cls, session, owner_id):
        owner = session.query(cls).filter_by(id=owner_id).first()
        if owner:
            session.delete(owner)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, owner_id):
        return session.query(cls).filter_by(id=owner_id).first()
