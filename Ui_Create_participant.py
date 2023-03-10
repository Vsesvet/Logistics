from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from Class_Mysql import*
from db_config import host, port, password, db_name, user
import generator_password

class Ui_Create_participant(QDialog):
    def __init__(self):
        super(Ui_Create_participant, self).__init__()
        self.setObjectName("Create_participant")
        self.resize(431, 368)
        self.label_username_role = QtWidgets.QLabel(self)
        self.label_username_role.setGeometry(QtCore.QRect(130, 0, 301, 20))
        self.label_username_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_role.setObjectName("label_username_role")
        self.lineEdit_second_name = QtWidgets.QLineEdit(self)
        self.lineEdit_second_name.setGeometry(QtCore.QRect(10, 100, 131, 25))
        self.lineEdit_second_name.setObjectName("lineEdit_second_name")
        self.lineEdit_email = QtWidgets.QLineEdit(self)
        self.lineEdit_email.setGeometry(QtCore.QRect(10, 140, 131, 25))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_last_name = QtWidgets.QLineEdit(self)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(290, 100, 131, 25))
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setGeometry(QtCore.QRect(10, 180, 131, 25))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_generate = QtWidgets.QPushButton(self)
        self.pushButton_generate.setGeometry(QtCore.QRect(150, 180, 131, 25))
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.checkBox_disabled_participant = QtWidgets.QCheckBox(self)
        self.checkBox_disabled_participant.setGeometry(QtCore.QRect(10, 300, 221, 23))
        self.checkBox_disabled_participant.setObjectName("checkBox_disabled_participant")
        self.label_create_participant = QtWidgets.QLabel(self)
        self.label_create_participant.setGeometry(QtCore.QRect(120, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_participant.setFont(font)
        self.label_create_participant.setObjectName("label_create_participant")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(self)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(150, 60, 131, 25))
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.lineEdit_first_name = QtWidgets.QLineEdit(self)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(150, 100, 131, 25))
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.setGeometry(QtCore.QRect(330, 330, 89, 25))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancel = QtWidgets.QPushButton(self)
        self.pushButton_cancel.setGeometry(QtCore.QRect(230, 330, 89, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit_city = QtWidgets.QLineEdit(self)
        self.lineEdit_city.setGeometry(QtCore.QRect(150, 140, 131, 25))
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.lineEdit_comment = QtWidgets.QLineEdit(self)
        self.lineEdit_comment.setGeometry(QtCore.QRect(10, 220, 411, 25))
        self.lineEdit_comment.setObjectName("lineEdit_comment")

        self.retranslateUi(self)
        # ?????????????? ???? ????????????
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.create_participant)
        self.pushButton_cancel.clicked.connect(self.close)
        self.checkBox_disabled_participant.stateChanged['int'].connect(self.show)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setTabOrder(self.lineEdit_phone_number, self.lineEdit_second_name)
        self.setTabOrder(self.lineEdit_second_name, self.lineEdit_first_name)
        self.setTabOrder(self.lineEdit_first_name, self.lineEdit_last_name)
        self.setTabOrder(self.lineEdit_last_name, self.lineEdit_email)
        self.setTabOrder(self.lineEdit_email, self.lineEdit_city)
        self.setTabOrder(self.lineEdit_city, self.lineEdit_password)
        self.setTabOrder(self.lineEdit_password, self.pushButton_generate)
        self.setTabOrder(self.pushButton_generate, self.lineEdit_comment)
        self.setTabOrder(self.lineEdit_comment, self.checkBox_disabled_participant)
        self.setTabOrder(self.checkBox_disabled_participant, self.pushButton_cancel)
        self.setTabOrder(self.pushButton_cancel, self.pushButton_save)
        self.setTabOrder(self.pushButton_save, self.lineEdit_phone_number)

        self.db = Mysql(host, port, user, password, db_name)


    def retranslateUi(self, Create_participant):
        _translate = QtCore.QCoreApplication.translate
        Create_participant.setWindowTitle(_translate("Create_participant", "????????????????  (update 23.02)"))
        self.label_username_role.setText(_translate("Create_participant", "???????????? ?????????? (??????????????????????????)"))
        self.lineEdit_second_name.setPlaceholderText(_translate("Create_participant", "??????????????..."))
        self.lineEdit_email.setPlaceholderText(_translate("Create_participant", "e-mail..."))
        self.lineEdit_last_name.setPlaceholderText(_translate("Create_participant", "????????????????..."))
        self.lineEdit_password.setPlaceholderText(_translate("Create_participant", "????????????..."))
        self.pushButton_generate.setText(_translate("Create_participant", "??????????????????????????"))
        self.checkBox_disabled_participant.setText(_translate("Create_participant", "?????????????????? ?????????????? ????????????"))
        self.label_create_participant.setText(_translate("Create_participant", "???????????????? ??????????????????"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Create_participant", "79265001020"))
        self.lineEdit_first_name.setPlaceholderText(_translate("Create_participant", "??????..."))
        self.pushButton_save.setText(_translate("Create_participant", "??????????????????"))
        self.pushButton_cancel.setText(_translate("Create_participant", "????????????"))
        self.lineEdit_city.setPlaceholderText(_translate("Create_participant", "??????????..."))
        self.lineEdit_comment.setPlaceholderText(_translate("Create_participant", "??????????????????????..."))
        self.move_to_center()

    def move_to_center(self):
        desktop = QApplication.desktop()
        desktop.screenGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

    def create_participant(self):
        phone_number = self.lineEdit_phone_number.text()
        second_name = self.lineEdit_second_name.text()
        first_name = self.lineEdit_first_name.text()
        last_name = self.lineEdit_last_name.text()
        email = self.lineEdit_email.text()
        city = self.lineEdit_city.text()
        password = self.lineEdit_password.text()
        comment = self.lineEdit_comment.text()
        disabled = self.checkBox_disabled_participant.isChecked()

        role = "participant"
        full_name = second_name + " " + first_name +" " + last_name
        if len(phone_number) == 11:
            self.db.add_participant(phone_number, second_name, first_name, last_name, role, full_name, email, city, password, comment, disabled)
            self.close()
        else:
            self.lineEdit_phone_number.setPlaceholderText("?????????????? ?????????? ????????????????")


    def generate_password(self):
        passw = generator_password.generate()
        self.lineEdit_password.setText(f'{passw}')