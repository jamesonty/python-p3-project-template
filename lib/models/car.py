from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    number_plate = Column(String, nullable=False)
    time_of_arrival = Column(DateTime, nullable=False)
    expected_stay = Column(Integer, nullable=False)
    time_of_departure = Column(DateTime)

    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    owner = relationship('Owner', back_populates='cars')

    def __repr__(self):
        return (f"<Car(number_plate={self.number_plate}, time_of_arrival={self.time_of_arrival}, "
                f"expected_stay={self.expected_stay}, time_of_departure={self.time_of_departure})>")

    @classmethod
    def create(cls, session, number_plate, time_of_arrival, expected_stay, owner_id):
        car = cls(number_plate=number_plate, time_of_arrival=time_of_arrival, expected_stay=expected_stay, owner_id=owner_id)
        session.add(car)
        session.commit()
        return car

    @classmethod
    def delete(cls, session, car_id):
        car = session.query(cls).filter_by(id=car_id).first()
        if car:
            session.delete(car)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, car_id):
        return session.query(cls).filter_by(id=car_id).first()
