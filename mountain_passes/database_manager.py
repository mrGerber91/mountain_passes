import os
import psycopg2
from psycopg2 import sql

# Менеджер базы данных PostgreSQL
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

    def add_image(self, title):
        # Метод для добавления нового изображения в базу данных
        try:
            sql_query = sql.SQL("INSERT INTO pereval_images (title) VALUES (%s)")
            self.cur.execute(sql_query, (title,))
            self.conn.commit()
            print("Image added successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Unable to add image: {e}")

    def add_user(self, email, fam, name, otc):
        # Метод для добавления нового пользователя в базу данных
        try:
            sql_query = sql.SQL("INSERT INTO users (email, fam, name, otc) VALUES (%s, %s, %s, %s)")
            self.cur.execute(sql_query, (email, fam, name, otc))
            self.conn.commit()
            print("User added successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Unable to add user: {e}")

    def moderate_pereval(self, pereval_id, status):
        # Метод для изменения статуса модерации перевала
        try:
            sql_query = sql.SQL("UPDATE pereval_added SET status = %s WHERE id = %s")
            self.cur.execute(sql_query, (status, pereval_id))
            self.conn.commit()
            print("Pereval status updated successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Unable to update pereval status: {e}")

    def close_connection(self):
        # Метод для закрытия соединения с базой данных
        self.cur.close()
        self.conn.close()
        print("Connection to the database closed")

    def get_all_perevals(self):
        # Метод для получения списка всех перевалов из базы данных
        try:
            self.cur.execute("SELECT * FROM pereval_added")
            perevals = self.cur.fetchall()
            print("All perevals retrieved successfully")
            return perevals
        except Exception as e:
            print(f"Unable to retrieve all perevals: {e}")
            return None
