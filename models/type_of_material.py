# models/type_of_material.py
from .db import get_connection

mydb = get_connection()

class TypeOfMaterial:
    def __init__(self, name_material='', price='', id_material=''):
        self.name_material = name_material
        self.price = price
        self.id_material = id_material
    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO type_of_material (name_material, price) VALUES (%s, %s)"
            values = (self.name_material, self.price)
            cursor.execute(sql, values) 
        mydb.commit()

    @staticmethod
    def get_all():
        types_of_material = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                type_of_material = TypeOfMaterial(
                    id_material=row["ID de Material"],
                    name_material=row["Nombre de Material"],
                    price=row["Precio"],
                )
                type_of_material.append(type_of_material)
        return types_of_material

    @staticmethod
    def get_all():
        types_of_material = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type_of_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                type_of_material = TypeOfMaterial(id_material=row["id_material"],
                                                  name_material=row["name_material"],
                                                  price=row["price"])
                types_of_material.append(type_of_material)
        return types_of_material
