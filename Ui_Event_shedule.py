from PyQt5.QtWidgets import QMainWindow
from Class_Journal import *
from Ui_Create_event import *
from Ui_Create_participant import *
from Ui_Create_organization import *
from Ui_Create_inspector import *
# from Ui_list_of_all_participants_F import*
from Ui_list_of_all_participants import*
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Event_shedule(QMainWindow):
    """Главное окно Расписание Мероприятий"""
    def __init__(self):
        super(Ui_Event_shedule, self).__init__()
        self.setObjectName("Event_shedule")
        self.resize(1080, 620)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # username_role, заполнение setText в разделе
        self.label_username_role = QtWidgets.QLabel(self.centralwidget)
        self.label_username_role.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_username_role.setObjectName("label_username_role")
        self.gridLayout_2.addWidget(self.label_username_role, 0, 3, 1, 3)

        self.label_event_shedule = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_event_shedule.setFont(font)
        self.label_event_shedule.setObjectName("label_event_shedule")
        self.gridLayout_2.addWidget(self.label_event_shedule, 1, 2, 1, 1)
        self.pushButton_create_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_event.setObjectName("pushButton_create_event")
        self.gridLayout_2.addWidget(self.pushButton_create_event, 2, 0, 1, 1)

        self.pushButton_show_all_participants = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_all_participants.setObjectName("pushButton_show_all_participants")
        self.gridLayout_2.addWidget(self.pushButton_show_all_participants, 3, 3, 1, 1)

        self.pushButton_create_organization = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_organization.setObjectName("pushButton_create_organization")
        self.gridLayout_2.addWidget(self.pushButton_create_organization, 2, 1, 1, 1)
        self.pushButton_export_xls = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_xls.setObjectName("pushButton_export_xls")
        self.gridLayout_2.addWidget(self.pushButton_export_xls, 2, 3, 1, 1)
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setObjectName("pushButton_print")
        self.gridLayout_2.addWidget(self.pushButton_print, 2, 4, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout_2.addWidget(self.pushButton_exit, 2, 5, 1, 1)
        self.pushButton_create_participant = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_participant.setObjectName("pushButton_create_participant")
        self.gridLayout_2.addWidget(self.pushButton_create_participant, 3, 0, 1, 1)
        self.pushButton_create_inspector = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_inspector.setObjectName("pushButton_create_inspector")
        self.gridLayout_2.addWidget(self.pushButton_create_inspector, 3, 1, 1, 1)

        # Таблица Мероприятий Tree Event Shedule
        self.tree_event_shedule = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_event_shedule.setObjectName("tree_event_shedule")
        self.tree_event_shedule.headerItem().setText(0, "1")
        self.gridLayout_2.addWidget(self.tree_event_shedule, 4, 0, 1, 6)

        # Заполнение заголовков Tree Event Shedule
        columns_names = [' Мероприятие ', 'Дата', 'Страна', 'Город', 'Участников', 'Организация', 'Статус']
        self.adjust_tree(columns_names, self.tree_event_shedule)

        # Заголовки Label
        self.label_total_completed_events = QtWidgets.QLabel(self.centralwidget)
        self.label_total_completed_events.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_total_completed_events.setObjectName("label_total_completed_events")
        self.gridLayout_2.addWidget(self.label_total_completed_events, 5, 3, 1, 3)
        self.label_find_event = QtWidgets.QLabel(self.centralwidget)
        self.label_find_event.setObjectName("label_find_event")
        self.gridLayout_2.addWidget(self.label_find_event, 6, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_status_event = QtWidgets.QLabel(self.centralwidget)
        self.label_status_event.setObjectName("label_status_event")
        self.gridLayout.addWidget(self.label_status_event, 0, 4, 1, 1)

        # ComboBox comboBox_select_organization & comboBox_event_status
        self.comboBox_select_organization = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_select_organization.setObjectName("comboBox_select_organization")
        self.comboBox_select_organization.addItem("")
        self.comboBox_select_organization.addItem("")
        self.comboBox_select_organization.addItem("")
        self.comboBox_select_organization.addItem("")
        self.comboBox_select_organization.setItemText(3, "")
        self.gridLayout.addWidget(self.comboBox_select_organization, 0, 3, 1, 1)
        self.label_organization = QtWidgets.QLabel(self.centralwidget)
        self.label_organization.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_organization.setObjectName("label_organization")
        self.gridLayout.addWidget(self.label_organization, 0, 2, 1, 1)
        self.comboBox_event_status = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_event_status.setObjectName("comboBox_event_status")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.gridLayout.addWidget(self.comboBox_event_status, 0, 5, 1, 1)

        # Здесь надо реализовать функцию Поиска по мероприятиям
        # По наименованию, датам,
        self.lineEdit_find_event = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_find_event.setObjectName("lineEdit_find_event")
        self.gridLayout.addWidget(self.lineEdit_find_event, 0, 0, 1, 2)
        self.dateEdit_finish_event = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_finish_event.setDate(QtCore.QDate(2023, 12, 31))
        self.dateEdit_finish_event.setObjectName("dateEdit_finish_event")
        self.gridLayout.addWidget(self.dateEdit_finish_event, 1, 1, 1, 1)
        self.dateEdit_begin_event = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_begin_event.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_begin_event.setObjectName("dateEdit_begin_event")
        self.gridLayout.addWidget(self.dateEdit_begin_event, 1, 0, 1, 1)
        self.pushButton_find_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find_event.setObjectName("pushButton_find_event")
        self.gridLayout.addWidget(self.pushButton_find_event, 1, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 7, 0, 1, 6)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)

        # Нажатия на кнопки
        # self.pushButton_exit.clicked.connect(self.finish_log)
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_create_event.clicked.connect(self.show_create_event)
        self.pushButton_create_participant.clicked.connect(self.show_create_participant)
        self.pushButton_create_organization.clicked.connect(self.show_create_organization)
        self.pushButton_create_inspector.clicked.connect(self.show_create_inspector)
        self.pushButton_export_xls.clicked.connect(self.showFullScreen)
        self.pushButton_print.clicked.connect(self.show)
        self.pushButton_find_event.clicked.connect(self.tree_event_shedule.clear)
        self.pushButton_show_all_participants.clicked.connect(self.show_list_of_all_participants)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Порядок перехода по Tab
        self.setTabOrder(self.pushButton_create_event, self.pushButton_create_participant)
        self.setTabOrder(self.pushButton_create_participant, self.pushButton_create_organization)
        self.setTabOrder(self.pushButton_create_organization, self.pushButton_create_inspector)
        self.setTabOrder(self.pushButton_create_inspector, self.tree_event_shedule)
        self.setTabOrder(self.tree_event_shedule, self.pushButton_export_xls)
        self.setTabOrder(self.pushButton_export_xls, self.pushButton_print)
        self.setTabOrder(self.pushButton_print, self.pushButton_exit)
        self.setTabOrder(self.pushButton_exit, self.lineEdit_find_event)
        self.setTabOrder(self.lineEdit_find_event, self.dateEdit_begin_event)
        self.setTabOrder(self.dateEdit_begin_event, self.dateEdit_finish_event)
        self.setTabOrder(self.dateEdit_finish_event, self.comboBox_select_organization)
        self.setTabOrder(self.comboBox_select_organization, self.comboBox_event_status)
        self.setTabOrder(self.comboBox_event_status, self.pushButton_find_event)

    def retranslateUi(self, Ui_Event_shedule):
        """Перевод на русский наименования кнопок, меток"""
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Логистик  (update 23.02)"))

        # Передать сюда username_role из Class_Access или Class_User
        self.label_username_role.setText(_translate("self", "Фомина Ирина (Администратор)"))

        self.label_event_shedule.setText(_translate("self", "Расписание мероприятий"))
        self.pushButton_create_event.setText(_translate("self", "Создать мероприятие"))
        self.pushButton_create_organization.setText(_translate("self", "Создать организацию"))
        self.pushButton_export_xls.setText(_translate("self", "Export xls"))
        self.pushButton_show_all_participants.setText(_translate("self", "Список участников"))
        self.pushButton_print.setText(_translate("self", "Печать"))
        self.pushButton_exit.setText(_translate("self", "Выход"))
        self.pushButton_create_participant.setText(_translate("self", "Создать участника"))
        self.pushButton_create_inspector.setText(_translate("self", "Создать инспектора"))

        # Здесь должна быть функция подсчета количества мероприятий
        self.label_total_completed_events.setText(_translate("self", "Всего проведено 2 мероприятия"))

        self.label_find_event.setText(_translate("self", "Фильтры поиска мероприятия:"))
        self.label_status_event.setText(_translate("self", "Статус мероприятия"))
        self.comboBox_select_organization.setItemText(0, _translate("self", "Все"))
        self.comboBox_select_organization.setItemText(1, _translate("self", "Мерц"))
        self.comboBox_select_organization.setItemText(2, _translate("self", "Аллерган"))
        self.label_organization.setText(_translate("self", "Организация"))
        self.comboBox_event_status.setItemText(0, _translate("self", "Все"))
        self.comboBox_event_status.setItemText(1, _translate("self", "Запланировано"))
        self.comboBox_event_status.setItemText(2, _translate("self", "Проведено"))
        self.comboBox_event_status.setItemText(3, _translate("self", "Отменено"))
        self.lineEdit_find_event.setPlaceholderText(_translate("self", "Наименование мероприятия..."))
        self.pushButton_find_event.setText(_translate("self", "Найти"))
        self.move_to_center()
        # self.set_username_and_role()

    def move_to_center(self):
        """Выравниваем окно по центру экрана"""
        desktop = QApplication.desktop()
        desktop.screenGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

    # def set_username_and_role(self, user_login):


    def adjust_tree(self, columns_names, tree):
        """Установка наименований для колонок Tree"""
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for i in columns_names:
            tree.headerItem().setText(columns_names.index(i), i)

        # Разобраться как установить фикс размер для первой колонки
        # tree.resizeColumnToContents(50)

    def show_create_event(self):
        """Запускает окно Создание Мероприятия"""
        create_event = Ui_Create_event()
        # exec - открывает QDialog, как модальное окно!
        create_event.exec()

    def show_create_participant(self):
        """Заспускает окно создание Участника"""
        self.create_participant = Ui_Create_participant()
        # exec - открывает QDialog, как модальное окно!
        self.create_participant.exec()

    def show_create_organization(self):
        """Запускает окно создание Организации"""
        self.create_organization = Ui_Create_org()
        # exec - открывает QDialog, как модальное окно!
        self.create_organization.exec()

    def show_create_inspector(self):
        """Запускает окно создание Инспектора"""
        self.create_inspector = Ui_Create_inspector()
        self.create_inspector.exec()

    def show_list_of_all_participants(self):
        """Запускает окно просмотра всех пользователей"""
        self.show_list_of_all_participants = Ui_list_of_all_participants()
        #self.ui_list_of_all_participants_f = Ui_list_of_all_participants_F()
        self.show_list_of_all_participants.exec()
    def finish_log(self):
        """Запись в journal.log события окончания работы программы."""
        Journal().finish_log()