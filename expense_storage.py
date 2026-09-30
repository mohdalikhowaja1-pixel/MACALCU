import sqlite3

DB_PATH = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_expense(title: str, amount: float, category: str, date_str: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (title, amount, category, date_str)
    )
    conn.commit()
    conn.close()

def get_all_expenses(filter_date: str = None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if filter_date and filter_date.strip():
        cursor.execute("SELECT id, title, amount, category, date FROM expenses WHERE date = ? ORDER BY id DESC", (filter_date.strip(),))
    else:
        cursor.execute("SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC, id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()