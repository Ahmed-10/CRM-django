from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated_at = datetime.now()
        return super(Lead, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lead:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
