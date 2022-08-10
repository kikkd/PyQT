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
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_hi = QPushButton(self.centralwidget)
        self.btn_hi.setObjectName(u"btn_hi")
        self.btn_hi.setGeometry(QRect(270, 200, 75, 24))
        self.radio_1 = QRadioButton(self.centralwidget)
        self.radio_1.setObjectName(u"radio_1")
        self.radio_1.setGeometry(QRect(220, 150, 89, 20))
        self.radio_2 = QRadioButton(self.centralwidget)
        self.radio_2.setObjectName(u"radio_2")
        self.radio_2.setGeometry(QRect(330, 150, 89, 20))
        self.chk_1 = QCheckBox(self.centralwidget)
        self.chk_1.setObjectName(u"chk_1")
        self.chk_1.setGeometry(QRect(170, 250, 76, 20))
        self.chk_2 = QCheckBox(self.centralwidget)
        self.chk_2.setObjectName(u"chk_2")
        self.chk_2.setGeometry(QRect(270, 250, 76, 20))
        self.chk_3 = QCheckBox(self.centralwidget)
        self.chk_3.setObjectName(u"chk_3")
        self.chk_3.setGeometry(QRect(380, 250, 76, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_hi.setText(QCoreApplication.translate("MainWindow", u"Hi", None))
        self.radio_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radio_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.chk_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

