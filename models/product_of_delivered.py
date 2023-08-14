# models/product_to_delivered.py
from .db import get_connection

mydb = get_connection()

class ProductToDelivered:
    def __init__(self, delivery_code='', entry_date='', id_maquilador='', id_maquilero='', id_product=''):
        self.delivery_code = delivery_code
        self.entry_date = entry_date
        self.id_maquilador = id_maquilador
        self.id_maquilero = id_maquilero
        self.id_product = id_product

    @staticmethod
    def get_all():
        product_to_delivereds = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM product_to_delivered"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product_to_delivered = ProductToDelivered(delivery_code=row["delivery_code"],
                                                          entry_date=row["entry_date"],
                                                          id_maquilador=row["id_maquilador"],
                                                          id_maquilero=row["id_maquilero"],
                                                          id_product=row["id_product"])
                product_to_delivereds.append(product_to_delivered)
        return product_to_delivereds
