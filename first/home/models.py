from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
#create  your models here
class User(models.Model):
    first_name = models.CharField(max_length=50,default="name")
    last_name = models.CharField(max_length=50,default="name")
    location=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    video_url=models.URLField(blank=True,null=True)
    facebook_url=models.URLField(blank=True,null=True)
    instagram_url=models.URLField(blank=True,null=True)
    github_url=models.URLField(blank=True,null=True)
    linkedin_url=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.first_name
   


class Service(models.Model):
    icon=models.CharField(max_length=255, blank=True, null=True)
    title=models.CharField(max_length=50, blank=True, null=True)
    description=models.TextField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image=models.CharField( max_length=255,blank=True, null=True)
    rate = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    name=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return self.profession


