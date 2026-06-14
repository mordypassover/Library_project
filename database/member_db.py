
class MemberDBManager:
    def __init__(self):
        pass

    def create_member(self, data, conn):
        if not ("name" in data and "email" in data):
            raise KeyError("input not valid")
        cursor =conn.cursor()
        query = "INSERT INTO members(name, email) VALUES (%s, %s)"
        cursor.execute(query,(data["name"], data["email"]))
        new_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        return new_id

    def get_all_members(self, conn):
        cursor = conn.cursor()
        query = "SELECT * FROM members"
        cursor.execute(query)
        all_members = cursor.fetchall()
        cursor.close()
        return all_members

    def get_member_by_id(self, id, conn):
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM members WHERE id = %s"
        cursor.execute(query, (id,))
        member = cursor.fetchone()
        cursor.close()
        if not member:
            raise ValueError(f"member id-{id} not valid")


        return member

    def update_member(self, conn):
        pass

    def deactivate_member(self, id, conn):
        pass

    def activate_member(self, id, conn):
        pass

    def increment_borrows(self, id, conn):
        pass

    def count_active_members(self, conn):
        pass

    def get_top_member(self, conn):
        pass