# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_personal.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 170)
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

