import os
from dotenv import load_dotenv
from django.core.management import BaseCommand

from config.settings import BASE_DIR
from user.models import User

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("EMAIL"),
            first_name=os.getenv("FIRST_NAME"),
            last_name=os.getenv("LAST_NAME"),
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('PASSWORD'))
        user.save()
