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
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(418, 409)
        Login.setStyleSheet("background-color: blue;")
        self.frame = QFrame(Login)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(60, 170, 311, 201))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0,0.8);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName("txt_user")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_user.setFont(font)
        self.txt_user.setFocusPolicy(Qt.TabFocus)
        self.txt_user.setStyleSheet("color: #ffffff;\n" "border: 1px solid #ffffff;")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_user)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName("txt_password")
        self.txt_password.setFont(font)
        self.txt_password.setFocusPolicy(Qt.TabFocus)
        self.txt_password.setStyleSheet(
            "color: #ffffff;\n" "border: 1px solid #ffffff;"
        )
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_password)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName("btn_login")
        font1 = QFont()
        font1.setFamilies(["News706 BT"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(
            "QPushButton{\n"
            "background-color: lightblue;\n"
            "	color: #000000;\n"
            "border: 2px solid ;\n"
            "	border-color:#FFFFFF;\n"
            "border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: blue;\n"
            "	color: #00aa00;\n"
            "border:2px solid;\n"
            "border-color: #00aa00;\n"
            "\n"
            "}"
        )

        self.verticalLayout.addWidget(self.btn_login)

        self.label = QLabel(Login)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(100, 20, 221, 171))
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
        self.txt_user.setPlaceholderText(
            QCoreApplication.translate("Login", "Usu\u00e1rio", None)
        )
        self.txt_password.setPlaceholderText(
            QCoreApplication.translate("Login", "Senha", None)
        )
        self.btn_login.setText(QCoreApplication.translate("Login", "Login", None))
        self.label.setText("")

    # retranslateUi
