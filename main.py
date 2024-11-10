from os import access

from PySide6 import QtCore
from PySide6.QtGui import QIcon
from numpy import equal
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTreeWidgetItem,
    QWidget,
)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import Database
from xml_files import Read_xml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon("_imgs/logo.PNG")
        self.setWindowIcon(appIcon)

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):

        self.users = Database()
        self.users.conecta()
        autenticado = self.users.check_user(
            self.txt_user.text().upper(), self.txt_password.text()
        )

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":

            self.w = MainWindow(self.txt_user.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(
                    f"Login ou senha incorreto \n \n Tentativa: {self.tentativas +1} de 3"
                )
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear o usuário
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        appIcon = QIcon("_imgs/logo.PNG")
        self.setWindowIcon(appIcon)

        self.user = username
        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

        # *************PAGINAS DO SISTEMA***********************************************
        self.btn_pg_home.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home)
        )
        self.btn_pg_tables.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_table)
        )
        self.btn_pg_contato.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_contato)
        )
        self.btn_pg_sobre.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_sobre)
        )
        self.btn_pg_cadastro.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro)
        )
        self.btn_pg_import.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_import)
        )

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        # ARQUIVO XML
        self.btn_open.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        # filtro
        self.txt_filtro.textChanged.connect(self.update_filter)

        # gerar saida e estorno
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_estorno.clicked.connect(self.gerar_estorno)

        self.btn_excel.clicked.connect(self.excel_file)

        self.btn_chart.clicked.connect(self.graphic)

        self.reset_table()

    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divirgentes")
            msg.setText("A senha não é igual!")
            msg.exec_()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = Database()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(
            self,
            str("Open Directory"),
            "/home",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        self.txt_file.setText(self.path)

    def import_xml_files(self):

        xml = Read_xml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = Database()
        db.conecta()
        cont = 1

        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1

        # ATUALIZA A TABELA

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("importação concluída!")
        msg.exec_()
        self.progressBar.setValue(0)

        db.close_connection()

    def table_estoque(self):
        # Ajuste o estilo de exibição
        self.tw_estoque.setStyleSheet(
            "QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )

        # Conecte-se ao banco de dados e obtenha os dados
        cn = sqlite3.connect("system.db")
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cn)
        result_list = result.values.tolist()  # Converta o resultado para lista

        # Limpa os dados existentes para evitar duplicação
        self.tw_estoque.clear()

        # Verificação se há dados antes de continuar
        if not result_list:
            print("Nenhum dado encontrado na consulta.")
            return

        # # Para depuração: verifique se os dados foram carregados
        # print("Dados carregados:", result_list)

        previous_nfe = None
        parent_item = None

        # Itera sobre cada linha de resultado e cria itens na QTreeWidget
        for row in result_list:
            nfe = row[0]  # A primeira coluna é considerada o identificador 'Nfe'

            # Verifica se o NFE atual é o mesmo do último para criar hierarquia
            if nfe == previous_nfe:
                QTreeWidgetItem(
                    parent_item, list(map(str, row))
                )  # Adiciona como item filho
            else:
                # Cria um novo item pai
                parent_item = QTreeWidgetItem(self.tw_estoque, list(map(str, row)))
                parent_item.setCheckState(
                    0, QtCore.Qt.CheckState.Unchecked
                )  # CheckBox no primeiro item

            previous_nfe = nfe  # Atualiza o NFE anterior

        # Permitir ordenação e redimensionar colunas
        self.tw_estoque.setSortingEnabled(True)
        for i in range(self.tw_estoque.columnCount()):
            self.tw_estoque.resizeColumnToContents(i)

    def table_saida(self):
        # Ajuste o estilo de exibição
        self.tw_saida.setStyleSheet(
            "QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )

        # Conecte-se ao banco de dados e obtenha os dados
        cn = sqlite3.connect("system.db")
        result = pd.read_sql_query(
            """SELECT Nfe, serie, data_importacao, data_saida, usuario
         FROM Notas WHERE data_saida != ''""",
            cn,
        )
        result_list = result.values.tolist()  # Converta o resultado para lista

        # Limpa os dados existentes para evitar duplicação
        self.tw_saida.clear()

        # Verificação se há dados antes de continuar
        if not result_list:
            print("Nenhum dado encontrado na consulta.")
            return

        # # Para depuração: verifique se os dados foram carregados
        # print("Dados carregados:", result_list)

        previous_nfe = None
        parent_item = None

        # Itera sobre cada linha de resultado e cria itens na QTreeWidget
        for row in result_list:
            nfe = row[0]  # A primeira coluna é considerada o identificador 'Nfe'

            # Verifica se o NFE atual é o mesmo do último para criar hierarquia
            if nfe == previous_nfe:
                QTreeWidgetItem(
                    parent_item, list(map(str, row))
                )  # Adiciona como item filho
            else:
                # Cria um novo item pai
                parent_item = QTreeWidgetItem(self.tw_saida, list(map(str, row)))
                parent_item.setCheckState(
                    0, QtCore.Qt.CheckState.Unchecked
                )  # CheckBox no primeiro item

            previous_nfe = nfe  # Atualiza o NFE anterior

        # Permitir ordenação e redimensionar colunas
        self.tw_saida.setSortingEnabled(True)
        for i in range(self.tw_saida.columnCount()):
            self.tw_saida.resizeColumnToContents(i)

    def table_geral(self):

        self.tb_geral.setStyleSheet(
            " QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    def update_filter(self, s):
        s = re.sub(r"[\W_]+", "", s)
        filter_str = 'Nfe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def gerar_saida(self):

        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))

        recurse(self.tw_estoque.invisibleRootItem())

        # Pergunta se usuario realmente deseja fazer isos.
        self.question("saída")

    def gerar_estorno(self):

        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.tw_saida.invisibleRootItem())
        self.question("estorno")

    def question(self, table):

        msgBox = QMessageBox()

        if table == "estorno":
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText(
                "As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar."
            )
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText(
                "As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar."
            )
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = Database()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime("%d/%m/%Y")
                self.db = Database()
                self.db.conecta()
                self.db.uptdate_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    def excel_file(self):

        cnx = sqlite3.connect("system.db")
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo de notas.xlsx", sheet_name="Notas", index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec_()

    def graphic(self):

        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query("SELECT * FROM Notas", cnx)
        saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
