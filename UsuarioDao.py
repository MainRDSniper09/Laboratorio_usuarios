# Se importa clase CursorDelPool
from CursorDelPool import CursorDelPool
# Se importa clase logger
from logger_base import log
# Se importa clase usuario
from Usuario import Usuario

class UsuarioDao:

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    # Creacion metodo seleccionar
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    #Creacion de metodo insertar
    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            log.info(
                f'Usuario a insertar {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.info(
                f'Usuario insertado correctamente: {usuario}')
            return cursor.rowcount

    # Creacion de metodo actualizar
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, usuario.username, usuario.password)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.info(f'Usuario actualizada correctamente: {usuario}')
            return cursor.rowcount

    # Creacion del metodo eliminar
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.info(f'Usuario eliminado correctamente {usuario}')
            return cursor.rowcount

# Prueba de nuestra clase
if __name__ == '__main__':
    usuarios = UsuarioDao.seleccionar()
    for usuario in usuarios:
        log.info(usuario)
