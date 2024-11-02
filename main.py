from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
import sys
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from controller import Controller
from database import Database


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")
        self.controller = Controller()

        # habilita botão de login
        # self.btn_login.clicked.connect(self.open_system)
        self.btn_login.clicked.connect(self.checkLogin)

    # def open_system(self):
    #     if self.txt_password.text() == '123':
    #         self.w = MainWindow(self.controller)
    #         self.w.show() # abre a janela principal
    #         self.close() # fecha a janela de login
    #     else:
    #         print('senha inválida.')

    def checkLogin(self):
        self.users = Database()
        self.users.conecta()
        autenticado = self.users.check_user(
            self.txt_user.text().upper(), self.txt_password.text()
        )

        if autenticado.lower() == "administrador" or autenticado == "user":

            self.w = MainWindow(self.controller)
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowIconText("Erro ao acessar")
                msg.setText(
                    f"Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3"
                )
                msg.exec()
                self.tentativas += 1
                if self.tentativas == 3:
                    # aqui pode se implementar um código para bloquear o usuário
                    self.users.close_connection()
                    sys.exit(0)

    def closeEvent(self, event):
        self.controller.close_db()
        event.accept()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, controller) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento de Atendimentos SAU - HEPP")
        self.controller = controller

        # ********************* Páginas do Sistema **********************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_cadastro.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro)
        )

        # Conecta o botão btn_cadastrar ao método subscribe_user
        self.btn_cadastrar.clicked.connect(self.subscribe_user)

    def subscribe_user(self):
        msg = QMessageBox()
        if self.txt_password.text() != self.txt_password_confirm.text():
            msg.setIcon(QMessageBox.Warning)
            msg.setText("As senhas não coincidem.")
            msg.setWindowTitle("Erro")
            msg.exec()
            return None

        name = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_password.text()
        access = self.cb_perfil.currentText()

        db = Database()
        db.conecta()
        db.insert_user(name, user, password, access)
        db.close_connection()

        msg = QMessageBox()
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
