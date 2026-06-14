import mysql.connector


class DBConnection:
    def __init__(self):
        self.user = "root",
        self.password = "root1",
        self.database = "library_db",
        self.host = "LocalHost"
        self.create_books_and_members_tables()

    def get_connection_to_db(self):
        return mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host
        )


    def create_books_and_members_tables(self):
        conn = self.get_connection_to_db()
        cursor = conn.cursor()
        query = ("CREATE TABLE IF NOT EXISTS members ("
                 "id INT PRIMARY KEY AUTO_INCREMENT,"
                 "name VARCHAR(50) NOT NULL,"
                 "email VARCHAR(50) NOT NULL UNIQUE,"
                 "is_active BOOLEAN DEFAULT TRUE NOT NULL,"
                 "total_borrows INT DEFAULT 0 NOT NULL)",
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
