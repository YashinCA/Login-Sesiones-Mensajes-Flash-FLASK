from settings import Config

# con esto puedo ocupar mi propia funcion llamada lg para hacer prints
# con esto me aseguro de no dejar prints por defecto


def lg(*cadena):
    if Config.DEBUG:
        print(*cadena)

# * para recibir argumentos multiples en el print
