import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from first_window import Ui_MainWindow,Ui_MainWindow_buy,Ui_MainWindow_payment,Ui_MainWindow_credit,Ui_MainWindow_card
from Login import Ui_MainWindow_login
from reg import Ui_MainWindow_registration
from sotrudnic import Ui_MainWindow_sorudnic,Ui_MainWindow_Add_product,Ui_MainWindow_delite,Ui_MainWindow_add_person

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.first_window = Ui_MainWindow()
        self.login_window = Ui_MainWindow_login()
        self.buyer_window = Ui_MainWindow_buy()
        self.payment_window = Ui_MainWindow_payment()
        self.credit_window = Ui_MainWindow_credit()
        self.registration_window = Ui_MainWindow_registration()
        self.sotrudnic_window = Ui_MainWindow_sorudnic()
        self.add_tovar = Ui_MainWindow_Add_product()
        self.dell = Ui_MainWindow_delite()
        self.add_person = Ui_MainWindow_add_person()
        self.card = Ui_MainWindow_card()

        self.initUI()

    def initUI(self):
        self.show_first_window()

    def show_first_window(self):
        self.first_window.setupUi(self)
        self.first_window.login.clicked.connect(self.show_login_window)
        self.first_window.basket.clicked.connect(self.show_buyer_window)
        self.first_window.registration.clicked.connect(self.show_registration_window)


    def show_login_window(self):
        self.login_window.setupUi(self)

        self.login_window.enter.clicked.connect(lambda:self.cheak_setupModel("Buyer"))
        self.login_window.pushButton.clicked.connect(lambda: self.cheak_setupModel("Seller"))

    def cheak_setupModel(self,button_name):
        setupModel = self.login_window.setupModel(button_name)

        if setupModel == True and button_name == "Buyer":
            self.show_first_window()
        elif setupModel == True and button_name == "Seller":
            self.show_sotrudnic_window()

    def show_buyer_window(self):
        self.buyer_window.setupUi(self)
        self.buyer_window.pushButton_beak.clicked.connect(self.show_first_window)
        self.buyer_window.pushButton_buy.clicked.connect(self.show_payment_window)

    def show_payment_window(self):
        self.payment_window.setupUi(self)
        self.payment_window.pushButton_3.clicked.connect(self.show_credit_window)
        self.payment_window.pushButton_2.clicked.connect(self.show_card)
        self.payment_window.pushButton.clicked.connect(self.show_first_window)

    def show_credit_window(self):
        self.credit_window.setupUi(self)
        if self.credit_window.Take_credit() == False:
            self.credit_window.pushButton.clicked.connect(self.show_first_window)

    def show_registration_window(self):
        self.registration_window.setupUi(self)
        self.registration_window.regist.clicked.connect(self.show_first_window)

    def show_sotrudnic_window(self):
        self.sotrudnic_window.setupUi(self)
        self.sotrudnic_window.add_tovar.clicked.connect(self.show_add_tovar)
        self.sotrudnic_window.del_tovar.clicked.connect(self.show_dell_tovar)
        self.sotrudnic_window.add_perdon.clicked.connect(self.show_add_person)

    def show_add_person(self):
        self.add_person.setupUi(self)
        self.add_person.pushButton.clicked.connect(self.show_first_window)



    def show_add_tovar(self):
        self.add_tovar.setupUi(self)
        self.add_tovar.Home.clicked.connect(self.show_first_window)

    def show_dell_tovar(self):
        self.dell.setupUi(self)
        self.dell.button_home.clicked.connect(self.show_first_window)
        self.dell.buttom_add.clicked.connect(self.show_add_tovar)

    def show_card(self):
        self.card.setupUi(self)
        self.card.Button_pay.clicked.connect(self.show_first_window)

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
