import mysql.connector


def get_connection_to_db():
    return mysql.connector.connect(
        user="root",
        password="root1",
        database="library_db",
        host="LocalHost"
    )


def create_books_and_members_tables():
    conn = get_connection_to_db()
    cursor = conn.cursor()
    query = ("CREATE TABLE IF NOT EXISTS members ("
             "id INT PRIMARY KEY AUTO_INCREMENT,"
             "name VARCHAR(50) NOT NULL,"
             "email VARCHAR(50) NOT NULL UNIQUE,"
             "is_active BOOLEAN DEFAULT TRUE NOT NULL,"
             "total_borrows INT NOT NULL)",
             "CREATE TABLE IF NOT EXISTS books ("
             "id INT PRIMARY KEY AUTO_INCREMENT,"
             "title VARCHAR(50) NOT NULL,"
             "author VARCHAR(50) NOT NULL,"
             "genre  ENUM('fiction', 'non-fiction', 'science', 'history', 'other') NOT NULL,"
             "is_available BOOLEAN DEFAULT TRUE NOT NULL,"
             "id_member_by_borrowed INT NULL)")
    for i in query:
        cursor.execute(i)
        conn.commit()
    cursor.close()
    conn.close()

create_books_and_members_tables()
