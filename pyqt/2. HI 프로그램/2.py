from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_MainWindow
import sys

# qt 설정
# =========================================================================================================================================
class MainWindow(QMainWindow):
#########################################################################
# UI 설정 불러오기
#########################################################################
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)
#########################################################################

# UI 버튼 클릭 시 동작 코드
# =========================================================================================================================================
    def click(self):
#########################################################################
# 클릭 후 메시지 박스 표시
#########################################################################
        self.ui.btn_hi.setText("인사했어요")
        print("클릭 되었습니다.")
        mb_hi = QMessageBox()
        mb_hi.setText("hello")
        mb_hi.exec()
#########################################################################

#########################################################################
# 퀴즈 메시지 박스 표시 및 정답 선택
#########################################################################
        mb_quiz = QMessageBox()
        mb_quiz.setText("1+1 ?")
        btn_answer_2 = mb_quiz.addButton("2", QMessageBox.ActionRole)
        btn_answer_3 = mb_quiz.addButton("3", QMessageBox.ActionRole) 
        # mb_quiz.addButton("no role", QMessageBox.NoRole) # no 와 action role이 같이 있을 경우 no role이 왼쪽으로 자동적으로 생성됨
        mb_quiz.exec()
        
        if mb_quiz.clickedButton() == btn_answer_2:
            # print("정답")
            mb_success = QMessageBox()
            mb_success.setText("정답입니다.")
            mb_success.exec()
        elif mb_quiz.clickedButton() == btn_answer_3:
            # print("오답")
            mb_fail = QMessageBox()
            mb_fail.setText("오답입니다.")
            mb_fail.exec()
#########################################################################
# =========================================================================================================================================
# =========================================================================================================================================
if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
