# Importamos la clase UsuarioDao
from UsuarioDao import UsuarioDao
# Se importa clase logger
from logger_base import log
# Se importa clase Usuario
from Usuario import Usuario

print('Bienvenido a nuestra aplicacion'.center(50,'+'))
while True:
    print('''
    Ingrese alguna de las opciones disponibles:
    1. Listar todos los usuarios existentes
    2. Insertar un usuario nuevo
    3. Actualizar un usuario
    4. Eliminar un usuario
    5. Salir del programa
    ''')
    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    if opcion == 2:
        username = input('Ingrese el usuario: ')
        password = input('Ingrese la contraseña: ')
        usuario = Usuario(username=username, password=password)
        registros_insertados = UsuarioDao.insertar(usuario)

        log.info(f'Usuarios insertados: {usuario}')

    if opcion == 3:
        id_usuario = int(input('Ingrese el id del usuario que quiera modificar: '))
        username = input('Ingrese el usuario: ')
        password = input('Ingrese la contraseña: ')
        usuario = Usuario(id_usuario=id_usuario,username=username,password=password)
        registros_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios Actualizados: {registros_actualizados}')

    if opcion == 4:
       id_usuario = int(input('Ingrese el id del usuario: '))
       usuario = Usuario(id_usuario = id_usuario)
       registros_eliminados = UsuarioDao.eliminar(usuario)
       log.info(f'Usuarios eliminados: {registros_eliminados}')

    if opcion == 5:
        print('saliendo del programa..')
        exit()




