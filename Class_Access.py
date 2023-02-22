import sys
from Class_Journal import *

class Access:
    """Access module. Проверка данных Входа и роли пользователя, для совершения действия"""
    # def __init__(self):

    def login(self, phone_number, password):
        """Сверяет данные логина и пароля"""
        for db_user in db:
            if db_user['phone_number'] == phone_number and db_user['password'] != password:
                journal.log(f"Попытка входа в систему. {db_user['second_name']} {db_user['first_name']} ({db_user['role']})  Неверный пароль.")

            elif db_user['phone_number'] == phone_number and db_user['password'] == password:
                journal.log(f"Успешный вход в систему. {db_user['second_name']} {db_user['first_name']}  ({db_user['role']})")
                return db_user
        journal.log(f'Отклонен вход в систему c учетными данными: Логин: {phone_number}, Пароль: {password}')
        journal.log(f'----------------------------------------------------------------')
        sys.exit(0)

    def check_role_sysadmin(self, user_login):
        """Проверка роли системного администратора"""
        role = user_login['role']
        if role == 'sysadmin':
            return True
        else:
            return False

    def check_role_admin(self, user_login):
        """Проверка роли Администратора пользователя для совершения действия"""
        role = user_login['role']
        if role == 'sysadmin':
            return True
        elif role == 'admin':
            return True
        else:
            return False

    def check_role_member(self, user_login):
        """Проверка роли - приндалежность к Участнику"""
        role = user_login['role']
        if role == 'participant':
            return True
        else:
            return False

    def check_role_inspector(self, user_login):
        """Проверка роли - принадлежность к Инспектору"""
        role = user_login['role']
        if role == 'inspector':
            return True
        else:
            return False


journal = Journal()


db_user1 = {'phone_number': '79777194310', 'second_name': 'Ефремов', 'first_name': 'Максим', 'last_name': 'Георгиевич', 'role': 'sysadmin', 'fullname': 'Ефремов Максим Георгиевич', 'city': 'Москва', 'e-mail': 'efremov@mgido.com', 'password': 'gnt6al47'}
db_user2 = {'phone_number': '79296062723', 'second_name': 'Фомина', 'first_name': 'Ирина', 'last_name': 'Владимировна', 'role': 'admin', 'fullname': 'Фомина Ирина Владимировна', 'city': 'Москва', 'e-mail': 'fomina@mgido.com', 'password': 'gnt6al47'}
db_user3 = {'phone_number': '79671574048', 'second_name': 'Корнеева', 'first_name': 'Ирина', 'last_name': 'Алексеевна', 'role': 'admin', 'fullname': 'Корнеева Ирина Алексеевна', 'city': 'Москва', 'e-mail': 'i.korneeva@mgido.com', 'password': 'gnt6al47'}
db_user4 = {'phone_number': '79216436255', 'second_name': 'Дериглазова', 'first_name': 'Дериглазова', 'last_name': 'Сергеевна', 'role': 'participant', 'fullname': 'Дериглазова Марина Сергеевна', 'city': 'Санкт-Петербург', 'e-mail': 'der-maria@yandex.ru', 'password': 'gnt6al47'}


# Database storage:
db = (db_user1, db_user2, db_user3, db_user4)
