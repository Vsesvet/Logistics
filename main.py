#!/usr/bin/env/ python3

import os
import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
#import pymysql


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

    def move_to_center(self):
        desktop = QApplication.desktop()
        rect = desktop.screenGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

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

    def show_login(self):
        self.wind_login = Ui_Login()
        self.wind_event_shedule = Ui_Event_shedule()
        self.wind_login.pushButton_login.clicked.connect(self.wind_event_shedule.show)

class Processing:
    """Класс обработки данных"""
    def __init__(self):
        journal.log(f'----------Program started----------')

    def check_exist_db(self):
        """Если подключение к БД успешно, то запускаем программу, если нет, то выдаем сообщаем об отсутствии"""
        #self.db_path =
        pass
        journal.log(f'Подключение к базе данных. Успешно проведено')
        #journal.log(f'База данных не обнаружена. Создайте базу данных. Завершение работы программы')

    def check_exist_user(self):
        """Если в БД существует хотя бы один пользователь, то запускаем. Если такого нет, то предлагаем создать"""
        pass

    def rename_file_client(self, documents_members):
        """Переименование документов загруженных участниками мероприятия"""
        pass


class User:
    """Класс создания, редактирования, удаления, сохранения пользователя в БД"""
    def create(self, person, user_login):
        """Действие по клику на кнопку: Добавить нового пользователя"""
        # row_db = 'string in database'
        # user_id = len(row_db) + 1
        username_login = user.name(user_login)
        new_user = {}
        new_user['id'] = person[0]
        new_user['lname'] = person[1]
        new_user['fname'] = person[2]
        new_user['mname'] = person[3]
        new_user['city'] = person[4]
        new_user['phone'] = person[5]
        new_user['email'] = person[6]
        new_user['password'] = person[7]
        new_user['role'] = person[8]
        new_user['full_name'] = f'{person[1]}_{person[2]}_{person[3]}'

        # Проверка прав на создание и запись пользователя в БД. Если роль Сисадмин или Админ, идет запись в БД
        flag_access = access.check_role_admin(user_login)

        if flag_access ==  True:
            self.phone = new_user.get('phone')
            self.full_name = new_user.get('full_name')

            #write_new_user_to_db()

            journal.log(f"{username_login} - создал(а) нового пользователя {self.phone} {self.full_name}")
            self.create_user_profile_folder()
        else:
            journal.log(f"{username_login} - не хвататет прав для создания нового пользователя {new_user.get('phone')} {new_user.get('full_name')}")

    def name(self, user_login):
        """Возвращает Фамилию и Имя пользователя из user_login"""
        username = f'{user_login[1]} {user_login[2]}'
        return username

    def create_user_profile_folder(self):
        """Создание профильной папки участника"""
        self.user_profile_folder = f'/home/logistics/{self.full_name}_{self.phone}'
        os.makedirs(self.user_profile_folder)
        journal.log(f'Создана профильная директория: {self.full_name}_{self.phone}')


class Access:
    """Access module. Проверка данных Входа и роли пользователя, для совершения действия"""
    # def __init__(self):
    def login(self, number, password):
        """Сверяет данные логина и пароля"""
        # self.number = number
        # self.password = password
        for db_user in db:
            if db_user[5] == number and db_user[7] != password:
                journal.log(f'Попытка входа в систему. {db_user[1]} {db_user[2]} ({db_user[8]})  Неверный пароль.')

            elif db_user[5] == number and db_user[7] == password:
                journal.log(f'Успешный вход в систему. {db_user[1]} {db_user[2]}  ({db_user[8]})')
                return db_user
        journal.log(f'Отклонен вход в систему c учетными данными: Логин: {number}, Пароль: {password}')
        journal.log(f'----------------------------------------------------------------')
        sys.exit(0)

    def check_role_sysadmin(self, user_login):
        """Проверка роли системного администратора"""
        role = user_login[8]
        if role == 'sysadmin':
            return True
        else:
            return False

    def check_role_admin(self, user_login):
        """Проверка роли Администратора пользователя для совершения действия"""
        role = user_login[8]
        if role == 'sysadmin':
            return True
        elif role == 'admin':
            return True
        else:
            return False

    def check_role_member(self, user_login):
        """Проверка роли - приндалежность к Участнику"""
        role = user_login[8]
        if role == 'member':
            return True
        else:
            return False

    def check_role_inspector(self, user_login):
        """Проверка роли - принадлежность к Инспектору"""
        role = user_login[8]
        if role == 'inspector':
            return True
        else:
            return False


