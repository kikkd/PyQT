from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_MainWindow
from PySide6.QtCore import QTimer
import sys
import random

class MainWindow(QMainWindow):
    last_read = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_send.clicked.connect(self.send)
        self.ui.edit_text.returnPressed.connect(self.send)

        # 닉네임 랜덤 자동 생성
        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)
        
        # 환엽합니다 메시지
        with open ("./server.txt", "a+", encoding="utf-8") as f:
            f.writelines(f"--------{nickname}님이 입장 하셨습니다.\n")

        self.listen()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.listen)
        self.timer.start()

    def send (self):
        nickname = self.ui.edit_nickname.text()
        text = self.ui.edit_text.text()
        # self.ui.list_chat.addItem(f"{nickname} : {text}")
        msg = f"{nickname} : {text}"

        # 파일에다가 msg를 씀
        with open ("./server.txt","a+", encoding="utf-8") as f:
            f.writelines(msg+"\n")
        
        self.ui.edit_text.clear()
        # # file 읽어오기
        # self.listen()

    def random_nickname(self):
        nickname = random.choice(["프로도","박보검","아이유"])
        num = random.randint(1,1000)
        return f"{nickname}{num}"

    def listen(self):
        try:
            with open ("./server.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            self.ui.list_chat.addItems(lines[self.last_read:])
            self.last_read = len(lines)
            self.ui.list_chat.scrollToBottom()
        except:
            pass

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())