# -*- coding: utf-8 -*-
import sqlite3

################################################################################
## Form generated from reading UI file 'Log.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow_login(object):
    def setupModel(self,button_name):
        login = self.Text_login.text()
        password = self.Text_password.text()

        conn = sqlite3.connect("Shop.db")
        cursor = conn.cursor()

        if button_name == "Buyer":
            cursor.execute("SELECT * FROM login_Buyer WHERE Login = ? and Password = ?", (login,password))

        elif button_name == "Seller":
            cursor.execute("SELECT * FROM login_Seller WHERE Login = ? and Password = ?",(login,password))

        select1 = cursor.fetchone()
        conn.close()

        if select1 is not None:
            return True
        else:
            self.Text_login.setText("")
            self.Text_password.setText("")



    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(367, 417)
        MainWindow.setMinimumSize(QSize(367, 417))
        MainWindow.setMaximumSize(QSize(367, 417))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.enter = QPushButton(self.centralwidget)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(140, 230, 75, 24))

        self.enter.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 71, 41))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2_login = QLabel(self.centralwidget)
        self.label_2_login.setObjectName(u"label_2_login")
        self.label_2_login.setGeometry(QRect(70, 80, 71, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2_login.setFont(font1)
        self.label_2_login.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_3_password = QLabel(self.centralwidget)
        self.label_3_password.setObjectName(u"label_3_password")
        self.label_3_password.setGeometry(QRect(70, 160, 81, 31))
        self.label_3_password.setFont(font1)
        self.label_3_password.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.Text_login = QLineEdit(self.centralwidget)
        self.Text_login.setObjectName(u"Text_login")
        self.Text_login.setGeometry(QRect(70, 110, 201, 22))
        self.Text_password = QLineEdit(self.centralwidget)
        self.Text_password.setObjectName(u"Text_password")
        self.Text_password.setGeometry(QRect(70, 190, 201, 22))
        self.Text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 390, 101, 24))


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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.enter.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label_2_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.Text_login.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
    # retranslateUi

