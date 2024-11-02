# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
    QComboBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 447)
        MainWindow.setIconSize(QSize(48, 48))
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName("btn_home")
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(
            "QPushButton{\n"
            "    background-color: #2196F3;\n"
            "    border: none;\n"
            "    color: #fff;\n"
            "    padding: 15px 32px;\n"
            "    text-align: center;\n"
            "    text-decoration: none;\n"
            "    font-size: 16px;\n"
            "    margin: 4px 2px;\n"
            "    border-radius: 8px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            " background-color: #4CAF50;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName("btn_tables")
        self.btn_tables.setFont(font)
        self.btn_tables.setStyleSheet(
            "QPushButton{\n"
            "    background-color: #2196F3;\n"
            "    border: none;\n"
            "    color: #fff;\n"
            "    padding: 15px 32px;\n"
            "    text-align: center;\n"
            "    text-decoration: none;\n"
            "    font-size: 16px;\n"
            "    margin: 4px 2px;\n"
            "    border-radius: 8px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            " background-color: #4CAF50;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName("btn_sobre")
        self.btn_sobre.setFont(font)
        self.btn_sobre.setStyleSheet(
            "QPushButton{\n"
            "    background-color: #2196F3;\n"
            "    border: none;\n"
            "    color: #fff;\n"
            "    padding: 15px 32px;\n"
            "    text-align: center;\n"
            "    text-decoration: none;\n"
            "    font-size: 16px;\n"
            "    margin: 4px 2px;\n"
            "    border-radius: 8px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            " background-color: #4CAF50;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName("btn_contato")
        self.btn_contato.setFont(font)
        self.btn_contato.setStyleSheet(
            "QPushButton{\n"
            "    background-color: #2196F3;\n"
            "    border: none;\n"
            "    color: #fff;\n"
            "    padding: 15px 32px;\n"
            "    text-align: center;\n"
            "    text-decoration: none;\n"
            "    font-size: 16px;\n"
            "    margin: 4px 2px;\n"
            "    border-radius: 8px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            " background-color: #4CAF50;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName("btn_outro")
        self.btn_outro.setFont(font)
        self.btn_outro.setStyleSheet(
            "QPushButton{\n"
            "    background-color: #2196F3;\n"
            "    border: none;\n"
            "    color: #fff;\n"
            "    padding: 15px 32px;\n"
            "    text-align: center;\n"
            "    text-decoration: none;\n"
            "    font-size: 16px;\n"
            "    margin: 4px 2px;\n"
            "    border-radius: 8px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            " background-color: #4CAF50;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_outro)

        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName("Pages")
        self.pg_table = QWidget()
        self.pg_table.setObjectName("pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName("tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName("tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName("txt_file")

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName("btn_open")

        self.horizontalLayout_2.addWidget(self.btn_open)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName("tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName("tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName("frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName("btn_importar")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName("btn_gerar")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.frame_2)
        self.btn_estorno.setObjectName("btn_estorno")

        self.verticalLayout_3.addWidget(self.btn_estorno)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName("pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName("label")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName("pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName("label_14")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName("label_6")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName("txt_nome")

        self.horizontalLayout_7.addWidget(self.txt_nome)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName("txt_usuario")

        self.horizontalLayout_8.addWidget(self.txt_usuario)

        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.txt_password = QLineEdit(self.pg_cadastro)
        self.txt_password.setObjectName("txt_password")

        self.horizontalLayout_9.addWidget(self.txt_password)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.txt_password_confirm = QLineEdit(self.pg_cadastro)
        self.txt_password_confirm.setObjectName("txt_password_confirm")

        self.horizontalLayout_10.addWidget(self.txt_password_confirm)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName("label_11")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName("cb_perfil")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.cb_perfil)

        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName("label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName("btn_cadastrar")

        self.horizontalLayout_6.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName("label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.Pages.addWidget(self.pg_cadastro)

        self.verticalLayout.addWidget(self.Pages)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName("btn_pg_cadastro")

        self.horizontalLayout_4.addWidget(self.btn_pg_cadastro)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_home, self.btn_tables)
        QWidget.setTabOrder(self.btn_tables, self.btn_contato)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.btn_home.setText(QCoreApplication.translate("MainWindow", "HOME", None))
        self.btn_tables.setText(
            QCoreApplication.translate("MainWindow", "TABLES", None)
        )
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", "SOBRE", None))
        self.btn_contato.setText(
            QCoreApplication.translate("MainWindow", "CONTATO", None)
        )
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", "OUTRO", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", "Abrir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "ESTOQUE:", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(
            12, QCoreApplication.translate("MainWindow", "Usuario", None)
        )
        ___qtreewidgetitem.setText(
            11, QCoreApplication.translate("MainWindow", "Data Importacao", None)
        )
        ___qtreewidgetitem.setText(
            10, QCoreApplication.translate("MainWindow", "Valor Nfe", None)
        )
        ___qtreewidgetitem.setText(
            9, QCoreApplication.translate("MainWindow", "Especie", None)
        )
        ___qtreewidgetitem.setText(
            8, QCoreApplication.translate("MainWindow", "UN", None)
        )
        ___qtreewidgetitem.setText(
            7, QCoreApplication.translate("MainWindow", "Descricao", None)
        )
        ___qtreewidgetitem.setText(
            6, QCoreApplication.translate("MainWindow", "Quantidade", None)
        )
        ___qtreewidgetitem.setText(
            5, QCoreApplication.translate("MainWindow", "Cod item", None)
        )
        ___qtreewidgetitem.setText(
            4, QCoreApplication.translate("MainWindow", "Municipio", None)
        )
        ___qtreewidgetitem.setText(
            3, QCoreApplication.translate("MainWindow", "UF", None)
        )
        ___qtreewidgetitem.setText(
            2, QCoreApplication.translate("MainWindow", "Cliente", None)
        )
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("MainWindow", "Serie", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "Nfe", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "SAIDA:", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(
            4, QCoreApplication.translate("MainWindow", "USUARIO", None)
        )
        ___qtreewidgetitem1.setText(
            3, QCoreApplication.translate("MainWindow", "DATA SAIDA", None)
        )
        ___qtreewidgetitem1.setText(
            2,
            QCoreApplication.translate("MainWindow", "DATA IMPORTA\u00c7\u00c3O", None),
        )
        ___qtreewidgetitem1.setText(
            1, QCoreApplication.translate("MainWindow", "S\u00c9RIE", None)
        )
        ___qtreewidgetitem1.setText(
            0, QCoreApplication.translate("MainWindow", "Nfe", None)
        )
        self.btn_importar.setText(
            QCoreApplication.translate("MainWindow", "Importar", None)
        )
        self.btn_gerar.setText(
            QCoreApplication.translate("MainWindow", "Gerar Sa\u00edda", None)
        )
        self.btn_estorno.setText(
            QCoreApplication.translate("MainWindow", "Estorno", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tables),
            QCoreApplication.translate("MainWindow", "TreeWidget", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Tab 2", None),
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:48pt; font-weight:600; color:#00004d;">RAMAR</span></p><p align="center"><span style=" font-size:36pt; font-weight:600; color:#00004d;">Sistema De Gerenciamento</span></p></body></html>',
                None,
            )
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Tela de Cadastro", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">CADASTRAR USU\u00c1RIO</p></body></html>',
                None,
            )
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Nome: ", None))
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "Usu\u00e1rio: ", None)
        )
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Senha:", None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Confirmar Senha: ", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "Perfil: ", None)
        )
        self.cb_perfil.setItemText(0, "")
        self.cb_perfil.setItemText(
            1, QCoreApplication.translate("MainWindow", "Administrador", None)
        )
        self.cb_perfil.setItemText(
            2, QCoreApplication.translate("MainWindow", "Usu\u00e1rio", None)
        )

        self.label_12.setText("")
        self.btn_cadastrar.setText(
            QCoreApplication.translate("MainWindow", "Cadastrar", None)
        )
        self.label_13.setText("")
        self.label_5.setText("")
        self.btn_pg_cadastro.setText(
            QCoreApplication.translate("MainWindow", "Cadastrar Usu\u00e1rio", None)
        )
        self.label_4.setText("")

    # retranslateUi
