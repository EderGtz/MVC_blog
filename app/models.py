import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "blogDatabase.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    #Create tables of users and blogs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blogs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT,
        body_text TEXT
        )
    ''')

    #Create admin if not exists

    cursor.execute('SELECT 1 FROM users WHERE username = ?',('EderGTZ',))
    if not cursor.fetchone():
        cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?,?)',
        ('Avatarnight25', generate_password_hash('Aceitunita')))

    conn.commit()
    conn.close()

#CRUD

def get_all_blogs():
    conn = get_db()
    cursor = conn.cursor()
    blogs = cursor.execute('SELECT * FROM blogs ORDER BY id DESC').fetchall()
    conn.close()
    return blogs

def get_user_by_username(username):
    conn = get_db()
    cursor = conn.cursor()
    user = cursor.execute("SELECT * FROM users WHERE username = ?",(username,)).fetchone()
    conn.close()
    return user

def create_blog_entry(title, date, body):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO blogs (title, date, body_text) VALUES (?,?,?)", (title, date, body))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()