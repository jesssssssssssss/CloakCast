import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="cloakcast.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize the database and create the contacts table if it doesn't exist"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def save_contact(self, name, email, message):
        """Save a new contact form submission to the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contacts (name, email, message)
                VALUES (?, ?, ?)
            ''', (name, email, message))
            conn.commit()
            return cursor.lastrowid
        
    