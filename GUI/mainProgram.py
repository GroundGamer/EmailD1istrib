import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.ui1 import Ui_widget
from GUI.GUI_A import Ui_Form

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
ui = Ui_widget()
ui.setupUi(widget)

Form = QtWidgets.QWidget()
ui1 = Ui_Form()
ui1.setupUi(Form)

widget.show()

ui.pushButton.clicked.connect(Form.show)
ui.pushButton.clicked.connect(widget.close)

# Выход из программы
sys.exit(app.exec_())

# def getEmail():
#     email = list_email.pop(0)
#     print(email)
#     return email
#
#
# def getPassword():
#     password = list_password.pop(0)
#     print(password)
#     return password
# ui1.pushButton.clicked.connect(getEmail)
# ui1.pushButton.clicked.connect(getPassword)
# def getFormUiFormInfo():
#     list_email = []
#     list_password = []
#     for x in ui1.onClickToGetInformationFromLE_Email():
#         list_email.append(x)
#
#     for x in ui1.onClickToGetInformationFromLE_Password():
#         list_password.append(x)
#
#     email = list_email.pop(0)
#     password = list_password.pop(0)
