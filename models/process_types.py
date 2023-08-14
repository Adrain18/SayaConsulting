# models/process_types.py
from .db import get_connection

mydb = get_connection()

class ProcessType:
    def __init__(self, id_process='', process=''):
        self.id_process = id_process
        self.process = process

    @staticmethod
    def get_all():
        process_types = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM process_types"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                process_type = ProcessType(id_process=row["id_process"], process=row["process"])
                process_types.append(process_type)
        return process_types
