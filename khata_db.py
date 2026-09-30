import sqlite3
from datetime import datetime

DB_NAME = "expenses.db"  # We can share the same DB file or use a separate table

def init_khata_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS business_khata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL, -- 'Sale' or 'Expense'
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_khata_entry(title, category, entry_type, amount, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO business_khata (title, category, type, amount, date)
        VALUES (?, ?, ?, ?, ?)
    """, (title, category, entry_type, amount, date))
    conn.commit()
    conn.close()

def get_khata_entries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, category, type, amount, date FROM business_khata ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_khata_entry(entry_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM business_khata WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()