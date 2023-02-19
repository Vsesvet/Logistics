import pymysql
from db_config import host, password,db_name,user
class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self, host, port, user, password, db_name):
        try:
            self.connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print("Error connection to db")

    def select_all_data(self):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM 'users'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            return rows

    def add_participant(self, phone_number, second_name, first_name, last_name, role, full_name, city, email, password, comment,disabled):
        """Добавление нового пользователя в базу данных MySql"""
        print(phone_number, second_name, first_name, last_name, role, full_name, city, email, password, comment)
        select_role_id = f"SELECT role_id FROM roles WHERE  role_name = '{role}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_id)
            result = cursor.fetchall()
            self.connection.commit()
        print(result)
        role_id = result[0]['role_id']
        print(role_id)

        insert_query = f"INSERT INTO participants (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
        VALUES('{phone_number}', '{second_name}', '{first_name}', '{last_name}', '{full_name}', {role_id}, '{city}', '{email}', '{password}', '{comment}',{disabled})"

        print(insert_query)
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


