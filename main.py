"""//////////////////////////////////////////////"""
""""////////------IMPORT CLASSES-------//////////"""
"""//////////////////////////////////////////////"""
from Class_User import *
from Class_Access import *
from Class_Journal import *
from Class_Processing import *
from Ui_Login import *
import pymysql



# Body programm
# Инициализация классов Журнала, Обработки данных, Интерфейса пользователя
journal = Journal()
processing = Processing()
user = User()
access = Access()

# Проверка подлючения к базе данных
# processing.check_database_connection()


# Запуск окна Логин. Вход пользователя по номеру телефона и паролю.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ui_Login()
    login.move_to_center()
    login.show()

    sys.exit(app.exec())


# user.create(new_user1, user_login)

# Запись в journal.log события окончания работы программы.
# journal.finish_log()
