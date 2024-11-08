from AuthManager import AuthManager
from TaskManager import TaskManager
from Usuario import Usuario


# Función principal para el flujo de autenticación e inicio de sesión
def main():
    # Ajusta estos valores con tus credenciales de MySQL
    host = 'localhost'
    database = 'task_manager'
    user = 'root'
    password = 'Alejogsz19/'

    auth_manager = AuthManager(host, database, user, password)
    task_manager = TaskManager(host, database, user, password)

    print("Bienvenido al Sistema de Gestión de Tareas")

    while True:
        print("\n1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            user_id = auth_manager.login_user(username, password)
            if user_id:
                print("Inicio de sesión exitoso.")
                user = Usuario(user_id, username, task_manager)
                user.display_menu()
            else:
                print("Usuario o contraseña incorrectos.")
        elif choice == "2":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            auth_manager.register_user(username, password)
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()


