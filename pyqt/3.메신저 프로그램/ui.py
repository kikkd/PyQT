# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 413)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_chat = QListWidget(self.centralwidget)
        self.list_chat.setObjectName(u"list_chat")
        self.list_chat.setGeometry(QRect(2, 2, 341, 341))
        self.edit_nickname = QLineEdit(self.centralwidget)
        self.edit_nickname.setObjectName(u"edit_nickname")
        self.edit_nickname.setGeometry(QRect(10, 350, 71, 22))
        self.edit_text = QLineEdit(self.centralwidget)
        self.edit_text.setObjectName(u"edit_text")
        self.edit_text.setGeometry(QRect(83, 350, 180, 22))
        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(265, 349, 70, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uba54\uc2e0\uc800", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc1a1", None))
    # retranslateUi

