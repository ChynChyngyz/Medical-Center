# users/management/commands/create_admin.py
import os
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Создание суперпользователя из переменных окружения'

    def handle(self, *args, **options):
        email = os.getenv('ADMIN_EMAIL')
        first_name = os.getenv('ADMIN_FIRST_NAME')
        last_name = os.getenv('ADMIN_LAST_NAME')
        password = os.getenv('ADMIN_PASSWORD')

        if not (email and first_name and last_name and password):
            self.stdout.write(self.style.ERROR('Отсутствуют необходимые переменные окружения'))
            return

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'is_staff': True,
                'is_superuser': True,
            },
        )
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Суперпользователь {email} успешно создан.'))
        else:
            self.stdout.write(self.style.WARNING(f'Суперпользователь с email {email} уже существует.'))
