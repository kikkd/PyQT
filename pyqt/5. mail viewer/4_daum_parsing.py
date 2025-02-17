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

N_ID = " "
N_PW = " "
D_ID = " "
D_PW = " " 
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
        pyperclip.copy(N_ID)
        time.sleep(1)
        input_id.click()
        input_id.send_keys(Keys.CONTROL, "v")
        
        pyperclip.copy(N_PW)
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

        chrome.get("""https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fmail.daum.net%252F""")
        input_did = find(chrome,"div.item_tf input#id_email_2")
        input_dpw = find(chrome,"#id_password_3")
        pyperclip.copy(D_ID)
        time.sleep(1)
        #input_did.click()
        input_did.send_keys(Keys.ENTER)
        time.sleep(1)
        input_did.send_keys(Keys.CONTROL,'v')
        time.sleep(0.5)

        pyperclip.copy(D_PW)
        time.sleep(1)
        # input_dpw.click()
        input_dpw.send_keys(Keys.ENTER)
        time.sleep(0.5)
        input_dpw.send_keys(Keys.CONTROL, "v")
        time.sleep(0.5)
        input_dpw.send_keys(Keys.ENTER)
        # input_pw.send_keys("\n")
        time.sleep(1)

        chrome.get("https://mail.daum.net/")

        for m in find_all(chrome, "ul.list_mail li.mail_item"):
            date = m.find_element(By.CSS_SELECTOR, ".txt_date").text
            site = "다음"
            sender = m.find_element(By.CSS_SELECTOR,".info_from a").text
            try:
                m.find_element(By.CSS_SELECTOR,"span.img_mail.ico_file")
                attached = True
            except:
                attached = False
            title = m.find_element(By.CSS_SELECTOR,"strong.tit_subject").text

            ##########################################################################33
            now = datetime.datetime.now()
            if len(date) < 6:
                date = f"{now.strftime('%y')}.{now.month}.{now.day} {date}"
            # date = datetime.datetime.strptime(date,"%Y.%m.%d %H:%M")
            date = f"{date}"
            date = datetime.datetime.strptime(date.strip(),"%y.%m.%d %H:%M")
            ###################################################################################3
            link = m.find_element(By.CSS_SELECTOR,".info_subject a.link_window").get_attribute("href")

            mails.append({
                "date" : date,
                "site" : site,
                "sender" : sender,
                "attached" : attached,
                "title" : title,
                "link" : link,
            })


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
        if mail["site"] == "네이버":
            content = find(self.chrome, "#readFrame").text
        elif mail["site"] == "다음":
            content = find(self.chrome, "div.txt_mailview").text
        self.ui.lb_title.setText(mail["title"])
        self.ui.lb_content.setText(content)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


