import users.connections as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]


class Note:

    def __init__(self, user_id, tittle = "", description = ""):
        self.user_id = user_id
        self.tittle = tittle
        self.description = description

    def save(self):
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        note = (self.user_id, self.tittle,self.description)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self]
    
    def get_ready(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND tittle LIKE '%{self.tittle}%' "
        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]

