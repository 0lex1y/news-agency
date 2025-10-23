from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Topics(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='newspapers')
    publisher = models.ManyToManyField('Redactor', related_name='newspapers')

    def __str__(self):
        return f'{self.title} ({self.topic} - {self.publisher})'


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'