class Journal:
    """Логирование работы программы в файл журнала"""
    def __init__(self):
        """Получаем текущее время из datetime"""
        self.dt_now = str(datetime.now())
        self.dt_now.split('.')
        self.dt_now = self.dt_now[:-7]
    def log(self, info):
        """Логирование событий"""
        self.info = info
        self.path_dir_journal = r'/home/logistics'
        self.path_journal_log = r'/home/logistics/journal.log'

        # Стандартная запись лога события
        if os.path.isfile(self.path_journal_log):
            with open(self.path_journal_log, 'a') as file:
                file.write(f"{self.dt_now} {info} \n")
        elif not os.path.isdir(self.path_dir_journal):
            self.create_path_dir_journal()

        # Проверка существования journal.log
        elif not os.path.isfile(self.path_journal_log):
            self.create_file_journal(self.info)

    def create_path_dir_journal(self):
        """Создание директорий для хранения journal.log"""
        os.makedirs(self.path_dir_journal)
        print(f'Journal.log() Создание структуры папок для размещения файла журнала: {self.path_dir_journal}')
        self.create_file_journal(self.info)

    def create_file_journal(self, info):
        """Создание файла journal.log"""
        print(f'Файл journal.log по пути {self.path_journal_log} не найден, поэтому был создан')
        with open(self.path_journal_log, 'w') as file:
            file.write(f"{self.dt_now[:-7]} {info} \n")
            info_dir = (f'Journal.log() Создание структуры папок для размещения файла журнала: {self.path_dir_journal}')
            info_file = (f'Journal.log() Создан файл журнала: {self.path_journal_log}')
            file.write(f"{self.dt_now[:-7]} {info_dir} \n")
            file.write(f"{self.dt_now[:-7]} {info_file} \n")

    def finish_log(self):
        """Последние строки лога перед завершением программы"""
        self.log(f'Выход пользователя {username_login} из системы')
        self.log(f'----------Program finished----------')
        print(f'{self.dt_now} Программа завершена без ошибок')


# Body programm
# Инициализация классов Журнала, Обработки данных, Интерфейса пользователя
journal = Journal()
processing = Processing()
user = User()
access = Access()

# Проверка существования БД
processing.check_exist_db()

id = 0
# 'Пользователи из БД'
db_user1 = ('000001', 'Ефремов', 'Максим', 'Гергиевич', 'Москва', '79777194310', 'efremov@mgido.com', 'gnt6al47', 'sysadmin')
db_user2 = ('000002', 'Фомина', 'Ирина', 'Владимировна', 'Москва', '79296062723', 'fomina@mgido.com', 'gnt6al47', 'admin')
db_user3 = ('000003', 'Корнеева', 'Ирина', 'Владимировна', 'Москва', '79671574048', 'i.korneeva@mgido.com', 'gnt6al47', 'admin')
db_user4 = ('000004', 'Дериглазова', 'Марина', 'Сергеевна', 'Санкт-Петербург', '79216436255', 'der-maria@yandex.ru', 'gnt6al47', 'client')
# Database storage:
db = (db_user1, db_user2, db_user3, db_user4)

# Пробные пользователи, которых"создают" администраторы
new_user1 = ('000006', 'Апаева', 'Юлия', 'Владимировна', 'Москва',	'79689537780', 'email@mail.ru', 'bx501eGA', 'client')
new_user2 = ('000007', 'Воронцова', 'Елена', 'Ивановна', 'Новосибирск', '79095346668', 'rico7272@mail.ru', 'tRxc9mqW', 'client')
new_user3 = ('000008', 'Дериглазов', 'Сергей', 'Алексеевич', 'Санкт-Петербург', '79216436250', 'der-sergey@yandex.ru', '2He5zqUn', 'client')

# Документы создаваемые/загружаемые участниками (members). Данные колонок из БД.
agree = 'agree'
diplom = 'diplom'
inn = 'inn'
passport = 'passport'
registration = 'registration'
snils ='snils'
sertificate = 'sertificate'
survey = 'survey'
documents_members = (agree, diplom, inn, passport, registration, snils, sertificate, survey)

# Вход пользователя по номеру телефона и паролю, запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ui_Login()
    login.move_to_center()
    login.show()
    # event_shedule = Ui_Event_shedule()
    # event_shedule.show()
    sys.exit(app.exec())


number = input('Логин: ')
password = input('Пароль: ')
user_login = access.login(number, password)
username_login = user.name(user_login)

user.create(new_user1, user_login)

# Запись в journal.log события окончания работы программы.
journal.finish_log()
