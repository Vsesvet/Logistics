"""//////////////////////////////////////////////"""
""""////////------IMPORT LIBRARIES-------////////"""
"""//////////////////////////////////////////////"""
import sys

"""//////////////////////////////////////////////"""
""""////////------IMPORT CLASSES-------////////"""
"""//////////////////////////////////////////////"""
from Class_Journal import *

class Access:
    """Access module. Проверка данных Входа и роли пользователя, для совершения действия"""
    # def __init__(self):
    def login(self, phone_number, password):
        """Сверяет данные логина и пароля"""
        # self.number = number
        # self.password = password
        for db_user in db:
            if db_user[5] == phone_number and db_user[7] != password:
                journal.log(f'Попытка входа в систему. {db_user[1]} {db_user[2]} ({db_user[8]})  Неверный пароль.')

            elif db_user[5] == phone_number and db_user[7] == password:
                journal.log(f'Успешный вход в систему. {db_user[1]} {db_user[2]}  ({db_user[8]})')
                return db_user
        journal.log(f'Отклонен вход в систему c учетными данными: Логин: {phone_number}, Пароль: {password}')
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


journal = Journal()

db_user1 = ('000001', 'Ефремов', 'Максим', 'Гергиевич', 'Москва', '79777194310', 'efremov@mgido.com', 'gnt6al47', 'sysadmin')
db_user2 = ('000002', 'Фомина', 'Ирина', 'Владимировна', 'Москва', '79296062723', 'fomina@mgido.com', 'gnt6al47', 'admin')
db_user3 = ('000003', 'Корнеева', 'Ирина', 'Владимировна', 'Москва', '79671574048', 'i.korneeva@mgido.com', 'gnt6al47', 'admin')
db_user4 = ('000004', 'Дериглазова', 'Марина', 'Сергеевна', 'Санкт-Петербург', '79216436255', 'der-maria@yandex.ru', 'gnt6al47', 'client')
# Database storage:
db = (db_user1, db_user2, db_user3, db_user4)