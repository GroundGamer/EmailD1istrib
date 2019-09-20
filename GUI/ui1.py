from PyQt5 import QtCore, QtGui, QtWidgets
import sourceIMG_rc
import sys


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1060, 842)
        widget.setMinimumSize(QtCore.QSize(1060, 842))
        widget.setMaximumSize(QtCore.QSize(1060, 842))
        widget.setStyleSheet("")
        self.label1 = QtWidgets.QLabel(widget)
        self.label1.setGeometry(QtCore.QRect(-30, -10, 1101, 871))
        self.label1.setStyleSheet("QLabel{\n"
                                  "background-image: url(:/Isxod/background.png);\n"
                                  "}")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(230, 50, 614, 415))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Isxod/Result.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(384, 693, 321, 64))
        font = QtGui.QFont()
        font.setFamily("Panton Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(255, 187, 122);\n"
                                      "border: none;\n"
                                      "text-align:center;\n"
                                      "color: #6A5AA7;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(249, 182, 119);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: rgb(106, 90, 167);\n"
                                      "color:#FFBB7A;\n"
                                      "}\n"
                                      "")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(380, 690, 328, 70))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Isxod/Button.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label1.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)


    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Distribution"))
        self.pushButton.setText(_translate("widget", "НАЧАТЬ"))
