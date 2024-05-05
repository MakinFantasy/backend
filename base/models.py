import uuid

from django.db import models
from django.contrib.auth.models import User
from datetime import timezone
from django.utils import timezone
from simple_history.models import HistoricalRecords


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True, blank=True, default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Tags'


class File(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    file_file = models.FileField(upload_to='files/')
    description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, default=timezone.now)
    file_type = models.CharField(max_length=20, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.file_name}, {self.description}"

    class Meta:
        verbose_name_plural = "Files"


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    files = models.ManyToManyField(File, blank=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Categories"


class Folder(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    files = models.ManyToManyField(File, blank=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Folders"
    