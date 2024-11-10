import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de QTableView com SQLite")
        self.setGeometry(100, 100, 600, 400)

        # Criação da QTableView
        self.table_view = QTableView(self)
        self.table_view.setGeometry(50, 50, 500, 300)

        # Conectar ao banco de dados SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("exemplo.db")

        # Verificar se a conexão foi bem-sucedida
        if not self.db.open():
            print("Erro ao abrir o banco de dados")
            return

        # Criar o modelo para a QTableView
        self.model = QSqlTableModel(self)
        self.model.setTable("clientes")  # Nome da tabela no banco de dados
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()  # Carregar os dados da tabela no modelo

        # Definir o modelo para a QTableView
        self.table_view.setModel(self.model)

        # Ajustar a exibição da tabela
        self.table_view.resizeColumnsToContents()  # Ajustar o tamanho das colunas
        self.table_view.setSortingEnabled(True)  # Habilitar a ordenação das colunas

        # Exibir a janela
        self.show()


# Criar o aplicativo e iniciar a interface gráfica
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
