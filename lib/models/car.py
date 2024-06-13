from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    number_plate = Column(String, unique=True, nullable=False)
    time_of_arrival = Column(DateTime, nullable=False)
    expected_stay = Column(Integer, nullable=False)
    time_of_departure = Column(DateTime, nullable=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)

    owner = relationship('Owner', back_populates='cars')

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, car_id):
        return session.query(cls).filter_by(id=car_id).first()

    @classmethod
    def create(cls, session, number_plate, time_of_arrival, expected_stay, owner_id):
        car = cls(
            number_plate=number_plate,
            time_of_arrival=time_of_arrival,
            expected_stay=expected_stay,
            owner_id=owner_id
        )
        session.add(car)
        session.commit()
        session.refresh(car)
        return car

    def __repr__(self):
        return (f"<Car(number_plate={self.number_plate}, "
                f"time_of_arrival={self.time_of_arrival}, "
                f"expected_stay={self.expected_stay}, "
                f"time_of_departure={self.time_of_departure}, "
                f"owner_id={self.owner_id})>")
