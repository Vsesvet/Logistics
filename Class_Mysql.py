import pymysql

class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self, host, port, user, password, db_name):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor)

    def select_all_data(self):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM 'users'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            return rows

    def add_user(self, phone_number, second_name, first_name, last_name, role, fullname, city, email, password):
        """Добавление нового пользователя в базу данных MySql"""

        insert_query = f"INSERT INTO 'users' (phone_number, second_name, first_name, last_name, role, fullname, city, email, password) \
        VALUES = ({phone_number}, {second_name}, {first_name}, {last_name}, {role}, {fullname}, {city}, {email}, {password})"
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def delete_user(self, id):
        """Удаление пользователя из БД MySql по id"""
        delete_quere = f"DELETE FROM 'users' WHERE id = {id}"
        with self.connection.cursor() as cursor:
            cursor.execute(delete_quere)
            self.connection.commit()

    def __del__(self):
        """Закрытие сессии соединения с базой данных"""
        self.connection.close()


