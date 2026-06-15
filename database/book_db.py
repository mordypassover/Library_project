class BooksDBManager:
    GENRE_TYPES = ('fiction', 'non-fiction', 'science', 'history', 'other')
    def __init__(self):
        pass

    def create_book(self,title, author, genre, conn):
        cursor = conn.cursor()
        query = "INSERT INTO books(title, author, genre) VALUES (%s,%s, %s)"
        cursor.execute(query, (title, author, genre))
        new_book = cursor.lastrowid
        conn.commit()
        cursor.close()
        return new_book


    def get_all_books(self, conn):
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books"
        cursor.execute(query)
        all_books = cursor.fetchall()
        cursor.close()
        return all_books

    def get_book_by_id(self, id, conn):
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books WHERE id = %s"
        cursor.execute(query, (id,))
        book = cursor.fetchone()
        cursor.close()

        if not book:
            raise ValueError("book id not valid")
        return book

    def update_book(self, id, data, conn):
        data_key_to_list = []
        for i in data.keys():
            if i not in {"title", "author", "genre", "is_available", "id_member_by_borrowed"}:
                raise KeyError(f"data column {i} not supported")
            data_key_to_list.append(f"{i}=%s")

        keys_string = ", ".join(data_key_to_list)

        cursor = conn.cursor()
        query = f"UPDATE books SET {keys_string} WHERE id = %s"
        params = [data[val] for val in data.keys()]
        cursor.execute(query, params+ [id])
        is_success = cursor.rowcount > 0
        conn.commit()
        cursor.close()
        return is_success

    def set_available(self, id, val, member_id, conn):
        book = self.get_book_by_id(id, conn)
        borrowed_books =  self.count_borrowed_books(member_id, conn)
        if (not val) and book["is_available"] and borrowed_books:
            return self.update_book(id,{"is_available":val, "id_member_by_borrowed":member_id}, conn)
        elif val and book["id_member_by_borrowed"] == member_id:
            return self.update_book(id, {"is_available":val, "id_member_by_borrowed":None}, conn)
        else:
            raise ValueError("unable to change data do to one or more data errors")

    def books_total_count(self):
        pass

    def count_available_books(self):
        pass

    def count_borrowed_books(self, member_id, conn):
        cursor = conn.cursor()
        query = "SELECT COUNT(id_member_by_borrowed) books WHERE id_member_by_borrowed = %s"
        cursor.execute(query, (member_id,))
        books_borrowed = cursor.fetchone
        cursor.close()
        return books_borrowed

    def count_by_genre(self, genre):
        pass

    def count_active_borrows_by_member(self, member_id):
        pass