# Importamos la clase conexion
from Conexion import Conexion
# Importamos clase looger_base
from logger_base import log

# Creacion clase Cursor del pool para realizar las querys
class CursorDelPool:
    # Creacion de atributos conn y cursor
    def __init__(self):
        self._conn = None
        self._cursor = None

    # Creacion metodo enter
    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor

    # Creacion funcion exit
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conn.rollback()
            log.error(
                f'Ocurrio un error, realizando rollback: {exc_val} {exc_type} {exc_tb}'
            )
        else:
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conn)

# Prueba para realizar una consulta en nuestra tabla
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM usuario')
        log.info(cursor.fetchall())

