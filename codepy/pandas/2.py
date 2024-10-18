import psycopg2
from psycopg2 import Binary

# 将文件保存到数据库中
def save_file_to_database(file):
    conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword")
    cursor = conn.cursor()
    # 处理文件读取并将其数据插入到数据库中
    with open(file, 'rb') as f:
        file_data = Binary(f.read())
        cursor.execute("INSERT INTO files (name, data) VALUES (%s, %s)", (file.name, file_data))
        conn.commit()
    cursor.close()
    conn.close()

def get_file_from_database(file_id):
    conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM files WHERE id = %s", (file_id,))
    file_data = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return file_data
