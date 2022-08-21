import datetime
import time
import sys

#pip install pySide6
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTimer
from PySide6 import QtWidgets
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

mails = []
# daum_mails = []

ID = "whddls6666"
PW = "dasom1036!d"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # seleniu up
        chrome = webdriver.Chrome("./chromedriver.exe")
        self.chrome = chrome
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

            site = "네이버"
            sender = mail.find_element(By.CSS_SELECTOR,".mTitle .name a").text
            try:
                mail.find_element(By.CSS_SELECTOR,"li.file span.spr:not([title=\"\"])")
                attached = True
            except:
                attached = False
            # attached = mail.find_element(By.CSS_SELECTOR,"li.file span span.blind").text
            title = mail.find_element(By.CSS_SELECTOR,"strong.mail_title").text
            link = mail.find_element(By.CSS_SELECTOR,"div.subject > a").get_attribute("href")
            mails.append({
                "date" : date,
                "site" : site,
                "sender" : sender,
                "attached" : attached,
                "title" : title,
                "link" : link,
            })
            # print(sender)
            # print(attached)
            # print(date)
            # print(title)
        # print(mails)

        # table_show
        self.ui.table.horizontalHeader().setSectionResizeMode(4,QtWidgets.QHeaderView.ResizeToContents)
        self.ui.table.setRowCount(len(mails))
        for r, m in enumerate(mails):
            self.ui.table.setItem(r,0,QTableWidgetItem(str(m["date"])))
            self.ui.table.setItem(r,1,QTableWidgetItem(m["site"]))
            self.ui.table.setItem(r,2,QTableWidgetItem(m["sender"]))
            self.ui.table.setItem(r,3,QTableWidgetItem(str(m["attached"])))
            self.ui.table.setItem(r,4,QTableWidgetItem(m["title"]))
            #self.ui.table.setItem(r,5,m["link"])

        self.ui.table.cellDoubleClicked.connect(self.opne_mail)
    
    def opne_mail(self, r, c):
        mail = mails[r]
        link = mail["link"]

        self.chrome.get(link)
        content = find(self.chrome, "#readFrame").text

        self.ui.lb_title.setText(mail["title"])
        self.ui.lb_content.setText(content)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

