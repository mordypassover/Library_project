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
        conn = self.connector()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books"
        cursor.execute(query)
        all_books = cursor.fetchall()
        cursor.close()
        conn.close()
        return all_books

    def get_book_by_id(self, id):
        conn = self.connector()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books WHERE id = %s"
        cursor.execute(query, (id,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()

        if not book:
            raise ValueError("book id not valid")
        return book

    def update_book(self, id, data):
        data_key_to_list = []
        for i in data.keys():
            if i not in {"title", "author", "genre", "is_available", "id_member_by_borrowed"}:
                raise KeyError(f"data column {i} not supported")
            data_key_to_list.append(f"{i}=%s")

        keys_string = ", ".join(data_key_to_list)

        conn = self.connector()
        cursor = conn.cursor()
        query = f"UPDATE books SET {keys_string} WHERE id = %s"
        params = [data[val] for val in data.keys()]
        cursor.execute(query, params+ [id])
        is_success = cursor.rowcount > 0
        conn.commit()
        cursor.close()
        conn.close()
        return is_success


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
