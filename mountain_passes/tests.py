from django.test import TestCase
from .models import Users, PerevalAdded, PerevalImages
from mountain_passes.database_manager import DataBaseManager
from django.utils import timezone


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = Users.objects.create(email="test@example.com", fam="TestFam", name="TestName", otc="TestOtc",
                                         phone="123456789")

    def test_add_pereval(self):
        data = (
            timezone.now(),
            "Test Beauty Title",
            "Test Title",
            "Test Other Titles",
            "Test Connect",
            timezone.now(),
            "Test Winter Level",
            "Test Summer Level",
            "Test Autumn Level",
            "Test Spring Level",
            1,
            self.user.id,
            "new"
        )

        db_manager = DataBaseManager()
        db_manager.connect()
        db_manager.add_pereval(data)

        self.assertEqual(PerevalAdded.objects.count(), 1)

    def test_add_image(self):
        pereval = PerevalAdded.objects.create(user=self.user, beauty_title="Test Beauty Title", title="Test Title",
                                              other_titles="Test Other Titles",
                                              connect="Test Connect", add_time=timezone.now(),
                                              winter_level="Test Winter Level",
                                              summer_level="Test Summer Level", autumn_level="Test Autumn Level",
                                              spring_level="Test Spring Level",
                                              status="new")

        db_manager = DataBaseManager()
        db_manager.connect()
        db_manager.add_image("Test Image Title")

        self.assertEqual(PerevalImages.objects.filter(pereval_added=pereval).count(), 1)

    def test_add_user(self):
        db_manager = DataBaseManager()
        db_manager.connect()
        db_manager.add_user("test@example.com", "TestFam", "TestName", "TestOtc")

        self.assertEqual(Users.objects.count(), 2)



