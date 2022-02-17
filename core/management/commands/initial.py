from django.core.management import BaseCommand
from core.models import User
from rolepermissions.roles import assign_role

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            email="admin@test.phsw",
            password='asdf'
        )
        assign_role(user, 'test_user')
