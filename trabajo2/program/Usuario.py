from datetime import datetime, date
from TaskManager import TaskManager
from Task import Task

class Usuario:
    def __init__(self, user_id: int, name: str, task_manager: TaskManager):
        self.user_id = user_id
        self.name = name
        self.task_manager = task_manager

    def display_menu(self):
        while True:
            print("\n--- Menú de Gestión de Tareas ---")
            print("1. Crear nueva tarea")
            print("2. Listar todas las tareas")
            print("3. Editar una tarea")
            print("4. Marcar tarea como completada")
            print("5. Eliminar una tarea")
            print("6. Salir")

            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.mark_task_completed()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def create_task(self):
        title = input("Título de la tarea: ")
        description = input("Descripción de la tarea: ")
        priority = input("Prioridad (Alta, Media, Baja): ")
        due_date_input = input("Fecha límite (YYYY-MM-DD) o deje vacío: ")
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date() if due_date_input else None
        tags_input = input("Etiquetas (separadas por comas): ")
        tags = tags_input.split(",") if tags_input else []

        task = Task(title=title, description=description, creation_date=date.today(),
                    due_date=due_date, priority=priority, tags=tags)
        self.task_manager.add_task(task, self.user_id)
        print("Tarea creada con éxito.")

    def list_tasks(self):
        tasks = self.task_manager.list_tasks(self.user_id)
        print("\n--- Lista de Tareas ---")
        for task in tasks:
            print(task)

    def edit_task(self):
        task_id = int(input("ID de la tarea a editar: "))
        title = input("Nuevo título (deje vacío para mantener actual): ")
        description = input("Nueva descripción (deje vacío para mantener actual): ")
        priority = input("Nueva prioridad (Alta, Media, Baja): ")
        due_date_input = input("Nueva fecha límite (YYYY-MM-DD) o deje vacío: ")
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date() if due_date_input else None

        self.task_manager.update_task(task_id, title=title, description=description,
                                      due_date=due_date, priority=priority)
        print("Tarea actualizada con éxito.")

    def mark_task_completed(self):
        task_id = int(input("ID de la tarea a marcar como completada: "))
        self.task_manager.update_task(task_id, status="Completada")
        print("Tarea marcada como completada.")

    def delete_task(self):
        task_id = int(input("ID de la tarea a eliminar: "))
        self.task_manager.delete_task(task_id)
        print("Tarea eliminada con éxito.")