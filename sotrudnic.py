# -*- coding: utf-8 -*-
import sqlite3
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox,QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget,QTableView,QVBoxLayout,QMessageBox,QGridLayout)
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel,QSqlTableModel

from first_window import Ui_MainWindow

from random import randint

class Ui_MainWindow_sorudnic(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 151)
        MainWindow.setMinimumSize(375, 151)
        MainWindow.setMaximumSize(375, 151)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_tovar = QPushButton(self.centralwidget)
        self.add_tovar.setObjectName(u"add_tovar")
        self.add_tovar.setGeometry(QRect(80, 30, 211, 24))
        self.add_tovar.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.del_tovar = QPushButton(self.centralwidget)
        self.del_tovar.setObjectName(u"del_tovar")
        self.del_tovar.setGeometry(QRect(80, 60, 211, 24))
        self.del_tovar.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.add_perdon = QPushButton(self.centralwidget)
        self.add_perdon.setObjectName(u"add_perdon")
        self.add_perdon.setGeometry(QRect(80, 90, 211, 24))
        self.add_perdon.setStyleSheet(u"QPushButton {\n"
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
        self.add_tovar.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.del_tovar.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.add_perdon.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
    # retranslateUi
class Ui_MainWindow_Add_product(object):
    def connection(self):
        model = self.text_model.text()
        price = self.tetx_price.text()
        type = self.text_type.currentText()
        article = randint(999,9999999)
        rating = randint(1,5)

        conn = sqlite3.connect("Shop.db")
        cursor = conn.cursor()

        if price.isdigit() or (model == "", price == "", type == ""):
            cursor.execute("INSERT INTO Tovar (article,name,price,rating,Filter) VALUES(?,?,?,?,?)",(article,model,price,rating,type))
            conn.commit()

        conn.close()


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 217)
        MainWindow.setMinimumSize(373, 217)
        MainWindow.setMaximumSize(373, 217)
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(9, 9, 100, 16))
        self.label_name.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.tetx_price = QLineEdit(self.centralwidget)
        self.tetx_price.setObjectName(u"tetx_price")
        self.tetx_price.setGeometry(QRect(10, 80, 351, 22))
        self.label_price = QLabel(self.centralwidget)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setGeometry(QRect(10, 60, 28, 16))
        self.label_price.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_type = QLabel(self.centralwidget)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setGeometry(QRect(10, 110, 71, 16))
        self.label_type.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_type = QComboBox(self.centralwidget)
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.addItem("")
        self.text_type.setObjectName(u"text_type")
        self.text_type.setGeometry(QRect(10, 130, 351, 20))
        self.text_type.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(0, 190, 121, 24))
        self.add_button.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.text_model = QLineEdit(self.centralwidget)
        self.text_model.setObjectName(u"text_model")
        self.text_model.setGeometry(QRect(10, 30, 351, 22))
        self.Home = QPushButton(self.centralwidget)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(240, 190, 121, 24))
        self.Home.setStyleSheet(u"QPushButton {\n"
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u043a/\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.label_type.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.text_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0442\u043e\u0432\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430", None))
        self.text_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043e\u0442\u0430 \u0438 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435", None))
        self.text_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u044b", None))
        self.text_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u0438 \u0438 \u0430\u0443\u0434\u0438\u043e", None))
        self.text_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u041a", None))
        self.text_type.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0443\u044e\u0449\u0438\u0435", None))
        self.text_type.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041e\u0444\u0438\u0441", None))
        self.text_type.setItemText(7, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u044b\u0445", None))
        self.text_type.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        self.text_type.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u0434", None))
        self.text_type.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c", None))
        self.text_type.setItemText(11, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.text_type.setItemText(12, QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0441\u0435\u0441\u0441\u0443\u0430\u0440\u044b", None))

        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Home.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
    # retranslateUi
class Ui_MainWindow_delite(Ui_MainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(789, 535)
        MainWindow.setMinimumSize(789, 535)
        MainWindow.setMaximumSize(789, 535)
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)



        self.query_model = QSqlQueryModel()
        self.query_model.setQuery("SELECT * FROM Tovar")

        if self.query_model.lastError().isValid():
            print(self.query_model.lastError().text())
            return

        self.tableView.setModel(self.query_model)


        self.tableView.setObjectName(u"tableView")


        self.tableView.setGeometry(QRect(160, 60, 621, 471))
        self.tableView.setStyleSheet(u"c")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 151, 481))
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-15, 0, 171, 481))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)

        self.pushButton.clicked.connect(self.Button_BTehnic)

        self.pushButton.setObjectName(u"pushButton")
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

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.verticalLayout.addWidget(self.pushButton_13)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 131, 44))
        self.widget1.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_14 = QPushButton(self.widget1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
" border-radius:6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./ico/Menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setIconSize(QSize(23, 23))
        self.pushButton_14.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_14, 0, 1, 1, 1)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"	font-weight:bold;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.off = QPushButton(self.widget1)
        self.off.setObjectName(u"off")
        self.off.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")

        self.gridLayout.addWidget(self.off, 1, 0, 1, 2)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(160, 30, 481, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_dell = QPushButton(self.layoutWidget1)
        self.button_dell.setObjectName(u"button_dell")

        self.button_dell.clicked.connect(self.dell_tovar)

        self.button_dell.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"ico/Basket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_dell.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_dell)

        self.buttom_add = QPushButton(self.layoutWidget1)
        self.buttom_add.setObjectName(u"buttom_add")
        self.buttom_add.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.buttom_add.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttom_add)

        self.button_home = QPushButton(self.layoutWidget1)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.button_home.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_home)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_14.toggled.connect(self.widget.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)



        self.pushButton.clicked.connect(self.Button_BTehnic)
        self.pushButton_2.clicked.connect(self.Button_Beauty)
        self.pushButton_3.clicked.connect(self.Button_Smartphone)
        self.pushButton_4.clicked.connect(self.Button_TV)
        self.pushButton_5.clicked.connect(self.Button_PK)
        self.pushButton_6.clicked.connect(self.Button_Set)
        self.pushButton_7.clicked.connect(self.Button_office)
        self.pushButton_8.clicked.connect(self.Button_Relax)
        self.pushButton_9.clicked.connect(self.Button_Build)
        self.pushButton_10.clicked.connect(self.Button_Garden)
        self.pushButton_11.clicked.connect(self.Button_house)
        self.pushButton_12.clicked.connect(self.Button_auto)
        self.pushButton_13.clicked.connect(self.Button_services)
        self.off.clicked.connect(self.Button_off)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
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
        self.pushButton_14.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.off.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.button_dell.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.buttom_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_home.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
    # retranslateUi


    def dell_tovar(self):

        current_index = self.tableView.currentIndex()
        if current_index.isValid():
            row = current_index.row()
            model = self.tableView.model()
            row_all = [model.data(model.index(row, column), Qt.DisplayRole)
                       for column in range(model.columnCount())]
            print(row_all[0], row_all[1], row_all[2], row_all[3], row_all[4])

            con = sqlite3.connect("Shop.db")
            cursor = con.cursor()

            cursor.execute(f"DELETE From Tovar WHERE article =? or name = ? ",(row_all[0],row_all[1],))


            query = "SELECT * FROM Tovar"
            self.query_model.setQuery(query)
            if self.query_model.lastError().isValid():
                print(self.query_model.lastError().text())
            else:
                self.tableView.resizeColumnsToContents()


            con.commit()
            cursor.close()
            con.close()
            #model.removeRow(row)
            #self.tableView.viewport().update()
            #self.tableView.update()
