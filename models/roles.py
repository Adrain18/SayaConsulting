# models/roles.py
from .db import get_connection

mydb = get_connection()

class Role:
    def __init__(self, id_role='', rol_name=''):
        self.id_role = id_role
        self.rol_name = rol_name

    @staticmethod
    def get_all():
        roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM roles"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                role = Role(id_role=row["id_role"], rol_name=row["rol_name"])
                roles.append(role)
        return roles
