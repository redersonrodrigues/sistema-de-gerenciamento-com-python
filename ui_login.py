# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(463, 489)
        Login.setStyleSheet("background-color: rgb(2, 80, 175);")
        self.frame = QFrame(Login)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(100, 160, 261, 221))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setGeometry(QRect(74, 145, 121, 51))
        font = QFont()
        font.setFamilies(["News706 BT"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(
            "QPushButton{\n"
            "background-color: #0250af;\n"
            "	color: #000000;\n"
            "border: 2px solid ;\n"
            "	border-color:#FFFFFF;\n"
            "border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #ffffff;\n"
            "	color: #0250af;\n"
            "border:2px solid;\n"
            "border-color: #0250af;\n"
            "\n"
            "}"
        )
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName("txt_user")
        self.txt_user.setGeometry(QRect(44, 60, 176, 23))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.txt_user.setFont(font1)
        self.txt_user.setFocusPolicy(Qt.TabFocus)
        self.txt_user.setStyleSheet("color: #ffffff;\n" "border: 1px solid #ffffff;")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName("txt_password")
        self.txt_password.setGeometry(QRect(44, 100, 176, 23))
        self.txt_password.setFont(font1)
        self.txt_password.setFocusPolicy(Qt.TabFocus)
        self.txt_password.setStyleSheet(
            "color: #ffffff;\n" "border: 1px solid #ffffff;"
        )
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Login)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(150, 80, 161, 131))
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setPixmap(QPixmap("assets/_imgs/logo_tela_login.png"))
        self.label.setScaledContents(True)
        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", "Form", None))
        self.btn_login.setText(QCoreApplication.translate("Login", "Login", None))
        self.txt_user.setPlaceholderText(
            QCoreApplication.translate("Login", "Usu\u00e1rio", None)
        )
        self.txt_password.setPlaceholderText(
            QCoreApplication.translate("Login", "Senha", None)
        )
        self.label.setText("")

    # retranslateUi
