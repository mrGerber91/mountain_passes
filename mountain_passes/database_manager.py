from django.contrib.contenttypes.models import ContentType
import os
from dotenv import load_dotenv
from .models import Users
import psycopg2

load_dotenv()

class DataBaseManager:
    def __init__(self):
        # Инициализация параметров подключения
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
        self.cur.close()
        self.conn.close()

    def get_new_perevals(self):
        self.cur.execute("SELECT * FROM PerevalAdded WHERE status='new'")
        new_perevals = self.cur.fetchall()
        return new_perevals

    def update_pereval_status(self, pereval_id, new_status):
        try:
            self.cur.execute("UPDATE PerevalAdded SET status=%s WHERE id=%s", (new_status, pereval_id))
            self.conn.commit()
            print(f"Status for Pereval {pereval_id} updated to {new_status}")
        except Exception as e:
            print(f"Error updating status: {e}")

    def create_user(self, email, fam, name, otc, phone):
        user = Users.objects.create(email=email, fam=fam, name=name, otc=otc, phone=phone)
        return user

    def add_pereval(self, user_id, beauty_title, title, other_titles, connect, add_time, winter_level, summer_level,
                    autumn_level, spring_level, latitude, longitude, height):
        user = Users.objects.get(id=user_id)
        coord = Coord.objects.create(latitude=latitude, longitude=longitude, height=height)
        pereval = PerevalAdded.objects.create(user=user, beauty_title=beauty_title, title=title, other_titles=other_titles,
                                              connect=connect, add_time=add_time, winter_level=winter_level, summer_level=summer_level,
                                              autumn_level=autumn_level, spring_level=spring_level, coord=coord)
        return pereval

    def add_pereval_image(self, pereval_id, data, title):
        pereval_model = ContentType.objects.get_for_model(PerevalAdded)
        pereval = pereval_model.model_class().objects.get(id=pereval_id)
        image = PerevalImages.objects.create(pereval_added=pereval, data=data, title=title)
        return image

    def get_pereval_images(self, pereval_id):
        pereval_model = ContentType.objects.get_for_model(PerevalAdded)
        pereval = pereval_model.model_class().objects.get(id=pereval_id)
        return PerevalImages.objects.filter(pereval_added=pereval)

    def get_user_perevals(self, email):
        user = Users.objects.get(email=email)
        return PerevalAdded.objects.filter(user=user)

    def edit_pereval(self, pereval_id, data):
        pereval = PerevalAdded.objects.get(id=pereval_id)
        for key, value in data.items():
            setattr(pereval, key, value)
        pereval.save()
        return pereval

    def delete_pereval(self, pereval_id):
        pereval = PerevalAdded.objects.get(id=pereval_id)
        pereval.delete()

    def delete_pereval_image(self, image_id):
        image = PerevalImages.objects.get(id=image_id)
        image.delete()
