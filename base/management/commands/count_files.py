from django.core.management import BaseCommand

from base.models import File

class Command(BaseCommand):
    help = 'Count your <Files> objects'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write(self.style.SUCCESS(f'Files count: {File.objects.count()}'))
        except File.DoesNotExist:
            self.stdout.write(self.style.SUCCESS('Files count: 0'))