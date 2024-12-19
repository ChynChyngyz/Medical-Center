from django.test import TestCase
from django.urls import reverse
from services.models import Service
from speciality.models import Speciality


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестовую специализацию
        cls.speciality = Speciality.objects.create(
            speciality_name='Cardiology',
            description='Heart-related conditions and treatments'
        )

        # Создаем тестовую услугу
        cls.service = Service.objects.create(
            title='Heart Checkup',
            description='A thorough heart checkup',
            price=100  # Указываем цену, чтобы избежать ошибок
        )


