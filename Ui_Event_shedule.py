import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Ui_Event_shedule(QMainWindow):
    def __init__(self):
        super(Ui_Event_shedule, self).__init__()
        self.setObjectName("Event_shedule")
        self.resize(1079, 600)
        self.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_create_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_event.setGeometry(QtCore.QRect(20, 90, 171, 25))
        self.pushButton_create_event.setObjectName("pushButton_create_event")
        self.pushButton_create_organization = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_organization.setGeometry(QtCore.QRect(210, 90, 171, 25))
        self.pushButton_create_organization.setObjectName("pushButton_create_organization")
        self.pushButton_create_member = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_member.setGeometry(QtCore.QRect(20, 130, 171, 25))
        self.pushButton_create_member.setObjectName("pushButton_create_member")
        self.label_username_role = QtWidgets.QLabel(self.centralwidget)
        self.label_username_role.setGeometry(QtCore.QRect(750, 0, 321, 20))
        self.label_username_role.setText("")
        self.label_username_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_role.setObjectName("label_username_role")
        self.label_event_shedule = QtWidgets.QLabel(self.centralwidget)
        self.label_event_shedule.setGeometry(QtCore.QRect(380, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_event_shedule.setFont(font)
        self.label_event_shedule.setObjectName("label_event_shedule")
        self.tree_event_shedule = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_event_shedule.setGeometry(QtCore.QRect(10, 180, 1061, 221))
        self.tree_event_shedule.setObjectName("tree_event_shedule")
        self.tree_event_shedule.headerItem().setText(0, "1")
        self.pushButton_create_insector = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_insector.setGeometry(QtCore.QRect(210, 130, 171, 25))
        self.pushButton_create_insector.setObjectName("pushButton_create_insector")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Event_shedule)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Ui_Event_shedule):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Event_shedule", "Логистик (Event shedule)"))
        self.pushButton_create_event.setText(_translate("Event_shedule", "Создать мероприятие"))
        self.pushButton_create_organization.setText(_translate("Event_shedule", "Создать организацию"))
        self.pushButton_create_member.setText(_translate("Event_shedule", "Создать участника"))
        self.label_event_shedule.setText(_translate("Event_shedule", "Расписание мероприятий"))
        self.pushButton_create_insector.setText(_translate("Event_shedule", "Создать инспектора"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind_shedule = Ui_Event_shedule()
    wind_shedule.show()
    sys.exit(app.exec_())