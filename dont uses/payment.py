# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
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

