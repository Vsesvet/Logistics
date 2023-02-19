"""//////////////////////////////////////////////"""
""""////////------IMPORT CLASSES-------//////////"""
"""//////////////////////////////////////////////"""
from Class_User import *
from Class_Access import *
from Class_Journal import *
from Class_Processing import *
from My_Ui_Login import *



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


# Вход пользователя по номеру телефона и паролю, запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ui_Login()
    login.move_to_center()
    login.show()

    sys.exit(app.exec())


# user.create(new_user1, user_login)

# Запись в journal.log события окончания работы программы.
# journal.finish_log()
