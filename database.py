import sqlite3


class Database:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );
            """
            )
        except AttributeError:
            print("faça a conexão")

    def insert_user(self, name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO users(name, user, password, access) VALUES (?, ?, ?, ?);
            """,
                (name, user, password, access),
            )
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_user(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    SELECT * FROM users;
                """
            )
            for linha in cursor.fetchall():
                if (
                    linha[2].upper() == user.upper()
                    and linha[3].upper() == password.upper()
                    and linha[4].upper() == "ADMINISTRADOR"
                ):
                    return "Administrador"
                elif (
                    linha[2].upper() == user.upper()
                    and linha[3].upper() == password.upper()
                    and linha[4].upper() == "USUÁRIO"
                ):
                    return "user"
            return None  # Melhor usar None para login inválido
        except:
            pass


if __name__ == "__main__":
    db = Database()
    db.conecta()
    db.create_table_users()
