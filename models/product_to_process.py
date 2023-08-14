# models/product_to_process.py
from .db import get_connection

mydb = get_connection()

class ProductToProcess:
    def __init__(self, entry_date='', estimated_delivery_date='', id_maquilador='', id_process='', id_product='', id_user='', process_code=''):
        self.entry_date = entry_date
        self.estimated_delivery_date = estimated_delivery_date
        self.id_maquilador = id_maquilador
        self.id_process = id_process
        self.id_product = id_product
        self.id_user = id_user
        self.process_code = process_code

    @staticmethod
    def get_all():
        product_to_processes = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM product_to_process"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product_to_process = ProductToProcess(entry_date=row["entry_date"],
                                                      estimated_delivery_date=row["estimated_delivery_date"],
                                                      id_maquilador=row["id_maquilador"],
                                                      id_process=row["id_process"],
                                                      id_product=row["id_product"],
                                                      id_user=row["id_user"],
                                                      process_code=row["process_code"])
                product_to_processes.append(product_to_process)
        return product_to_processes
