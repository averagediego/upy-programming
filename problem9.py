# Problema 9: Sistema de autenticación

# Credenciales guardadas en el sistema
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

# Lectura de datos del usuario
usuario_ingresado = input("Introduce el usuario: ")

# Primero verificamos el usuario
if usuario_ingresado == USUARIO_CORRECTO:
    # Si el usuario es correcto, pasamos a pedir y verificar la contraseña
    contrasena_ingresada = input("Introduce la contraseña: ")
    
    if contrasena_ingresada == CONTRASENA_CORRECTA:
        print("Bienvenido")
    else:
        print("Contrasena incorrecta")
else:
    # Si el usuario desde el principio no coincide
    print("Usuario desconocido")