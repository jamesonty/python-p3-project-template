# lib/initialize.py

from models import initialize_db

if __name__ == "__main__":
    initialize_db()
    print("Database initialized.")
