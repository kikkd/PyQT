import datetime
import time
import sys

#pip install pySide6
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTimer
from ui import Ui_MainWindow

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# pip install pyperclip
import pyperclip

def find(chrome,css):
    wait = WebDriverWait(chrome, 5)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    # seleniu up
    chrome = webdriver.Chrome("./chromedriver.exe")
    # log in
    chrome.get("https://mail.naver.com")

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

