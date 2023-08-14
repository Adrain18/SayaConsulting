# models/entrance_materials.py
from .db import get_connection

mydb = get_connection()

class EntranceMaterial:
    def __init__(self, date_of_entry='', id_material='', id_supplier='', metres=''):
        self.date_of_entry = date_of_entry
        self.id_material = id_material
        self.id_supplier = id_supplier
        self.metres = metres

    @staticmethod
    def get_all():
        entrance_materials = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM entrance_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                entrance_material = EntranceMaterial(date_of_entry=row["date_of_entry"],
                                                     id_material=row["id_material"],
                                                     id_supplier=row["id_supplier"],
                                                     metres=row["metres"])
                entrance_materials.append(entrance_material)
        return entrance_materials