import os
import psycopg2
from psycopg2 import sql

class DataBaseManager:
    def __init__(self):
        # Получаем параметры подключения к базе данных из переменных окружения
        self.db_host = os.getenv('FSTR_DB_HOST')
        self.db_port = os.getenv('FSTR_DB_PORT')
        self.db_login = os.getenv('FSTR_DB_LOGIN')
        self.db_pass = os.getenv('FSTR_DB_PASS')

    def connect(self):
        # Установка соединения с базой данных
        try:
            self.conn = psycopg2.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_login,
                password=self.db_pass,
                database='mountain_passes'  # Имя базы данных
            )
            self.cur = self.conn.cursor()
            print("Connected to the database")
        except Exception as e:
            print(f"Unable to connect to the database: {e}")

    def close(self):
        # Закрытие соединения с базой данных
        self.cur.close()
        self.conn.close()

    def add_pereval(self, data):
        # Метод для добавления нового перевала в базу данных
        try:
            # При добавлении новой строки в таблицу с перевалами устанавливаем значение поля status равным new
            sql_query = sql.SQL("INSERT INTO pereval_added (date_added, beauty_title, title, "
                                "other_titles, connect, add_time, winter_level, summer_level, "
                                "autumn_level, spring_level, coord_id, user_id, status) "
                                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            self.cur.execute(sql_query, data)
            self.conn.commit()
            print("Pereval added successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Unable to add pereval: {e}")
