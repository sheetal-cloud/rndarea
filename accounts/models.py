from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class profile(models.Model):
    hourly_rate=models.PositiveIntegerField()
    skill=models.CharField(max_length=200)
    cover_letter=models.FileField(upload_to='cover_letter/', max_length=254)
    tagline=models.CharField(max_length=100)
    Nationality=models.CharField(max_length=30)
    image=models.ImageField(upload_to='profile_image/', max_length=254)
    introduce_yourself=models.TextField(max_length=1000)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    
