import sys
import sqlite3
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout,QComboBox, QHBoxLayout, QLineEdit, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget,QMessageBox)
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel,QSqlTableModel
import random

def create_connection():
    db = QSqlDatabase.addDatabase("QSQLITE")  # Используем SQLite в качестве примера, можно выбрать другую БД
    db.setDatabaseName("Shop.db")  # Укажите путь к вашей базе данных
    if not db.open():
        print("Не удалось открыть базу данных")
        return False
    return True
global name
global price
quantity = 1

class Ui_MainWindow(object):
    #def setupModel(self):
    #    self.model = QSqlQueryModel(self)
#
    #    # Выполняем запрос к базе данных
    #    query = "SELECT * FROM Tovar"
    #    self.model.setQuery(query)
#
    #    # Устанавливаем модель для QTableView
    #    self.ui.tableView.setModel(self.model)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(789, 535)
        MainWindow.setMinimumSize(QSize(789, 535))
        MainWindow.setMaximumSize(QSize(789, 535))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")




        self.tableView = QTableView(self.centralwidget)

        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")


        if not create_connection():
            return

        self.query_model = QSqlQueryModel()
        self.query_model.setQuery("SELECT * FROM Tovar")

        if self.query_model.lastError().isValid():
            print(self.query_model.lastError().text())
            return

        self.tableView.setModel(self.query_model)
        self.tableView.resizeColumnsToContents()


        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")

        self.login.clicked.connect(self.Button_login)

        self.login.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:15px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:14px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"ico/Login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login.setIcon(icon1)

        self.horizontalLayout.addWidget(self.login)

        self.registration = QPushButton(self.centralwidget)

        self.registration.clicked.connect(self.Button_registr)

        self.registration.setObjectName(u"registration")
        self.registration.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:15px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:14px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"ico/Add_acaunt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registration.setIcon(icon2)

        self.horizontalLayout.addWidget(self.registration)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.basket = QPushButton(self.centralwidget)
        self.basket.setObjectName(u"basket")

        self.basket.clicked.connect(self.Button_basket)

        self.basket.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"ico/Basket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.basket.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.basket)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"	font-weight:bold;")

        self.verticalLayout_2.addWidget(self.label)

        self.off = QPushButton(self.centralwidget)
        self.off.setObjectName(u"off")

        self.off.clicked.connect(self.Button_off)

        self.off.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout_2.addWidget(self.off)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
                                         "    border-radius:4px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "border-radius:4px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
                                         "    color: white; \n"
                                         "}")

        self.verticalLayout.addWidget(self.pushButton_14)

        self.pushButton_14.clicked.connect(self.more_than_four)



        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.pushButton.clicked.connect(self.Button_BTehnic)

        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.pushButton_2.clicked.connect(self.Button_Beauty)

        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.Button_Smartphone)

        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.pushButton_4.clicked.connect(self.Button_TV)


        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.pushButton_5.clicked.connect(self.Button_PK)

        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.pushButton_6.clicked.connect(self.Button_Set)

        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.pushButton_7.clicked.connect(self.Button_office)


        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.pushButton_8.clicked.connect(self.Button_Relax)


        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.pushButton_9.clicked.connect(self.Button_Build)

        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.pushButton_10.clicked.connect(self.Button_Garden)


        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.pushButton_11.clicked.connect(self.Button_house)


        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.pushButton_12.clicked.connect(self.Button_auto)


        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.pushButton_13.clicked.connect(self.Button_services)


        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_13)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.basket.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.off.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u">4", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0442\u043e\u0432\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043e\u0442\u0430 \u0438 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u044b", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0412 \u0438 \u043a\u043e\u043d\u0441\u043e\u043b\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041a, \u043d\u043e\u0443\u0442\u0431\u0443\u043a\u0438", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0443\u044e\u0449\u0438\u0435", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u0438\u0441 \u0438 \u043c\u0435\u0431\u0435\u043b\u044c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u044b\u0445 \u0438 \u0440\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442 \u0438 \u0441\u0442\u0440\u043e\u0439\u043a\u0430", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u0434\u043e\u0432\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c, \u0434\u0435\u043a\u043e\u0440", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0441\u0435\u0441\u0441\u0443\u0430\u0440\u044b \u0438 \u0443\u0441\u043b\u0443\u0433\u0438", None))
    # retranslateUi


    def Button_login(self):
        print("ты кликнул на кнопку Войти")

    def Button_registr(self):
        print("ты кликнул на кнопку Регистрации")

    def Button_basket(self):
        global name,price

        current_index= self.tableView.currentIndex()
        if current_index.isValid():
            row = current_index.row()
            model = self.tableView.model()
            row_all = [model.data(model.index(row,column),Qt.DisplayRole)
                       for column in range(model.columnCount())]
            print(row_all[0],row_all[1],row_all[2],row_all[3],row_all[4])

            name = row_all[1]
            price = row_all[2]


    def Button_off(self):
        query = "SELECT * FROM tovar"
        self.query_model.setQuery(query)
        if self.query_model.lastError().isValid():
            print(self.query_model.lastError().text())
        else:
            self.tableView.resizeColumnsToContents()

    def more_than_four(self):
        query = "SELECT * FROM tovar WHERE rating > 4 "
        self.query(query)


    #Настройки
    def Button_BTehnic(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Бытовая техника'"
        self.query(query)
    def Button_Beauty(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Красота и здоровье'"
        self.query(query)
    def Button_Smartphone(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Смартфоны'"
        self.query(query)
    def Button_TV(self):

        query = "SELECT * FROM tovar WHERE Filter == 'Консоли и аудио'"
        self.query(query)
    def Button_PK(self):
        query = "SELECT * FROM tovar WHERE Filter == 'ПК'"
        self.query(query)
    def Button_Set(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Комплектующие'"
        self.query(query)
    def Button_office(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Офис'"
        self.query(query)
    def Button_Relax(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Отдых' "
        self.query(query)
    def Button_Build(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Инструмент'"
        self.query(query)
    def Button_Garden(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Сад'"
        self.query(query)
    def Button_house(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Дом'"
        self.query(query)
    def Button_auto(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Автотовары'"
        self.query(query)
    def Button_services(self):
        query = "SELECT * FROM tovar WHERE Filter == 'Аксессуары'"
        self.query(query)

    def query(self,query):
        self.query_model.setQuery(query)
        if self.query_model.lastError().isValid():
            print(self.query_model.lastError().text())
        else:
            self.tableView.resizeColumnsToContents()

class Ui_MainWindow_buy(object):
    global quantity

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 174)
        MainWindow.setMinimumSize(QSize(543, 174))
        MainWindow.setMaximumSize(QSize(543, 174))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 10, 81, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_quantity = QLabel(self.centralwidget)
        self.label_quantity.setObjectName(u"label_quantity")
        self.label_quantity.setGeometry(QRect(10, 70, 91, 41))
        self.label_quantity.setFont(font)
        self.label_quantity.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.pushButton_buy = QPushButton(self.centralwidget)
        self.pushButton_buy.setObjectName(u"pushButton_buy")
        self.pushButton_buy.setGeometry(QRect(210, 110, 111, 31))
        self.pushButton_buy.setStyleSheet(u"QPushButton {\n"
                                          "    border-radius:4px;\n"
                                          "	font-size:15px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "font-size:14px;\n"
                                          "border-radius:4px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
                                          "    color: white; \n"
                                          "}\n"
                                          "\n"
                                          "")
        self.label_price = QLabel(self.centralwidget)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setGeometry(QRect(10, 40, 51, 31))
        self.label_price.setFont(font)
        self.label_price.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_name = QLabel(self.centralwidget)
        self.text_name.setObjectName(u"text_name")
        self.text_name.setGeometry(QRect(110, 20, 49, 16))
        self.text_name.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_price = QLabel(self.centralwidget)
        self.text_price.setObjectName(u"text_price")
        self.text_price.setGeometry(QRect(110, 50, 49, 16))
        self.text_price.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_kol = QLabel(self.centralwidget)
        self.text_kol.setObjectName(u"text_kol")
        self.text_kol.setGeometry(QRect(110, 80, 49, 16))
        self.text_kol.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(140, 110, 61, 31))
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet(u"background-color:rgba(0,0,0,0)")

        self.pushButton_add.clicked.connect(self.button_add)


        icon1 = QIcon()
        icon1.addFile(u"ico/Add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setIconSize(QSize(25, 25))
        self.pushButton_add_2 = QPushButton(self.centralwidget)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setGeometry(QRect(80, 110, 61, 31))
        self.pushButton_add_2.setFont(font)
        self.pushButton_add_2.setStyleSheet(u"background-color:rgba(0,0,0,0)")

        self.pushButton_add_2.clicked.connect(self.minus)

        icon2 = QIcon()
        icon2.addFile(u"ico/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_2.setIcon(icon2)
        self.pushButton_add_2.setIconSize(QSize(25, 25))
        self.pushButton_beak = QPushButton(self.centralwidget)
        self.pushButton_beak.setObjectName(u"pushButton_beak")
        self.pushButton_beak.setGeometry(QRect(10, 110, 61, 31))
        self.pushButton_beak.setFont(font)
        self.pushButton_beak.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        icon3 = QIcon()
        icon3.addFile(u"ico/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_beak.setIcon(icon3)
        self.pushButton_beak.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.label_name.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_quantity.setText(
            QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:",
                                       None))
        self.pushButton_buy.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043f\u043b\u0430\u0442\u044b",
                                                               None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430:", None))
        self.text_name.setText(QCoreApplication.translate("MainWindow", f"{name}", None))
        self.text_price.setText(QCoreApplication.translate("MainWindow", f"{price}", None))
        self.text_kol.setText(QCoreApplication.translate("MainWindow", f"{quantity}", None))
        self.pushButton_add.setText("")
        self.pushButton_add_2.setText("")
        self.pushButton_beak.setText("")

    # retranslateUi

    def button_add(self):
        global quantity,price
        quantity += 1
        self.text_kol.setText(str(quantity))
        self.text_price.setText(str(price*quantity))


    def minus(self):
        global quantity,price
        quantity = 1
        self.text_kol.setText(str(quantity))
        self.text_price.setText(str(price*quantity))

class Ui_MainWindow_payment(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(398, 118)
        MainWindow.setMinimumSize(QSize(398, 118))
        MainWindow.setMaximumSize(QSize(398, 118))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 0, 261, 51))
        self.pushButton.clicked.connect(self.nal)


        font = QFont()
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:15px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:14px;\n"
"border-radius:4px;\n"
"\n"
"    color: white; \n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"ico/Nal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 131, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:15px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:14px;\n"
"border-radius:4px;\n"
"\n"
"    color: white; \n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"ico/credit_cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))


        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 60, 401, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:15px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:14px;\n"
"border-radius:4px;\n"
"\n"
"    color: white; \n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"ico/credit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0439", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0435\u0434\u0438\u0442", None))
    # retranslateUi


    def nal(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("TechSphere")
        ico = QIcon("ico/Shop.png")
        msgBox.setWindowIcon(ico)
        msgBox.setText("Оплата прошла успешно")
        msgBox.exec()

class Ui_MainWindow_credit(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(651, 376)
        MainWindow.setMinimumSize(651, 376)
        MainWindow.setMaximumSize(651, 376)
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_fio = QLineEdit(self.centralwidget)
        self.text_fio.setObjectName(u"text_fio")
        self.text_fio.setGeometry(QRect(10, 40, 331, 22))
        self.text_fio.setStyleSheet(u"border-radius:4px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 49, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_Issued = QLineEdit(self.centralwidget)
        self.text_Issued.setObjectName(u"text_Issued")
        self.text_Issued.setGeometry(QRect(180, 100, 241, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 81, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_seria_1 = QLineEdit(self.centralwidget)
        self.text_seria_1.setObjectName(u"text_seria_1")
        self.text_seria_1.setGeometry(QRect(70, 70, 31, 22))
        self.text_seria_1.setStyleSheet(u"border-radius:4px;")
        self.text_seria_1.setMaxLength(1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 49, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_seria_2 = QLineEdit(self.centralwidget)
        self.text_seria_2.setObjectName(u"text_seria_2")
        self.text_seria_2.setGeometry(QRect(110, 70, 31, 22))
        self.text_seria_2.setStyleSheet(u"border-radius:4px;")
        self.text_seria_2.setMaxLength(1)
        self.text_seria_3 = QLineEdit(self.centralwidget)
        self.text_seria_3.setObjectName(u"text_seria_3")
        self.text_seria_3.setGeometry(QRect(150, 70, 31, 22))
        self.text_seria_3.setStyleSheet(u"border-radius:4px;")
        self.text_seria_3.setMaxLength(1)
        self.text_seria_4 = QLineEdit(self.centralwidget)
        self.text_seria_4.setObjectName(u"text_seria_4")
        self.text_seria_4.setGeometry(QRect(190, 70, 31, 22))
        self.text_seria_4.setStyleSheet(u"border-radius:4px;")
        self.text_seria_4.setMaxLength(1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 70, 21, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_number_4 = QLineEdit(self.centralwidget)
        self.text_number_4.setObjectName(u"text_number_4")
        self.text_number_4.setGeometry(QRect(380, 70, 31, 22))
        self.text_number_4.setStyleSheet(u"border-radius:4px;")
        self.text_number_4.setMaxLength(1)
        self.text_number_3 = QLineEdit(self.centralwidget)
        self.text_number_3.setObjectName(u"text_number_3")
        self.text_number_3.setGeometry(QRect(340, 70, 31, 22))
        self.text_number_3.setStyleSheet(u"border-radius:4px;")
        self.text_number_3.setMaxLength(1)
        self.text_number_2 = QLineEdit(self.centralwidget)
        self.text_number_2.setObjectName(u"text_number_2")
        self.text_number_2.setGeometry(QRect(300, 70, 31, 22))
        self.text_number_2.setStyleSheet(u"border-radius:4px;")
        self.text_number_2.setMaxLength(1)
        self.text_number_1 = QLineEdit(self.centralwidget)
        self.text_number_1.setObjectName(u"text_number_1")
        self.text_number_1.setGeometry(QRect(260, 70, 31, 22))
        self.text_number_1.setStyleSheet(u"border-radius:4px;")
        self.text_number_1.setMaxLength(1)
        self.text_date_4 = QLineEdit(self.centralwidget)
        self.text_date_4.setObjectName(u"text_date_4")
        self.text_date_4.setGeometry(QRect(310, 130, 31, 22))
        self.text_date_4.setStyleSheet(u"border-radius:4px;")
        self.text_date_4.setMaxLength(1)
        self.text_date_3 = QLineEdit(self.centralwidget)
        self.text_date_3.setObjectName(u"text_date_3")
        self.text_date_3.setGeometry(QRect(270, 130, 31, 22))
        self.text_date_3.setStyleSheet(u"border-radius:4px;")
        self.text_date_3.setMaxLength(1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 91, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_date_5 = QLineEdit(self.centralwidget)
        self.text_date_5.setObjectName(u"text_date_5")
        self.text_date_5.setGeometry(QRect(360, 130, 31, 22))
        self.text_date_5.setStyleSheet(u"border-radius:4px;")
        self.text_date_5.setMaxLength(1)
        self.text_date_8 = QLineEdit(self.centralwidget)
        self.text_date_8.setObjectName(u"text_date_8")
        self.text_date_8.setGeometry(QRect(480, 130, 31, 22))
        self.text_date_8.setStyleSheet(u"border-radius:4px;")
        self.text_date_8.setMaxLength(1)
        self.text_date_7 = QLineEdit(self.centralwidget)
        self.text_date_7.setObjectName(u"text_date_7")
        self.text_date_7.setGeometry(QRect(440, 130, 31, 22))
        self.text_date_7.setStyleSheet(u"border-radius:4px;")
        self.text_date_7.setMaxLength(1)
        self.text_date_2 = QLineEdit(self.centralwidget)
        self.text_date_2.setObjectName(u"text_date_2")
        self.text_date_2.setGeometry(QRect(220, 130, 31, 22))
        self.text_date_2.setStyleSheet(u"border-radius:4px;")
        self.text_date_2.setMaxLength(1)
        self.text_date_6 = QLineEdit(self.centralwidget)
        self.text_date_6.setObjectName(u"text_date_6")
        self.text_date_6.setGeometry(QRect(400, 130, 31, 22))
        self.text_date_6.setStyleSheet(u"border-radius:4px;")
        self.text_date_6.setMaxLength(1)
        self.text_date_1 = QLineEdit(self.centralwidget)
        self.text_date_1.setObjectName(u"text_date_1")
        self.text_date_1.setGeometry(QRect(180, 130, 31, 22))
        self.text_date_1.setStyleSheet(u"border-radius:4px;")
        self.text_date_1.setMaxLength(1)
        self.text_code = QLineEdit(self.centralwidget)
        self.text_code.setObjectName(u"text_code")
        self.text_code.setGeometry(QRect(180, 160, 241, 22))
        self.text_code.setStyleSheet(u"border-radius:4px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 160, 151, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 190, 131, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_family = QComboBox(self.centralwidget)
        self.text_family.addItem("")
        self.text_family.addItem("")
        self.text_family.addItem("")
        self.text_family.addItem("")
        self.text_family.setObjectName(u"text_family")
        self.text_family.setEnabled(True)
        self.text_family.setGeometry(QRect(180, 190, 241, 22))
        self.text_family.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.text_family.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_family.setStyleSheet(u"border-radius:4px;")
        self.text_family.setEditable(False)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 220, 111, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_address = QLineEdit(self.centralwidget)
        self.text_address.setObjectName(u"text_address")
        self.text_address.setGeometry(QRect(180, 220, 241, 22))
        self.text_address.setStyleSheet(u"border-radius:4px;")
        self.text_address_pr = QLineEdit(self.centralwidget)
        self.text_address_pr.setObjectName(u"text_address_pr")
        self.text_address_pr.setGeometry(QRect(180, 250, 241, 22))
        self.text_address_pr.setStyleSheet(u"border-radius:4px;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 250, 121, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 280, 71, 16))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_number = QLineEdit(self.centralwidget)
        self.text_number.setObjectName(u"text_number")
        self.text_number.setGeometry(QRect(180, 280, 241, 22))
        self.text_number.setStyleSheet(u"border-radius:4px;")
        self.text_number.setMaxLength(10)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 280, 21, 16))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 310, 49, 16))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_email = QLineEdit(self.centralwidget)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setGeometry(QRect(180, 310, 241, 22))
        self.text_email.setStyleSheet(u"border-radius:4px;")
        self.text_connection = QComboBox(self.centralwidget)
        self.text_connection.addItem("")
        self.text_connection.addItem("")
        self.text_connection.addItem("")
        self.text_connection.setObjectName(u"text_connection")
        self.text_connection.setEnabled(True)
        self.text_connection.setGeometry(QRect(180, 340, 241, 22))
        self.text_connection.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.text_connection.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_connection.setStyleSheet(u"border-radius:4px;\n"
                                           "")
        self.text_connection.setEditable(False)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 340, 81, 16))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 340, 101, 24))

        self.pushButton.clicked.connect(self.Take_credit)

        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "    border-radius:4px;\n"
                                      "	font-size:17px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "font-size:15px;\n"
                                      "border-radius:4px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
                                      "    color: white; \n"
                                      "}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d", None))
        self.text_seria_1.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u2116", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438",
                                       None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f",
                                                        None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u0435\u043c\u0435\u0439\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435",
                                                        None))
        self.text_family.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                   u"\u0425\u043e\u043b\u043e\u0441\u0442/\u043d\u0435 \u0437\u0430\u043c\u0443\u0436\u0435\u043c",
                                                                   None))
        self.text_family.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                   u"\u0420\u0430\u0437\u0432\u0435\u0434\u0435\u043d/\u0420\u0430\u0437\u0432\u0435\u0434\u0435\u043d\u0430",
                                                                   None))
        self.text_family.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                   u"\u0416\u0435\u043d\u0430\u0442/\u0417\u0430\u043c\u0443\u0436\u0435\u043c",
                                                                   None))
        self.text_family.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                   u"\u0412\u0434\u043e\u0432\u0435\u043d/\u0412\u0434\u043e\u0432\u0430",
                                                                   None))

        self.text_family.setCurrentText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0425\u043e\u043b\u043e\u0441\u0442/\u043d\u0435 \u0437\u0430\u043c\u0443\u0436\u0435\u043c",
                                                                   None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0410\u0434\u0440\u0435\u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438",
                                                        None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f",
                                                        None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.text_number.setText("")
        self.text_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(___)-__-__", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"+7", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.text_connection.setItemText(0, QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.text_connection.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                       u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d",
                                                                       None))
        self.text_connection.setItemText(2, QCoreApplication.translate("MainWindow", u"Email", None))

        self.text_connection.setCurrentText(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0441\u0432\u044f\u0437\u0438", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))

    # retranslateUi


    def Take_credit(self):
        if self.text_fio.text() == "" or self.text_seria_1.text() == ""or self.text_seria_2.text() == ""or self.text_seria_3.text()== "" or self.text_seria_4.text() == ""or self.text_number.text() == ""or self.text_number_2.text()== ""\
                or self.text_number_3.text() == "" or self.text_number_4.text() == "" or self.text_Issued.text() == ""or self.text_date_1.text() == ""or self.text_date_2.text()== "" or self.text_date_3.text() == ""or self.text_date_4.text()== ""\
                or self.text_date_5.text() == "" or self.text_date_6.text() == "" or self.text_date_7.text() == "" or self.text_date_8.text()== "" or self.text_code.text() == ""or self.text_address.text()== ""\
                or self.text_address_pr.text() == "" or self.text_number.text() == "" or self.text_email.text() == "":
            return False
        else:
            Yes_or_NO = ["Да", "Нет"]
            result = random.choice(Yes_or_NO)

            if result =="Да":
                a = "Вам одобрен кредит на покупку"
            else:
                a = "К сожелению вы не понравились банку"


            box_msg = QMessageBox()
            box_msg.setWindowTitle("TechSphere")
            ico = QIcon(u"ico/Shop.png")
            box_msg.setWindowIcon(ico)
            box_msg.setText(f"{a}")
            box_msg.exec()
            return True

class Ui_MainWindow_card(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 188)
        MainWindow.setMinimumSize(385, 188)
        MainWindow.setMaximumSize(385, 188)
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Button_pay = QPushButton(self.centralwidget)
        self.Button_pay.setObjectName(u"Button_pay")
        self.Button_pay.setGeometry(QRect(250, 150, 121, 24))
        font = QFont()
        self.Button_pay.setFont(font)

        self.Button_pay.clicked.connect(self.cheak_card)

        self.Button_pay.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.label_nuber = QLabel(self.centralwidget)
        self.label_nuber.setObjectName(u"label_nuber")
        self.label_nuber.setGeometry(QRect(10, 10, 71, 21))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_nuber.setFont(font1)
        self.label_nuber.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.Text_number = QLineEdit(self.centralwidget)
        self.Text_number.setObjectName(u"Text_number")
        self.Text_number.setGeometry(QRect(10, 40, 361, 22))
        self.Text_number.setFont(font1)
        self.Text_number.setMaxLength(20)
        self.Text_Term1 = QLineEdit(self.centralwidget)
        self.Text_Term1.setObjectName(u"Text_Term1")
        self.Text_Term1.setGeometry(QRect(10, 120, 51, 22))
        self.Text_Term1.setFont(font1)
        self.Text_Term1.setMaxLength(2)
        self.Text_Code = QLineEdit(self.centralwidget)
        self.Text_Code.setObjectName(u"Text_Code")
        self.Text_Code.setGeometry(QRect(220, 120, 81, 22))
        self.Text_Code.setFont(font1)
        self.Text_Code.setMaxLength(3)
        self.label_Term = QLabel(self.centralwidget)
        self.label_Term.setObjectName(u"label_Term")
        self.label_Term.setGeometry(QRect(10, 80, 61, 31))
        self.label_Term.setFont(font1)
        self.label_Term.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_Code = QLabel(self.centralwidget)
        self.label_Code.setObjectName(u"label_Code")
        self.label_Code.setGeometry(QRect(220, 80, 41, 31))
        self.label_Code.setFont(font1)
        self.label_Code.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.Text_Term_2 = QLineEdit(self.centralwidget)
        self.Text_Term_2.setObjectName(u"Text_Term_2")
        self.Text_Term_2.setGeometry(QRect(70, 120, 51, 22))
        self.Text_Term_2.setFont(font1)
        self.Text_Term_2.setMaxLength(2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button_pay.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.label_nuber.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_Term.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None))
        self.label_Code.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
    # retranslateUi


    def cheak_card(self):
        if not (self.Text_Code.text() != "" and self.Text_number.text() != "" and
                self.Text_Term1.text() != "" and self.Text_Term_2.text() != ""):
            return True
        else:
            box_msg = QMessageBox()
            box_msg.setWindowTitle("TechSphere")
            ico = QIcon(u"ico/Shop.png")
            box_msg.setWindowIcon(ico)
            box_msg.setText(f"Оплата прошла успешно")
            box_msg.exec()
            return False