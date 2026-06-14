
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

    def get_all_members(self):
        pass

    def get_member_by_id(self, id):
        pass

    def update_member(self):
        pass

    def deactivate_member(self, id):
        pass

    def activate_member(self, id):
        pass

    def increment_borrows(self, id):
        pass

    def count_active_members(self):
        pass

    def get_top_member(self):
        pass