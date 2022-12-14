from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_cryptography.fields import encrypt

# Create your models here.


class Note(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = encrypt(models.CharField(max_length=100))
    recepty = encrypt(models.TextField(max_length=5000))
    lekarstwa = encrypt(models.TextField(max_length=5000))
    badania = encrypt(models.TextField(max_length=5000))
    wizyta = encrypt(models.TextField(max_length=5000))
    skierowanie = encrypt(models.TextField(max_length=5000))
    zalecenia = encrypt(models.TextField(max_length=5000))

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
