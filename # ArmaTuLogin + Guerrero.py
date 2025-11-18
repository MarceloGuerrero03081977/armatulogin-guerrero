#   ArmaTuLogin + Guerrero
#   Sistema de registro, login y listado
# ============================================

# Base de datos de usuarios (diccionario)
usuarios = {}


# --------------------------------------------
# Función para registrar un usuario nuevo
# --------------------------------------------
def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    # Verificar si ya existe
    if usuario in usuarios:
        print("❌ El usuario ya existe. Intente con otro.")
        return

    # Guardar el usuario
    usuarios[usuario] = contraseña
    print("✅ Usuario registrado con éxito.")


# --------------------------------------------
# Función para mostrar los usuarios registrados
# --------------------------------------------
def mostrar_usuarios():
    print("\n=== USUARIOS REGISTRADOS ===")
    
    if not usuarios:
        print("No hay usuarios cargados.")
        return

    for user in usuarios:
        print(f"- {user}")


# --------------------------------------------
# Función para loguear un usuario
# --------------------------------------------
def login():
    print("\n=== LOGIN ===")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verificar usuario
    if usuario not in usuarios:
        print("❌ El usuario no existe.")
        return

    # Verificar contraseña
    if usuarios[usuario] == contraseña:
        print("✅ Login exitoso. ¡Bienvenido!")
    else:
        print("❌ Contraseña incorrecta.")


# --------------------------------------------
# Menú principal
# --------------------------------------------
def menu():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Registrar usuario")
        print("2. Login")
        print("3. Mostrar usuarios")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("👋 Saliendo del programa…")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")


# Ejecutar el programa
menu()