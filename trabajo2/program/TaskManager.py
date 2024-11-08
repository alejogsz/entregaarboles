import mysql.connector
from datetime import date
from typing import List, Optional
from Task import Task

class TaskManager:
    def __init__(self, host: str, database: str, user: str, password: str):
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def add_task(self, task: Task, user_id: int):
        tags_str = ",".join(task.tags)
        query = """
        INSERT INTO tasks (title, description, creation_date, due_date, priority, status, tags, user_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (task.title, task.description, task.creation_date, task.due_date, task.priority, task.status, tags_str, user_id))
        self.connection.commit()

    def list_tasks(self, user_id: int) -> List[Task]:
        self.cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
        tasks_data = self.cursor.fetchall()
        tasks = []
        for data in tasks_data:
            tags = data[7].split(",") if data[7] else []
            task = Task(data[1], data[2], data[3], data[4], data[5], data[6], tags)
            tasks.append(task)
        return tasks

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    due_date: Optional[date] = None, priority: Optional[str] = None, status: Optional[str] = None):
        updates = []
        values = []

        if title:
            updates.append("title = %s")
            values.append(title)
        if description:
            updates.append("description = %s")
            values.append(description)
        if due_date:
            updates.append("due_date = %s")
            values.append(due_date)
        if priority:
            updates.append("priority = %s")
            values.append(priority)
        if status:
            updates.append("status = %s")
            values.append(status)

        if updates:
            query = "UPDATE tasks SET " + ", ".join(updates) + " WHERE id = %s"
            values.append(task_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()

    def delete_task(self, task_id: int):
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.connection.commit()

    def __del__(self):
        if self.connection:
            self.connection.close()