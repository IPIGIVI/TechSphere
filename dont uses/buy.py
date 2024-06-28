# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buy.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 174)
        MainWindow.setMinimumSize(QSize(543, 174))
        MainWindow.setMaximumSize(QSize(543, 174))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
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
        icon1 = QIcon()
        icon1.addFile(u"ico/Add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setIconSize(QSize(25, 25))
        self.pushButton_add_2 = QPushButton(self.centralwidget)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setGeometry(QRect(80, 110, 61, 31))
        self.pushButton_add_2.setFont(font)
        self.pushButton_add_2.setStyleSheet(u"background-color:rgba(0,0,0,0)")
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
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_quantity.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.pushButton_buy.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430:", None))
        self.text_name.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.text_price.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.text_kol.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.pushButton_add.setText("")
        self.pushButton_add_2.setText("")
        self.pushButton_beak.setText("")
    # retranslateUi

