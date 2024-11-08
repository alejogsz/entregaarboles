import mysql.connector
from typing import Optional



class AuthManager:
    def __init__(self, host: str, database: str, user: str, password: str):
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def register_user(self, username: str, password: str):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            print("Usuario registrado con éxito.")
        except mysql.connector.IntegrityError:
            print("El nombre de usuario ya existe. Intente con otro.")

    def login_user(self, username: str, password: str) -> Optional[int]:
        self.cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def __del__(self):
        if self.connection:
            self.connection.close()