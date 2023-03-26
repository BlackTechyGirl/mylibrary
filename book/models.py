from enum import Enum, unique
from uuid import uuid4

from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-10-01')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genres')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return self.title


class Genre(models.Model):
    Genre_CHOICES = [
        ('SCI-FI', 'SCI'),
        ('FANTASY', 'FAN'),
        ('COMEDY', 'COM'),
        ('ROM-COM', 'ROM'),

    ]
    name = models.CharField(max_length=25, choices=Genre_CHOICES, default='COM')

    def __str__(self):
        return self.name


class Language(models.Model):
    LANGUAGE_CHOICES =[
        ('ENGLISH', 'ENG'),
        ('HAUSA', 'HAU'),
        ('FRENCH', 'FRE'),
        ('SPANISH', 'SPA'),
    ]
    name = models.CharField(max_length=25, choices=LANGUAGE_CHOICES, default='ENG')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B'),
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.imprint
