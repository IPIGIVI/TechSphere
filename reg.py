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
from PySide6.QtSql import QSqlDatabase
def create_connectiom():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("Shop.db")
    if not db.open():
        print("Нет")
        return False
    return True
class Ui_MainWindow_registration(object):

    def connect(self):
        login = self.Text_login.text()
        password = self.Text_password.text()
        if not (login == "" or password == ""):
            conn = sqlite3.connect("Shop.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO login_Buyer (login,password) VALUES(?,?)",(login,password))
            conn.commit()
            conn.close()

            box_msg = QMessageBox()
            box_msg.setWindowTitle("TechSphere")
            ico = QIcon(u"ico/Shop.png")
            box_msg.setWindowIcon(ico)
            box_msg.setText("Регистрация прошла успешно")
            box_msg.exec()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(367, 172)
        MainWindow.setMinimumSize(QSize(367, 172))
        MainWindow.setMaximumSize(QSize(367, 172))
        icon = QIcon()
        icon.addFile(u"ico/Shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(367, 172))
        self.centralwidget.setMaximumSize(QSize(367, 172))
        self.Text_login = QLineEdit(self.centralwidget)
        self.Text_login.setObjectName(u"Text_login")
        self.Text_login.setGeometry(QRect(80, 60, 201, 22))
        self.label_3_password = QLabel(self.centralwidget)
        self.label_3_password.setObjectName(u"label_3_password")
        self.label_3_password.setGeometry(QRect(0, 100, 81, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_3_password.setFont(font)
        self.label_3_password.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.label_2_login = QLabel(self.centralwidget)
        self.label_2_login.setObjectName(u"label_2_login")
        self.label_2_login.setGeometry(QRect(0, 50, 71, 31))
        self.label_2_login.setFont(font)
        self.label_2_login.setStyleSheet(u"background-color:rgba(0,0,0,0)")
        self.Text_password = QLineEdit(self.centralwidget)
        self.Text_password.setObjectName(u"Text_password")
        self.Text_password.setGeometry(QRect(80, 110, 201, 22))
        self.Text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 181, 41))
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.regist = QPushButton(self.centralwidget)
        self.regist.setObjectName(u"regist")
        self.regist.setGeometry(QRect(110, 140, 131, 24))

        self.regist.clicked.connect(self.connect)

        self.regist.setStyleSheet(u"QPushButton {\n"
"    border-radius:4px;\n"
"	font-size:17px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:15px;\n"
"border-radius:4px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.422343 rgba(155, 79, 165, 255), stop:1 rgba( 41, 61, 132, 235));\n"
"    color: white; \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"ico/Add_acaunt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.regist.setIcon(icon1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechSphere", None))
        self.Text_login.setText("")
        self.label_3_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_2_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.regist.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0446\u0438\u044f", None))
    # retranslateUi


