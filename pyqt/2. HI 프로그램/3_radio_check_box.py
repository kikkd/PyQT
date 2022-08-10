from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)

    def click(self):       
        self.ui.chk_1.setChecked(True)
        self.ui.chk_2.setChecked(True)
        self.ui.chk_3.setChecked(True)

        if self.ui.radio_1.isChecked():
            self.ui.radio_2.setChecked(True)
        elif self.ui.radio_2.isChecked():
            self.ui.radio_1.setChecked(True)
        else:
            self.ui.radio_1.setChecked(True)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
