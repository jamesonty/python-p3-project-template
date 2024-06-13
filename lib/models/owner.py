import sqlite3

class Owner:
    @classmethod
    def create(cls, name):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO owners (name) VALUES (?)', (name,))
        conn.commit()
        owner_id = cursor.lastrowid
        conn.close()
        return owner_id

    @classmethod
    def delete(cls, owner_id):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM owners WHERE id = ?', (owner_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM owners')
        owners = cursor.fetchall()
        conn.close()
        return owners

    @classmethod
    def find_by_id(cls, owner_id):
        conn = sqlite3.connect('parking_lot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM owners WHERE id = ?', (owner_id,))
        owner = cursor.fetchone()
        conn.close()
        return owner
