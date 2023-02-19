import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_Login(QWidget):
    def __init__(self):
        super(Ui_Login, self).__init__()
        self.setObjectName("Login")
        self.resize(365, 215)
        self.pushButton_login = QtWidgets.QPushButton(self)
        self.pushButton_login.setGeometry(QtCore.QRect(140, 180, 89, 25))
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_main_input = QtWidgets.QLabel(self)
        self.label_main_input.setGeometry(QtCore.QRect(130, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_main_input.setFont(font)
        self.label_main_input.setObjectName("label_main_input")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 50, 241, 104))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.label_bad_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_bad_password.setText("")
        self.label_bad_password.setObjectName("label_bad_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_bad_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_password)
        self.lineEdit_login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_login)
        self.label_login = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_login.setObjectName("label_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_login)
        self.label_user_not_found = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_user_not_found.setText("")
        self.label_user_not_found.setObjectName("label_user_not_found")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_user_not_found)

        self.retranslateUi(self)
        self.pushButton_login.clicked.connect(self.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Вход в программу"))
        self.pushButton_login.setText(_translate("Login", "Войти"))
        self.label_main_input.setText(_translate("Login", "Логистик"))
        self.label_password.setText(_translate("Login", "Пароль"))
        self.lineEdit_login.setPlaceholderText(_translate("Login", "79265002010"))
        self.label_login.setText(_translate("Login", "Логин"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_login = Ui_Login()
    win_login.show()
    sys.exit(app.exec())