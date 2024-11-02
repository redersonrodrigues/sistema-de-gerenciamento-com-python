import sqlite3

class Database():
    def __init__(self, name="system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                access TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_paciente TEXT NOT NULL,
                data_nascimento TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS setores(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_setor TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS especialidades(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_especialidade TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assistentes_sociais(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_assistente TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atendimentos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                data_atendimento TEXT NOT NULL,
                especialidade_id INTEGER NOT NULL,
                descricao_atendimento TEXT NOT NULL,
                desfecho_atendimento TEXT NOT NULL,
                assistente_social_id INTEGER NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                FOREIGN KEY (especialidade_id) REFERENCES especialidades(id),
                FOREIGN KEY (assistente_social_id) REFERENCES assistentes_sociais(id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atendimentos_especialidades(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                atendimento_id INTEGER NOT NULL,
                especialidade_id INTEGER NOT NULL,
                FOREIGN KEY (atendimento_id) REFERENCES atendimentos(id),
                FOREIGN KEY (especialidade_id) REFERENCES especialidades(id)
            );
        """)

    def insert_user(self, name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users(name, user, password, access) VALUES (?, ?, ?, ?);
            """, (name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_user(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)
            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3].upper() == password.upper() and linha[4].upper() == "ADMINISTRADOR":
                    return "Administrador"
                elif linha[2].upper() == user.upper() and linha[3].upper() == password.upper() and linha[4].upper() == "USUÁRIO":
                    return "Usuário"
                else:
                    continue
            return "Sem acesso."
        except AttributeError:
            print("faça a conexão")
