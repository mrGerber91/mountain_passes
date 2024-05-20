from django.test import TestCase
from .models import PerevalAdded, Users, Coord
from mountain_passes.database_manager import DataBaseManager
from django.test import Client

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

        self.assertTrue(Users.objects.filter(email=email, fam=fam, name=name, otc=otc, phone=phone).exists())

class UsersTest(TestCase):
    def test_create_user(self):
        user = Users.objects.create(email="test@example.com", fam="Фамилия", name="Имя", otc="Отчество", phone="1234567890")
        self.assertEqual(user.email, "test@example.com")

class PerevalAddedTests(TestCase):
    def setUp(self):
        self.user = Users.objects.create(email="test@example.com", fam="Фамилия", name="Имя", otc="Отчество", phone="1234567890")
        self.coord = Coord.objects.create(latitude="50.0", longitude="30.0", height="1000")
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

class TestDataSubmissionRetrieval(TestCase):
    def test_submit_and_retrieve_data(self):
        client = Client()

        user = Users.objects.create(email="test@example.com", fam="Фамилия", name="Имя", otc="Отчество", phone="1234567890")

        new_data = {
            "user": {
                "email": "test@example.com",
                "fam": "Фамилия",
                "name": "Имя",
                "otc": "Отчество",
                "phone": "1234567890"
            },
            "beauty_title": "Красивый перевал",
            "title": "Перевал",
            "other_titles": "Другие названия",
            "connect": "Соединения",
            "add_time": "2023-12-31T12:00:00Z",
            "winter_level": "Зимний уровень",
            "summer_level": "Летний уровень",
            "autumn_level": "Осенний уровень",
            "spring_level": "Весенний уровень",
            "coord": {
                "latitude": "50.0",
                "longitude": "30.0",
                "height": "1000"
            },
            "status": "new"
        }

        submission_response = client.post('/api/submitData/', data=new_data, content_type='application/json')
        print("Submission response status code:", submission_response.status_code)
        print("Submission response data:", submission_response.json())
        self.assertEqual(submission_response.status_code, 201)

        self.assertIn('id', submission_response.json())

        submission_id = submission_response.json()['id']
        print("Submission ID:", submission_id)

        retrieval_response = client.get(f'/api/submitData/{submission_id}/')
        print("Retrieval response status code:", retrieval_response.status_code)
        print("Retrieval response data:", retrieval_response.json())
        self.assertEqual(retrieval_response.status_code, 200)

        retrieved_data = retrieval_response.json()
        self.assertEqual(retrieved_data['title'], "Перевал")
        self.assertEqual(retrieved_data['user']['email'], "test@example.com")

        deletion_response = client.delete(f'/api/submitData/{submission_id}/')
        print("Deletion response status code:", deletion_response.status_code)
        self.assertEqual(deletion_response.status_code, 204)

        verify_deletion_response = client.get(f'/api/submitData/{submission_id}/')
        print("Verify deletion response status code:", verify_deletion_response.status_code)
        self.assertEqual(verify_deletion_response.status_code, 404)
