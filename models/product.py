# models/product.py
from .db import get_connection

mydb = get_connection()

class Product:
    def __init__(self, name_product='', id_material='', size='', price='', id_product=''):
        self.name_product = name_product
        self.id_material = id_material
        self.size = size
        self.price = price
        self.id_product = id_product

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO product (name_product, id_material, size, price) VALUES (%s, %s, %s, %s)"
            values = (self.name_product, self.id_material, self.size, self.price)
            cursor.execute(sql, values)
        mydb.commit()

    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_producto"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product = Product(
                    id_product=row["ID de Producto"],
                    id_material=row["ID de Material"],
                    name_product=row["Nombre de Producto"],
                    price=row["Precio"],
                    size=row["Talla"],
                )
                product.append(product)
        return products

    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM product"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product = Product(
                    id_product=row["id_product"],
                    id_material=row["id_material"],
                    name_product=row["name_product"],
                    price=row["price"],
                    size=row["size"]
                )
                products.append(product)
        return products   

class Material:
    def __init__(self, id_material='', name_material=''):
        self.id_material = id_material
        self.name_material = name_material

    @staticmethod
    def get_all():
        type_of_materials = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type_of_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                material = Material(
                    id_material=row["id_material"],
                    name_material=row["name_material"]
                )
                type_of_materials.append(material)
        return type_of_materials
