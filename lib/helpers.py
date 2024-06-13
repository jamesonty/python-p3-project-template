from models.owner import Owner
from models.car import Car
import datetime

def exit_program():
    print("Goodbye!")
    exit()

def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)

def find_owner_by_id():
    owner_id = input("Enter the owner's id: ")
    owner = Owner.find_by_id(owner_id)
    print(owner) if owner else print(f'Owner with id {owner_id} not found')

def create_owner():
    name = input("Enter the owner's name: ")
    owner_id = Owner.create(name)
    print(f'Owner created with id: {owner_id}')

def delete_owner():
    owner_id = input("Enter the owner's id: ")
    Owner.delete(owner_id)
    print(f'Owner with id {owner_id} deleted')

def list_cars():
    cars = Car.get_all()
    for car in cars:
        print(car)

def find_car_by_id():
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(car_id)
    print(car) if car else print(f'Car with id {car_id} not found')

def create_car():
    number_plate = input("Enter the car's number plate: ")
    time_of_arrival = input("Enter the time of arrival (YYYY-MM-DD HH:MM:SS): ")
    expected_stay = input("Enter the expected stay duration in hours: ")
    owner_id = input("Enter the owner's id: ")
    try:
        time_of_arrival = datetime.datetime.strptime(time_of_arrival, '%Y-%m-%d %H:%M:%S')
        expected_stay = int(expected_stay)
        car_id = Car.create(number_plate, time_of_arrival, expected_stay, owner_id)
        print(f'Car created with id: {car_id}')
    except Exception as exc:
        print("Error adding car: ", exc)

def update_expected_stay():
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(car_id)
    if car:
        new_expected_stay = input("Enter the new expected stay duration in hours: ")
        try:
            new_expected_stay = int(new_expected_stay)
            Car.update_expected_stay(car_id, new_expected_stay)
            print(f'Expected stay updated for car with id: {car_id}')
        except Exception as exc:
            print("Error updating expected stay: ", exc)
    else:
        print(f'Car with id {car_id} not found')

def register_departure():
    car_id = input("Enter the car's id: ")
    car = Car.find_by_id(car_id)
    if car:
        time_of_departure = input("Enter the time of departure (YYYY-MM-DD HH:MM:SS): ")
        try:
            time_of_departure = datetime.datetime.strptime(time_of_departure, '%Y-%m-%d %H:%M:%S')
            Car.register_departure(car_id, time_of_departure)
            print(f'Departure registered for car with id: {car_id}')
        except Exception as exc:
            print("Error registering departure: ", exc)
    else:
        print(f'Car with id {car_id} not found')
