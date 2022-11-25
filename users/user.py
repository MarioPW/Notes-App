import datetime
import hashlib
import users.connections as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]


class User:

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def regiser(self):
        # Current date
        date = datetime.datetime.now()
        
        # encrypted password
        encrypted_password = hashlib.sha256()
        encrypted_password.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, encrypted_password.hexdigest(), date)
        try:
            cursor.execute(sql, user)
            database.commit()
            result =  [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def login_data (self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # encrypted password
        encrypted_password = hashlib.sha256()
        encrypted_password.update(self.password.encode('utf8'))
        
        # Data for consultation
        user = (self.email, encrypted_password.hexdigest())
        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
