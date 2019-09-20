from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from GUI.Test.GUI_test import Ui_Form

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def getFormUiFormInfo():
    print(ui.onClickToGetInformationFromLE())


ui.pushButton.clicked.connect(getFormUiFormInfo)

sys.exit(app.exec_())
