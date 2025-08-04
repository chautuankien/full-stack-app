import mysql.connector

# Kết nối đến MySQL server (chưa cần chỉ định database)
connection = mysql.connector.connect(
    host="localhost",       # hoặc IP MySQL server
    user="root",            # username của MySQL
    password="your_password"  # thay bằng mật khẩu thật
)

cursor = connection.cursor()

# Tạo database mới
cursor.execute("CREATE DATABASE mydatabase")

# Đóng kết nối
cursor.close()
connection.close()