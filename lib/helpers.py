from lib.models.car import Car
from lib.models.owner import Owner
from lib.database import SessionLocal
import datetime

def exit_program():
    print("Goodbye!")
    exit()

def list_owners():
    session = SessionLocal()
    owners = Owner.get_all(session)
    for owner in owners:
        print(owner)
    session.close()

def find_owner_by_id():
    session = SessionLocal()
    owner_id = input("Enter the owner's id: ")
    owner = Owner.find_by_id(session, owner_id)
    print(owner) if owner else print(f'Owner with id {owner_id} not found')
    session.close()

def create_owner():
    session = SessionLocal()
    name = input("Enter the owner's name: ")
    owner = Owner.create(session, name)
    print(f'Success: {owner}')
    session.close()

def delete_owner():
    session = SessionLocal()
    owner_id = input("Enter the owner's id: ")
    Owner.delete(session, owner_id)
    print(f'Owner with id {owner_id} deleted')
    session.close()

def list_cars():
    session = SessionLocal()
    cars = Car.get_all(session)
    for car in cars:
        print(car)
    session.close()

def find_car_by_id():
    session = SessionLocal()
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(session, car_id)
    print(car) if car else print(f'Car with id {car_id} not found')
    session.close()

def create_car():
    session = SessionLocal()
    number_plate = input("Enter the car's number plate: ")
    time_of_arrival = input("Enter the time of arrival (YYYY-MM-DD HH:MM:SS): ")
    expected_stay = input("Enter the expected stay duration in hours: ")
    owner_id = input("Enter the owner's id: ")
    try:
        time_of_arrival = datetime.datetime.strptime(time_of_arrival, '%Y-%m-%d %H:%M:%S')
        expected_stay = int(expected_stay)
        car = Car.create(session, number_plate, time_of_arrival, expected_stay, owner_id)
        print(f'Success: {car}')
    except Exception as exc:
        print("Error adding car: ", exc)
    session.close()

def update_expected_stay():
    session = SessionLocal()
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(session, car_id)
    if car:
        new_expected_stay = input("Enter the new expected stay duration in hours: ")
        try:
            new_expected_stay = int(new_expected_stay)
            car.expected_stay = new_expected_stay
            session.commit()
            print(f'Success: {car}')
        except Exception as exc:
            print("Error updating expected stay: ", exc)
    else:
        print(f'Car with id {car_id} not found')
    session.close()

def register_departure():
    session = SessionLocal()
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(session, car_id)
    if car:
        time_of_departure = input("Enter the time of departure (YYYY-MM-DD HH:MM:SS): ")
        try:
            time_of_departure = datetime.datetime.strptime(time_of_departure, '%Y-%m-%d %H:%M:%S')
            car.time_of_departure = time_of_departure
            session.commit()
            print(f'Success: {car}')
        except Exception as exc:
            print("Error registering departure: ", exc)
    else:
        print(f'Car with id {car_id} not found')
    session.close()