class Ui_MainWindow_add_person(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 170)
        MainWindow.setMinimumSize(402, 170)
        MainWindow.setMaximumSize(402, 170)
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 21))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_FIO = QLabel(self.centralwidget)
        self.label_FIO.setObjectName(u"label_FIO")
        self.label_FIO.setGeometry(QRect(10, 60, 51, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_FIO.setFont(font1)
        self.label_FIO.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 110, 61, 31))
        self.label_password.setFont(font1)
        self.label_password.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_fio = QLineEdit(self.centralwidget)
        self.text_fio.setObjectName(u"text_fio")
        self.text_fio.setGeometry(QRect(10, 80, 201, 22))
        self.text_password = QLineEdit(self.centralwidget)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setGeometry(QRect(10, 140, 201, 22))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.pushButton.clicked.connect(self.button_add_person)

        self.pushButton.setGeometry(QRect(260, 140, 91, 21))
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
        self.label_Login = QLabel(self.centralwidget)
        self.label_Login.setObjectName(u"label_Login")
        self.label_Login.setGeometry(QRect(220, 60, 51, 21))
        self.label_Login.setFont(font1)
        self.label_Login.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.text_login = QLineEdit(self.centralwidget)
        self.text_login.setObjectName(u"text_login")
        self.text_login.setGeometry(QRect(220, 80, 161, 22))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430", None))
        self.label_FIO.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_Login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
    # retranslateUi

    def button_add_person(self):
        if not(self.text_fio.text() == "" and self.text_login.text() == "" and self.text_password.text() == ""):
            con = sqlite3.connect("Shop.db")
            cursor = con.cursor()
            cursor.execute("INSERT INTO login_Seller (login,password) VALUES (?,?)",(self.text_login.text(),
                                                                                   self.text_password.text()))
            con.commit()
            con.close()

            box_msg = QMessageBox()
            box_msg.setWindowTitle("TechSphere")
            ico = QIcon(u"ico/Shop.png")
            box_msg.setWindowIcon(ico)
            box_msg.setText("Регистрация прошла успешно")
            box_msg.exec()

        else:
            print(False)
            return False