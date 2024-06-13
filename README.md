# Parking Lot Management App

## By: James Mwangi


## Introduction
  -Enjoy use of tech disposable at ur fingertips
  -You can manage,track,delete, and update the cars that set foot to ur compound



## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` :

# lib/cli.py

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

from models.database import initialize_db

def main():
    initialize_db()  # Ensure the database is initialized
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

```

You can run the template CLI with `python3 lib/cli.py`,or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.




## Resources

- [Markdown Cheat Sheet](https://chatgpt.com/)
