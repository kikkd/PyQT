from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui1 import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.model = QStandardItemModel()
        self.ui.list_chat.setModel(self.model)
        
        self.ui.btn_send.clicked.connect(self.send)
    
    def send (self):
        # mb = QMessageBox()
        # mb.setText(self.ui.edit_text.text())
        # mb.exec()
        text = self.ui.edit_text.text()
        item = QStandardItem(text)
        self.model.appendRow(item)


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())