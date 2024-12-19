from django.test import TestCase
from speciality.models import Speciality
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import SpecialityForm


class SpecialityFormTest(TestCase):
    def test_speciality_form_valid(self):
        """
        Тест на создание специализации через форму.
        Проверяем, что форма создаст объект при валидных данных.
        """
        form_data = {
            'speciality_name': 'Cardiology',
            'description': 'Heart related issues',
        }
        form = SpecialityForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Создаем объект через форму
        speciality = form.save()

        # Проверяем, что объект был сохранен в базе данных
        self.assertEqual(Speciality.objects.count(), 1)
        self.assertEqual(speciality.speciality_name, 'Cardiology')
        self.assertEqual(speciality.description, 'Heart related issues')

    def test_speciality_form_invalid(self):
        """
        Тест на создание специализации через форму.
        Проверяем, что форма не создаст объект при невалидных данных.
        """
        form_data = {
            'speciality_name': '',  # Пустое поле, что делает форму невалидной
            'description': '',
        }
        form = SpecialityForm(data=form_data)
        self.assertFalse(form.is_valid())  # Форма не должна быть валидной


class SpecialityCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Создание данных для тестов: специализация.
        """
        cls.speciality = Speciality.objects.create(
            speciality_name='Cardiology',
            description='Heart related issues'
        )

    def test_speciality_creation(self):
        """
        Тестируем создание новой специализации.
        """
        speciality = Speciality.objects.get(speciality_name='Cardiology')
        self.assertEqual(speciality.speciality_name, 'Cardiology')
        self.assertEqual(speciality.description, 'Heart related issues')


class SpecialityImageTest(TestCase):
    def test_speciality_image(self):
        """
        Тест на загрузку изображения для специализации.
        Проверяем, что изображение сохраняется и его имя корректно.
        """
        # Создаем объект изображения для теста
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        speciality = Speciality.objects.create(
            speciality_name='Cardiology',
            description='Heart related issues',
            image=image,  # Загрузка тестового изображения
        )

        # Проверяем, что изображение действительно сохранено в директории 'image_speciality/'
        self.assertTrue(speciality.image.name.startswith('image_speciality/test_image'))

        # Проверяем, что имя изображения начинается с 'test_image'
        self.assertTrue(speciality.image.name.split('/')[-1].startswith('test_image'))
