from helpers import (
    exit_program,
    list_owners,
    find_owner_by_id,
    create_owner,
    delete_owner,
    list_cars,
    find_car_by_id,
    create_car,
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
            list_owners()
        elif choice == "2":
            find_owner_by_id()
        elif choice == "3":
            create_owner()
        elif choice == "4":
            delete_owner()
        elif choice == "5":
            list_cars()
        elif choice == "6":
            find_car_by_id()
        elif choice == "7":
            create_car()
        elif choice == "8":
            update_expected_stay()
        elif choice == "9":
            register_departure()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all owners")
    print("2. Find owner by ID")
    print("3. Create owner")
    print("4. Delete owner")
    print("5. List all cars")
    print("6. Find car by ID")
    print("7. Create car")
    print("8. Update expected stay for car")
    print("9. Register departure for car")

if __name__ == "__main__":
    main()
