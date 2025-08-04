import sqlite3

DB_NAME = 'mysql.db'

def init_db():
    # Kết nối đến SQLite database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Tạo bảng nếu chưa tồn tại
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Lưu thay đổi và đóng kết nối
    connection.commit()
    cursor.close()
    connection.close()

def get_user(email: str, password: str):
    # Kết nối đến SQLite database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Truy vấn người dùng theo email và mật khẩu
    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone() # fetchone: get the first result line after run SQL 

    # Đóng kết nối
    cursor.close()
    connection.close()

    return user


