# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_produkt.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 217)
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

