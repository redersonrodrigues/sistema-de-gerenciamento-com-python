from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import Database


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")

        # habilita botão de login
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = Database()
        self.users.conecta()
        autenticado = self.users.check_user(
            self.txt_user.text().upper(), self.txt_password.text()
        )

        if autenticado in ["Administrador", "user"]:
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(
                    f"Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3"
                )
                msg.exec()
                self.tentativas += 1
                if self.tentativas == 3:
                    self.users.close_connection()
                    sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")

        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

        # ********************* Páginas do Sistema **********************
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

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

    def subscribe_user(self):
        msg = QMessageBox()
        if self.txt_password.text() != self.txt_password_confirm.text():
            msg.setIcon(QMessageBox.Warning)
            msg.setText("As senhas não coincidem.")
            msg.setWindowTitle("Senhas divergentes")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_password.text()
        access = self.cb_perfil.currentText()

        db = Database()
        try:
            db.conecta()
            db.insert_user(nome, user, password, access)
        except Exception as e:
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro de cadastro")
            msg.setText(f"Erro ao cadastrar usuário: {e}")
            msg.exec()
            return
        finally:
            db.close_connection()

        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_password.setText("")
        self.txt_password_confirm.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
