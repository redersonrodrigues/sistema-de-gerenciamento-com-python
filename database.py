import sqlite3


class Database:
    def __init__(self, name="system.db") -> None:
        self.name = name
        self.connection = None

    def conecta(self):
        """Estabelece a conexão com o banco de dados."""
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()

    def create_table_users(self):
        """Cria a tabela de usuários, se não existir."""
        if not self.connection:
            print("faça a conexão")
            return
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

    def insert_user(self, name, user, password, access):
        """Insere um novo usuário na tabela."""
        if not self.connection:
            print("faça a conexão")
            return
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO users(name, user, password, access) VALUES (?, ?, ?, ?);
            """,
            (name, user, password, access),
        )
        self.connection.commit()

    def check_user(self, user, password):
        """Verifica se o usuário e senha correspondem a um usuário existente."""
        if not self.connection:
            print("faça a conexão")
            return None
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
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
        return None

    def insert_data(self, full_dataset):
        """Insere dados na tabela Notas."""
        if not self.connection:
            print("faça a conexão")
            return
        cursor = self.connection.cursor()
        campos_tabela = (
            "NFe",
            "serie",
            "data_emissao",
            "chave",
            "cnpj_emitente",
            "nome_emitente",
            "valorNfe",
            "itemNota",
            "cod",
            "qntd",
            "descricao",
            "unidade_medida",
            "valorProd",
            "data_importacao",
            "usuario",
            "data_saida",
        )
        qntd = ",".join(["?"] * 16)
        query = f"INSERT INTO Notas {campos_tabela} VALUES ({qntd})"
        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Nota já existe no banco")

    def create_table_nfe(self):
        """Cria a tabela Notas, se não existir."""
        if not self.connection:
            print("faça a conexão")
            return
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Notas(
                NFe TEXT,
                serie TEXT,
                data_emissao TEXT,
                chave TEXT,
                cnpj_emitente TEXT,
                nome_emitente TEXT,                
                valorNfe TEXT,
                itemNota TEXT,
                cod TEXT,
                qntd TEXT,
                descricao TEXT,
                unidade_medida TEXT,
                valorProd TEXT,
                data_importacao TEXT,
                usuario TEXT,
                data_saida TEXT,
                PRIMARY KEY(chave, NFe, itemNota)
            );
            """
        )

    def uptdate_estoque(self, data_saida, user, notas):
        """Atualiza o estoque com a data de saída e o usuário."""
        if not self.connection:
            print("faça a conexão")
            return
        cursor = self.connection.cursor()
        for nota in notas:
            cursor.execute(
                f"""UPDATE Notas SET data_saida = '{data_saida}', 
                usuario = '{user}' WHERE NFe = '{nota}'"""
            )
        self.connection.commit()

    def update_estorno(self, notas):
        """Estorna a data de saída das notas especificadas."""
        if not self.connection:
            print("faça a conexão")
            return
        cursor = self.connection.cursor()
        for nota in notas:
            cursor.execute("UPDATE Notas SET data_saida = '' WHERE NFe = ?", (nota,))
        self.connection.commit()

    def get_all_notes(self):
        """Busca todas as notas na tabela Notas."""
        if not self.connection:
            print("faça a conexão")
            return []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Notas")
        return cursor.fetchall()


if __name__ == "__main__":
    db = Database()
    db.conecta()
    db.create_table_users()
    db.create_table_nfe()

    # Exibir todas as notas da tabela Notas
    notas = db.get_all_notes()
    if notas:
        for nota in notas:
            print(nota)
    else:
        print("Nenhum dado encontrado na tabela Notas.")

    db.close_connection()
