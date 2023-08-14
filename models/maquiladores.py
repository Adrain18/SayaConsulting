# models/maquiladores.py
from .db import get_connection

mydb = get_connection()

class Maquilador:
    def __init__(self, name='', ape_mat='', ape_pat='', direction='', id_maquilador=''):
        self.name = name
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_maquilador = id_maquilador
    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO maquiladores (ape_mat, ape_pat, direction, name) VALUES (%s, %s, %s, %s)"
            values = (self.name, self.ape_mat, self.ape_pat, self.direction)
            cursor.execute(sql, values)
        mydb.commit()

    @staticmethod
    def get_all():
        maquiladores = []  # Declara la lista vacía antes del bucle
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_maquiladores"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                maquilador = Maquilador(
                    id_maquilador=row["ID de Maquilador"],
                    name=row["Nombre"],
                    ape_pat=row["Apellido_Paterno"],
                    ape_mat=row["Apellido Materno"],
                    direction=row["Direccion"]
                )
                maquilador.append(maquilador)  # Agrega el objeto user a la lista
        return maquiladores

    @staticmethod
    def get_all():
        maquiladores = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM maquiladores"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                maquilador = Maquilador(ape_mat=row["ape_mat"],
                                        ape_pat=row["ape_pat"],
                                        direction=row["direction"],
                                        id_maquilador=row["id_maquilador"],
                                        name=row["name"])
                maquiladores.append(maquilador)
        return maquiladores
