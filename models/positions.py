# models/positions.py
from .db import get_connection

mydb = get_connection()

class Position:
    def __init__(self, name_position='', machinery_in_use='', id_position=''):
        self.name_position = name_position
        self.machinery_in_use = machinery_in_use
        self.id_position = id_position

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO positions (name_position, machinery_in_use) VALUES (%s, %s)"
            values = (self.name_position, self.machinery_in_use)
            cursor.execute(sql, values)
        mydb.commit()

    @staticmethod
    def get_all():
        positions = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_puestos"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                position = Position(
                    id_position=row["ID de Puesto"],
                    name_position=row["Nombre de Puesto"],
                    machinery_in_use=row["Maquinaria"],
                )
                positions.append(position)
        return positions
    @staticmethod
    def get_all():
        positions = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM positions"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                position = Position(id_position=row["id_position"],
                                    machinery_in_use=row["machinery_in_use"],
                                    name_position=row["name_position"])
                positions.append(position)
        return positions
