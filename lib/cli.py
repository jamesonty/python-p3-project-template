# lib/cli.py

from helpers import (
    exit_program,
    list_cars,
    find_car_by_number_plate,
    add_car,
    update_expected_stay,
    register_departure,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_cars()
        elif choice == "2":
            find_car_by_number_plate()
        elif choice == "3":
            add_car()
        elif choice == "4":
            update_expected_stay()
        elif choice == "5":
            register_departure()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all cars")
    print("2. Find car by number plate")
    print("3. Add car")
    print("4. Update expected stay")
    print("5. Register departure")

if __name__ == "__main__":
    main()
