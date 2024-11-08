import mysql.connector
from datetime import datetime, date
from typing import List, Optional

# Clase que representa una tarea individual
class Task:
    def __init__(self, title: str, description: str, creation_date: date, due_date: Optional[date] = None,
                 priority: str = "Media", status: str = "Pendiente", tags: Optional[List[str]] = None):
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.due_date = due_date
        self.priority = priority  # Puede ser Alta, Media o Baja
        self.status = status  # Pendiente o Completada
        self.tags = tags or []

    def __repr__(self):
        return f"Task({self.title}, Priority={self.priority}, Status={self.status})"




