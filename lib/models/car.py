import sqlite3
from datetime import datetime

class Car:
    @classmethod
    def create(cls, number_plate, time_of_arrival, expected_stay, owner_id):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cars (number_plate, time_of_arrival, expected_stay, owner_id) VALUES (?, ?, ?, ?)', 
                       (number_plate, time_of_arrival, expected_stay, owner_id))
        conn.commit()
        car_id = cursor.lastrowid
        conn.close()
        return car_id

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cars')
        cars = cursor.fetchall()
        conn.close()
        return cars

    @classmethod
    def find_by_id(cls, car_id):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cars WHERE id = ?', (car_id,))
        car = cursor.fetchone()
        conn.close()
        return car

    @classmethod
    def find_by_owner_id(cls, owner_id):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cars WHERE owner_id = ?', (owner_id,))
        cars = cursor.fetchall()
        conn.close()
        return cars

    @classmethod
    def update_expected_stay(cls, car_id, new_expected_stay):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE cars SET expected_stay = ? WHERE id = ?', (new_expected_stay, car_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, car_id, conn=None):
        close_conn = False
        if conn is None:
            conn = sqlite3.connect('parking_lot.db')
            close_conn = True

        
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cars WHERE id = ?', (car_id,))
        conn.commit()

        if close_conn:
            conn.close()    

    @classmethod
    def register_departure(cls, car_id, time_of_departure):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE cars SET time_of_departure = ? WHERE id = ?', (time_of_departure, car_id))
        conn.commit()
        conn.close()
