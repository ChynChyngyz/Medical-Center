from django.test import TestCase
from django.urls import reverse
from services.models import Service


class ServiceViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Создание тестовых данных для тестов.
        """
        # Создаем тестовую услугу
        cls.service = Service.objects.create(
            title='Cardiology Consultation',
            description='A thorough heart check-up.',
            price=150.00
        )

    def test_service_list_view(self):
        """
        Тестируем представление списка медицинских услуг.
        """
        # Отправляем GET запрос на представление списка услуг
        response = self.client.get(reverse('services:service_list'))

        # Проверяем статус код ответа
        self.assertEqual(response.status_code, 200)

        # Проверяем, что название нашей услуги отображается в ответе
        self.assertContains(response, self.service.title)
