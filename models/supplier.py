# models/supplier.py
from .db import get_connection

mydb = get_connection()

class Supplier:
    def __init__(self, name='',ape_mat='', ape_pat='', direction='', id_material='', id_supplier=''):
        self.name = name
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_material = id_material
        self.id_supplier = id_supplier
    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO supplier (ape_mat, ape_pat, direction, id_material, name) VALUES (%s, %s, %s, %s, %s)"
            values = ( self.name, self.ape_mat, self.ape_pat, self.direction, self.id_material)
            cursor.execute(sql, values)
        mydb.commit()
    
    @staticmethod
    def get_all():
        suppliers = []  # Declara la lista vacía antes del bucle
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_supplier"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                supplier = Supplier(
                    id_supplier=row["ID de Proveedor"],
                    name=row["Nombre"],
                    ape_pat=row["Apellido_Paterno"],
                    ape_mat=row["Apellido materno"],
                    direction=row["Direccion"],
                    id_material=row["ID de Material"]
                )
                supplier.append(supplier)  # Agrega el objeto user a la lista
        return suppliers

    @staticmethod
    def get_all():
        suppliers = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM supplier"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                supplier = Supplier(ape_mat=row["ape_mat"],
                                    ape_pat=row["ape_pat"],
                                    direction=row["direction"],
                                    id_material=row["id_material"],
                                    id_supplier=row["id_supplier"],
                                    name=row["name"])
                suppliers.append(supplier)
        return suppliers

class Material:
    def __init__(self, id_material='', name_material=''):
        self.id_material = id_material
        self.name_material = name_material

    @staticmethod
    def get_all():
        type_of_materials = []  # Crear una lista vacía para almacenar los materiales
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type_of_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                material = Material(id_material=row["id_material"], name_material=row["name_material"])
                type_of_materials.append(material)  # Agregar cada material a la lista
        return type_of_materials
