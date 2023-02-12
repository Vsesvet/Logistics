#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# Изначально вручную - создаем директорию '/home/logistics'. И присваиваем ей права пользователя и группы.
# tail -f /home/logistics/journal.log - динамическое отображение логов работы программы.
# Установка PyMySQL: sudo pip3 install PyMySQL
import os
import sys
from datetime import datetime
#import pymysql


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
number = input('Логин: ')
password = input('Пароль: ')
user_login = access.login(number, password)
username_login = user.name(user_login)

user.create(new_user1, user_login)

# Запись в journal.log события окончания работы программы.
journal.finish_log()
