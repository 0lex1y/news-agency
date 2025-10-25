from django.conf import settings
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
    publisher = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='newspapers')

    def __str__(self):
        return f'{self.title} ({self.topic} - {self.published_date})'


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'
