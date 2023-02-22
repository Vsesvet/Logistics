from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from db_config import host, port, password, db_name, user
from Class_Mysql import*
from Ui_Create_participant import*


class Ui_list_of_all_participants(QDialog):
    def __init__(self):
        super(Ui_list_of_all_participants, self).__init__()
        self.setObjectName("List_of_all_participants")
        self.resize(1016, 556)
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_find_participant = QtWidgets.QLineEdit(self)
        self.lineEdit_find_participant.setObjectName("lineEdit_find_participant")
        self.gridLayout_2.addWidget(self.lineEdit_find_participant, 0, 0, 1, 2)
        self.pushButton_find_event_2 = QtWidgets.QPushButton(self)
        self.pushButton_find_event_2.setObjectName("pushButton_find_event_2")
        self.gridLayout_2.addWidget(self.pushButton_find_event_2, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 0, 1, 7)
        self.tree_participants_list = QtWidgets.QTreeWidget(self)
        self.tree_participants_list.setObjectName("tree_participants_list")

        #Установка соеденения с БД
        self.db = Mysql(host, port, user, password, db_name)

        #Установка заголовков для колонок  treeWidget
        headers_names = ['Телефон', 'Фамилия', 'Имя', 'Отчетство', 'Город', 'e-mail', 'Пароль', 'Комментарий']
        self.set_headers(headers_names, self.tree_participants_list)
        # self.tree_participants_list.headerItem().setText(0, "Номер телефона")
        # self.tree_participants_list.headerItem().setText(1, "Фамилия")
        # self.tree_participants_list.headerItem().setText(2, "Имя")
        # self.tree_participants_list.headerItem().setText(3, "Отчество")
        # self.tree_participants_list.headerItem().setText(4, "Город")
        # self.tree_participants_list.headerItem().setText(5, "E-mail")
        # self.tree_participants_list.headerItem().setText(6, "Пароль")
        # self.tree_participants_list.headerItem().setText(7, "Комментарий")

        self.set_view_of_all_participants()


        self.gridLayout_3.addWidget(self.tree_participants_list, 4, 0, 1, 7)
        self.pushButton_export_xls = QtWidgets.QPushButton(self)
        self.pushButton_export_xls.setObjectName("pushButton_export_xls")
        self.gridLayout_3.addWidget(self.pushButton_export_xls, 2, 5, 1, 1)
        self.pushButton_redact_participant = QtWidgets.QPushButton(self)
        self.pushButton_redact_participant.setObjectName("pushButton_redact_participant")
        self.gridLayout_3.addWidget(self.pushButton_redact_participant, 3, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_3.addWidget(self.pushButton_close, 2, 6, 1, 1)
        self.label_username_role = QtWidgets.QLabel(self)
        self.label_username_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_role.setObjectName("label_username_role")
        self.gridLayout_3.addWidget(self.label_username_role, 0, 5, 1, 2)
        self.pushButton_create_participant = QtWidgets.QPushButton(self)
        self.pushButton_create_participant.setObjectName("pushButton_create_participant")
        self.gridLayout_3.addWidget(self.pushButton_create_participant, 3, 0, 1, 1)

        self.pushButton_delete_participant = QtWidgets.QPushButton(self)
        self.pushButton_delete_participant.setObjectName("pushButton_delete_participant")
        self.gridLayout_3.addWidget(self.pushButton_delete_participant, 3, 6, 1, 1)

        self.label_find_event = QtWidgets.QLabel(self)
        self.label_find_event.setObjectName("label_find_event")
        self.gridLayout_3.addWidget(self.label_find_event, 5, 0, 1, 3)
        self.label_participants_list = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_participants_list.setFont(font)
        self.label_participants_list.setObjectName("label_participants_list")
        self.gridLayout_3.addWidget(self.label_participants_list, 2, 2, 1, 1)


        self.retranslateUi(self)
        self.pushButton_delete_participant.clicked.connect(self.delete_participant)
        self.pushButton_create_participant.clicked.connect(self.show_create_participant)
        self.pushButton_close.clicked.connect(self.close)


        #self.pushButton_create_participant.clicked.connect(self.delete_participant())
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, List_of_all_participants):
        _translate = QtCore.QCoreApplication.translate
        List_of_all_participants.setWindowTitle(_translate("List_of_all_participants", "Общий список участников"))
        self.lineEdit_find_participant.setPlaceholderText(_translate("List_of_all_participants", "Поиск участника"))
        self.pushButton_find_event_2.setText(_translate("List_of_all_participants", "Найти"))
        self.pushButton_export_xls.setText(_translate("List_of_all_participants", "Export xls"))
        self.pushButton_redact_participant.setText(_translate("List_of_all_participants", "Редактировать участника"))
        self.pushButton_close.setText(_translate("List_of_all_participants", "Закрыть"))

        #Сюда транслировать из Access или Ui_event_schedule
        self.label_username_role.setText(_translate("List_of_all_participants", "Фомина Ирина (Администратор)"))
        self.pushButton_create_participant.setText(_translate("List_of_all_participants", "Создать участника"))
        self.label_find_event.setText(_translate("List_of_all_participants", "Фильтры поиска участника:"))
        self.label_participants_list.setText(_translate("List_of_all_participants", "Общий список участников"))
        self.pushButton_delete_participant.setText(_translate("List_of_all_participants", "Удалить участника"))

    def set_headers(self, headers_names, tree):
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)


    def set_view_of_all_participants(self):
        """Отображение данных по всем участникам"""
        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = self.db.select_all(table_name)

        value = []

        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()

    def delete_participant(self):
        """Удаление участника из списка"""
        try:
            phone_number = self.tree_participants_list.currentItem().text(0)
            print(phone_number)
            id = (self.db.get_participant_id(phone_number))[0]["participant_id"]
            self.db.delete_participant(id)
            self.tree_participants_list.clear()
            self.set_view_of_all_participants()
        except Exception as ex:
            print("cant do")

    def show_create_participant(self):
        """Заспускает окно создание Участника"""
        self.create_participant = Ui_Create_participant()
        # exec - открывает QDialog, как модальное окно!
        self.create_participant.exec()

        if not self.create_participant.isActiveWindow():
            self.tree_participants_list.clear()
            self.set_view_of_all_participants()
        # else:
        #     pass