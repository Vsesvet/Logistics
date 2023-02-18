from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_Create_org(QDialog):
    def __init__(self):
        super(Ui_Create_org, self).__init__()
        self.setObjectName("Dialog_org")
        self.resize(485, 191)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(290, 150, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_create_organization = QtWidgets.QLabel(self)
        self.label_create_organization.setGeometry(QtCore.QRect(100, 30, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_organization.setFont(font)
        self.label_create_organization.setObjectName("label_create_organization")
        self.label_username_role = QtWidgets.QLabel(self)
        self.label_username_role.setGeometry(QtCore.QRect(210, 0, 271, 20))
        self.label_username_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_role.setObjectName("label_username_role")
        self.lineEdit_organization_name = QtWidgets.QLineEdit(self)
        self.lineEdit_organization_name.setGeometry(QtCore.QRect(10, 70, 461, 25))
        self.lineEdit_organization_name.setText("")
        self.lineEdit_organization_name.setObjectName("lineEdit_organization_name")
        self.lineEdit_organization_inn = QtWidgets.QLineEdit(self)
        self.lineEdit_organization_inn.setGeometry(QtCore.QRect(10, 110, 141, 25))
        self.lineEdit_organization_inn.setObjectName("lineEdit_organization_inn")
        self.lineEdit_organization_kpp = QtWidgets.QLineEdit(self)
        self.lineEdit_organization_kpp.setGeometry(QtCore.QRect(170, 110, 141, 25))
        self.lineEdit_organization_kpp.setObjectName("lineEdit_organization_kpp")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(self)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(330, 110, 141, 25))
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")

        self.retranslateUi(self)
        # Нажатия на кнопки
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog_org):
        _translate = QtCore.QCoreApplication.translate
        Dialog_org.setWindowTitle(_translate("Dialog_org", "Логистик  (update 23.02)"))
        self.label_create_organization.setText(_translate("Dialog_org", "Создание новой организации"))
        self.label_username_role.setText(_translate("Dialog_org", "Фомина Ирина (Администратор)"))
        self.lineEdit_organization_name.setPlaceholderText(_translate("Dialog_org", "Наименование организации..."))
        self.lineEdit_organization_inn.setPlaceholderText(_translate("Dialog_org", "ИНН"))
        self.lineEdit_organization_kpp.setPlaceholderText(_translate("Dialog_org", "КПП"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Dialog_org", "Телефон..."))
        self.move_to_center()

    def move_to_center(self):
        desktop = QApplication.desktop()
        desktop.screenGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)