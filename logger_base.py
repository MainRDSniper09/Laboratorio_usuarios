import logging as log

# Configuracion handler
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers= [
                    log.FileHandler('registro_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Prueba debug')
