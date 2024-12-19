from django.test import TestCase
from django.urls import reverse
from appointments.models import Appointment
from services.models import Service
from users.models import Doctor
from services.models import Speciality


class AppointmentCreateViewTest(TestCase):

    def setUp(self):
        # Создаем сервис с обязательным полем price
        self.service = Service.objects.create(
            title='Heart Checkup',
            description='A thorough heart checkup',
            price=1000
        )

