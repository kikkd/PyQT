from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTimer
from ui import Ui_MainWindow
import datetime
import sys

orders = [
    {"menu":"에스프레소 L", "quantity":"10", "oder_amount":"10000", "time":"2022-07-22 09:14", "status":"waiting"},
    {"menu":"라떼 S", "quantity":"10", "oder_amount":"10000", "time":"2022-07-22 09:14", "status":"waiting"},
    {"menu":"아메리카노 M", "quantity":"10", "oder_amount":"10000", "time":"2022-07-22 09:14", "status":"processing"},
    {"menu":"에스프레소 S", "quantity":"10", "oder_amount":"10000", "time":"2022-07-22 09:14", "status":"delivery"},
    {"menu":"에스프레소 M", "quantity":"10", "oder_amount":"10000", "time":"2022-07-22 09:14", "status":"done"},
]

menu_widgets=[
    "radio_espresso",
    "radio_americano",
    "radio_latte",
    "radio_mocha",
    "radio_choco_smoothie",
    "radio_strawberry_smoothie",
]

size_widgets=[
    "radio_size_s",
    "radio_size_m",
    "radio_size_l",
    "radio_size_xl",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(990)
        self.timer.timeout.connect(self.tick)
        self.timer.start()

        self.load()
        
        for w in menu_widgets + size_widgets:
            widget = getattr(self.ui,w)
            widget.clicked.connect(self.calc)
        
        self.calc()

    def tick(self):
        now = datetime.datetime.now()
        self.ui.lb_now.setText(f"현재 시각 : {now}")
    
    def load(self):
        for d in orders:
            r = self.ui.table_orders.rowCount()
            self.ui.table_orders.insertRow(r)
            self.ui.table_orders.setItem(r,0,QTableWidgetItem(d["menu"]))
            self.ui.table_orders.setItem(r,1,QTableWidgetItem(d["quantity"]))
            self.ui.table_orders.setItem(r,2,QTableWidgetItem(d["oder_amount"]))
            self.ui.table_orders.setItem(r,3,QTableWidgetItem(d["time"]))
            self.ui.table_orders.setItem(r,4,QTableWidgetItem(d["status"]))

        # lcd 주문 현황 업데이트
        self.ui.lcd_num_of_orders.display(len(orders))
        waiting = [x for x in orders if x["status"]=="waiting"]
        self.ui.lcd_num_of_orders_waiting.display(len(waiting))
        processing = [x for x in orders if x["status"]=="processing"]
        self.ui.lcd_num_of_orders_processing.display(len(processing))
        delivery = [x for x in orders if x["status"]=="delivery"]
        self.ui.lcd_num_of_orders_delivery.display(len(delivery))
        done = [x for x in orders if x["status"]=="done"]
        self.ui.lcd_num_of_orders_done.display(len(done))
        
    def calc(self):
        menu_price = {
            "에스프레소" : 1000,
            "아메리카노" : 1500,
            "라떼" : 3000,
            "모카" : 3500,
            "초코 스무디" : 5500,
            "딸기 스무디" : 5500,
        }
        size_price = {
            "S" : 0,
            "M" : 500,
            "L" : 1000,
            "XL" : 1500,
        }

        price = 0
        for w in menu_widgets:
            menu = getattr(self.ui, w)
            # menu = self.ui.radio_espresso
            # menu = self.ui.radio_americano
            if menu.isChecked():
                price = menu_price[menu.text()]
                break

        for w in size_widgets:
            size = getattr(self.ui, w)
            if size.isChecked():
                price += size_price[size.text()]
                break
        
        quantity = self.ui.spin_quantity.value()
        price = price * quantity

        self.ui.lb_order_amount.setText(f"총 주문 금액 : {price}원")
        
        return price


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())