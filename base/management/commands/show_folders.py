from typing import Any
from django.core.management import BaseCommand

from base.models import File, Folder

class Command(BaseCommand):
    help = 'Show you all folder and files. (JSON)'

    def handle(self, *args: Any, **options: Any) -> str | None:

        result = {}

        try:
            folders = Folder.objects.all()
            for folder in folders:
                result[folder.name] = folder.files.values_list('file_name', flat=True)
            if not folders:
                self.stdout.write(self.style.ERROR('No folders found'))
            else:
                self.stdout.write(self.style.SUCCESS(f'{result}'))
        except Folder.DoesNotExist:
            self.stdout.write(self.style.ERROR('Folder.DoesNotExist occured.'))