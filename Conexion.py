# Se instala la libreria psycopg2
from psycopg2 import pool
# Se importa clase logger_base
from logger_base import log

# Se crea clase conexion
class Conexion:
    _DATABASE = 'usuario'
    _USERNAME = 'admin'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

# Metodo para obtener pool
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
        else:
            return cls._pool

# Metodo para obtener conexion a nuestra pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion

# Metodo para liberar esa conexion que ya no esta en uso
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)

# Metodo para cerrar las conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

# Prueba para realizar una conexion a nuestra db
if __name__ == '__main__':
    conexion_prueba = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_prueba)


