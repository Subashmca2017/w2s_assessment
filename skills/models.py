from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Skills(models.Model):
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_obj')
    skills = models.CharField(max_length=50, default='Test')
    percentage = models.IntegerField()

    def __str__(self):
        return self.user_obj.username

    class Meta:
        ordering = ('skills',)