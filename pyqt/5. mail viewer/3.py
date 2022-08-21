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
def find_all(chrome,css):
    find(chrome,css)
    return chrome.find_elements(By.CSS_SELECTOR,css)

ID = " "
PW = " "

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # seleniu up
        chrome = webdriver.Chrome("./chromedriver.exe")
        # log in
        chrome.get("https://mail.naver.com")
        input_id = find(chrome,"#id")
        input_pw = find(chrome,"#pw")
        pyperclip.copy(ID)
        time.sleep(1)
        input_id.click()
        input_id.send_keys(Keys.CONTROL, "v")
        
        pyperclip.copy(PW)
        time.sleep(1)
        input_pw.click()
        input_pw.send_keys(Keys.CONTROL, "v")
        time.sleep(0.5)
        input_pw.send_keys("\n")
        time.sleep(0.5)
        
        for mail in find_all(chrome, "ol.mailList > li"):
            date = mail.find_element(By.CSS_SELECTOR,"li.iDate").text
            # date = datetime.datetime.strptime(date)
            #11:02
            #08-18 21:08
            now = datetime.datetime.now()

            if len(date) < 6:
                date = f"{now.month}-{now.day} {date}"
            date = f"{now.year}-{date}"
            date = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M")

            print(date)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

