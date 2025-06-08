import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from BankAccount import Ui_MainWindow

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.money_in_GEL.setReadOnly(True)
        self.convert_money.clicked.connect(self.convertation)
    @staticmethod
    def attitude(money, currency):
        rates={"GEL":1.0, "USD":0.37, "EUR":0.32, "GBP":0.27, "KWD":0.11, "JPY":52.73}
        new_value = money*rates[currency]
        return f"{new_value} {currency}"

    def convertation(self):
        new_money=self.show_money.text()
        for_now=self.money_in_GEL.text().split(" ")
        new_currency=self.currency.currentText()
        if float(for_now[0])>=float(new_money):
            new_meaning=Logic.attitude(float(new_money),new_currency)
            changed_meaning=new_meaning.split(" ")
            if self.convert_check.isChecked():
                self.money_in_GEL.setText(f"{float(eval(f"{for_now[0]}-{self.show_money.text()}"))} {for_now[1]}")
                self.successed.setText("კონვერტაცია წარმატებით დასრულდა!")
                self.converted_money.setText(f"{float(eval(f"{changed_meaning[0]}+0"))}")
                self.not_GEL.setText(changed_meaning[1])
                self.unconverted_money.setText(f"{float(eval(f"{for_now[0]}-{self.show_money.text()}"))}")
                self.in_GEL.setText(for_now[1])
                self.show_money.clear()
                self.show_money.setReadOnly(True)
                self.convert_money.setEnabled(False)

            else:
                self.successed.setText("დაეთანხმეთ კონვერტაციას!")

        elif float(new_money)>float(for_now[0]):
            if self.convert_check.isChecked():
                self.show_money.clear()
                self.successed.setText("არ გაქვთ საკმარისი თანხა!")
            else:
                self.successed.setText("დაეთანხმეთ კონვერტაციას!")


        self.cashing_out.clicked.connect(self.cashing)
    def cashing(self):
        cashing_part=float(self.cashing_part.text())
        if self.cash_currency.currentText()==self.not_GEL.text():
            if float(self.converted_money.text())>=cashing_part:
                self.cash.setText(f"{cashing_part} {self.not_GEL.text()}")
                self.converted_money.setText(f"{float(eval(f"{self.converted_money.text()}-{cashing_part}"))}")
                self.cashing_part.setReadOnly(True)
                self.cashing_out.setEnabled(False)
                self.cash.setReadOnly(True)
            else:
                self.cash.setText("არ გაქვთ საკმარისი თანხა!")
        elif self.cash_currency.currentText()==self.in_GEL.text():
            if float(self.unconverted_money.text())>=cashing_part:
                renewed_balance=self.money_in_GEL.text().split(" ")
                self.cash.setText(f"{cashing_part} {self.in_GEL.text()}")
                self.unconverted_money.setText(f"{float(eval(f"{self.unconverted_money.text()}-{cashing_part}"))}")
                self.money_in_GEL.setText(f"{float(eval(f"{renewed_balance[0]}-{cashing_part}"))} {renewed_balance[1]}")
                self.cashing_part.setReadOnly(True)
                self.cashing_out.setEnabled(False)
                self.cash.setReadOnly(True)
            else:
                self.cash.setText("არ გაქვთ საკმარისი თანხა!")
                self.cash.setReadOnly(True)
        else:
            self.cash.setText("შეუსაბამო ვალუტა!")
            self.cash.setReadOnly(True)




app = QApplication(sys.argv)
window = Logic()
window.show()
sys.exit(app.exec())