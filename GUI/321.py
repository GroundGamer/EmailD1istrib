from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1060, 842)
        Form.setMinimumSize(QtCore.QSize(1060, 842))
        Form.setMaximumSize(QtCore.QSize(1060, 842))
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(-120, -50, 1201, 901))
        self.Background.setStyleSheet("background-image: url(:/newPrefix/background.png);")
        self.Background.setText("")
        self.Background.setObjectName("Background")

        self.Login = QtWidgets.QLineEdit(Form)
        self.Login.setGeometry(QtCore.QRect(400, 170, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setStyleSheet("QLineEdit{\n"
"\n"
"background-color: rgb(106, 90, 167);\n"
"border:4px solid #EDA560;\n"
"color:#FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"\n"
"}")
        self.Login.setMaxLength(35)
        self.Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Login.setObjectName("Login")
        self.Password = QtWidgets.QLineEdit(Form)
        self.Password.setGeometry(QtCore.QRect(400, 230, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setStyleSheet("QLineEdit{\n"
"\n"
"background-color: rgb(106, 90, 167);\n"
"border:4px solid #EDA560;\n"
"color:#FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"\n"
"}")
        self.Password.setMaxLength(30)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 580, 200, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"color:#6A5AA7;\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(249, 182, 119);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(106, 90, 167);\n"
"color:#FFBB7A;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(400, 510, 300, 50))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color: rgb(106, 90, 167);\n"
"color:#FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"border:none;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(445, 575, 209, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Button.png"))
        self.label.setObjectName("label")
        self.LineEdit2 = QtWidgets.QLineEdit(Form)
        self.LineEdit2.setGeometry(QtCore.QRect(400, 290, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit2.sizePolicy().hasHeightForWidth())
        self.LineEdit2.setSizePolicy(sizePolicy)
        self.LineEdit2.setStyleSheet("QLineEdit{\n"
"\n"
"background-color: rgb(106, 90, 167);\n"
"border:4px solid white;\n"
"color:#FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"\n"
"}")
        self.LineEdit2.setMaxLength(30)
        self.LineEdit2.setAlignment(QtCore.Qt.AlignCenter)
        self.LineEdit2.setObjectName("LineEdit2")
        self.EmailLabel = QtWidgets.QLabel(Form)
        self.EmailLabel.setGeometry(QtCore.QRect(523, 184, 61, 21))
        self.EmailLabel.setStyleSheet("QLabel{\n"
"\n"
"color:#e2e2e2;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover {\n"
"\n"
"}")
        self.EmailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.LineEdit3 = QtWidgets.QTextEdit(Form)
        self.LineEdit3.setGeometry(QtCore.QRect(400, 350, 300, 150))
        self.LineEdit3.setStyleSheet("QTextEdit{\n"
"\n"
"background-color: rgb(106, 90, 167);\n"
"border:4px solid white;\n"
"color:#FFBB7A;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"\n"
"\n"
"}")
        self.LineEdit3.setObjectName("LineEdit3")
        self.PasswordLabel = QtWidgets.QLabel(Form)
        self.PasswordLabel.setGeometry(QtCore.QRect(495, 244, 111, 21))
        self.PasswordLabel.setStyleSheet("QLabel{\n"
"\n"
"color:#e2e2e2;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover {\n"
"\n"
"}")
        self.PasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.SubjectLabel = QtWidgets.QLabel(Form)
        self.SubjectLabel.setGeometry(QtCore.QRect(510, 303, 79, 21))
        self.SubjectLabel.setStyleSheet("QLabel{\n"
"\n"
"color:#e2e2e2;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover {\n"
"\n"
"}")
        self.SubjectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SubjectLabel.setObjectName("SubjectLabel")
        self.SubjectLabel_2 = QtWidgets.QLabel(Form)
        self.SubjectLabel_2.setGeometry(QtCore.QRect(512, 410, 71, 21))
        self.SubjectLabel_2.setStyleSheet("QLabel{\n"
"\n"
"color:#e2e2e2;\n"
"font-family: Panton;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover {\n"
"\n"
"}")
        self.SubjectLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SubjectLabel_2.setObjectName("SubjectLabel_2")
        self.Background.raise_()
        self.label.raise_()
        self.Login.raise_()
        self.Password.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.LineEdit2.raise_()
        self.EmailLabel.raise_()
        self.LineEdit3.raise_()
        self.PasswordLabel.raise_()
        self.SubjectLabel.raise_()
        self.SubjectLabel_2.raise_()

        self.retranslateUi(Form)
        self.Login.textEdited['QString'].connect(self.EmailLabel.hide)
        self.Password.textEdited['QString'].connect(self.PasswordLabel.hide)
        self.LineEdit2.textEdited['QString'].connect(self.SubjectLabel.hide)
        self.LineEdit3.textChanged.connect(self.SubjectLabel_2.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.comboBox.setItemText(0, _translate("Form", "Mail.ru"))
        self.comboBox.setItemText(1, _translate("Form", "Yandex.ru"))
        self.EmailLabel.setText(_translate("Form", "EMAIL"))
        self.PasswordLabel.setText(_translate("Form", "PASSWORD"))
        self.SubjectLabel.setText(_translate("Form", "SUBJECT"))
        self.SubjectLabel_2.setText(_translate("Form", "TEXT"))
import GUIprogram_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
