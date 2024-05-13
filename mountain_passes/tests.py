from django.test import TestCase
from .models import PerevalAdded, Users, Coord
from mountain_passes.database_manager import DataBaseManager


class TestDataBaseManager(TestCase):
    def setUp(self):
        self.db_manager = DataBaseManager()
        self.db_manager.connect()

    def tearDown(self):
        self.db_manager.close()

    def test_create_user(self):
        email = "test@example.com"
        fam = "Иванов"
        name = "Иван"
        otc = "Иванович"
        phone = "1234567890"

        user = self.db_manager.create_user(email, fam, name, otc, phone)

        # Проверяем, что пользователь был создан
        self.assertTrue(Users.objects.filter(email=email, fam=fam, name=name, otc=otc, phone=phone).exists())

class UsersTest(TestCase):
    def test_create_user(self):
        user = Users.objects.create(email="test@example.com", fam="Фамилия", name="Имя", otc="Отчество", phone="1234567890")
        self.assertEqual(user.email, "test@example.com")


class PerevalAddedTests(TestCase):
    def setUp(self):
        # Создание пользователя
        self.user = Users.objects.create(email="test@example.com", fam="Фамилия", name="Имя", otc="Отчество",
                                         phone="1234567890")

        # Создание координат
        self.coord = Coord.objects.create(latitude="50.0", longitude="30.0", height="1000")

        # Создание перевала с присвоением пользователя и координат
        self.pereval = PerevalAdded.objects.create(user=self.user, beauty_title="Красивый перевал", title="Перевал",
                                                   other_titles="Другие названия", connect="Соединения",
                                                   add_time="2023-12-31T12:00:00Z", winter_level="Зимний уровень",
                                                   summer_level="Летний уровень", autumn_level="Осенний уровень",
                                                   spring_level="Весенний уровень", coord=self.coord)

    def test_create_pereval(self):
        self.assertEqual(self.pereval.beauty_title, "Красивый перевал")

    def test_update_pereval_status(self):
        new_status = 'approved'
        self.pereval.status = new_status
        self.pereval.save()

        updated_pereval = PerevalAdded.objects.get(id=self.pereval.id)
        self.assertEqual(updated_pereval.status, 'approved')
