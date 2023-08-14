from .entities.User import User
from conexionBD import * 

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                print(row)
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_all(self):
        try:
            conexion_MySQLdb = connectionBD()
            cursor           = conexion_MySQLdb.cursor(dictionary=True)
            sql = "SELECT * FROM user"
            
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close() #Cerrando conexion SQL
            conexion_MySQLdb.close() #cerrando conexion de la BD
            return result
        except Exception as ex:
            raise Exception(ex)
