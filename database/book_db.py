from database.db_connection import get_connection_to_db


class BooksDBManager:
    GENRE_TYPES = ('fiction', 'non-fiction', 'science', 'history', 'other')
    def __init__(self):
        self.connector = get_connection_to_db


    def create_book(self,title, author, genre):
        conn =self.connector()
        cursor = conn.cursor()
        query = "INSERT INTO books(title, author, genre) VALUES (%s,%s, %s)"
        cursor.execute(query, (title, author, genre))
        new_book = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return new_book


    def get_all_books(self):
        pass

    def get_book_by_id(self, id):
        pass

    def update_book(self, id, data):
        pass

    def set_available(self, id, val, member_id):
        pass

    def books_total_count(self):
        pass

    def count_available_books(self):
        pass

    def count_borrowed_books(self):
        pass

    def count_by_genre(self, genre):
        pass

    def count_active_borrows_by_member(self, member_id):
        pass
