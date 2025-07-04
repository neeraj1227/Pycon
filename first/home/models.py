from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
#create  your models here

# User Model 
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
   
#Service Model

class Service(models.Model):
    icon=models.CharField(max_length=50, blank=True, null=True)
    title=models.CharField(max_length=250, blank=True, null=True)
    description=models.TextField()

    def __str__(self):
        return self.title
#Testimonail Model

class Testimonial(models.Model):
    image=models.CharField( max_length=255,blank=True, null=True)
    star_count=[
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rate = models.IntegerField( choices=star_count)
    name=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return f"{self.profession}-{self.profession}"


#FAQ Model

class FAQ(models.Model):
    question=models.CharField(max_length=255)
    answer=models.TextField()
    
    def __str__(self):
        return self.question


#ContactLog Details
class Contact_log(models.Model):
    name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField()
    action_time=models.DateTimeField(blank=True,null=True)
    is_error=models.BooleanField(default=False)
    is_success=models.BooleanField(default=False)
    error_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.email
    

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    joined_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.first_name

# class Blog(models.Model):
#     blog_image=models.CharField(max_length=255,null=True,blank=True)
#     category=models.CharField(max_length=255,null=True,blank=True)
#     title=models.CharField(max_length=255)
#     # author=models.CharField(max_length=255)
#     author=models.ForeignKey(Author, on_delete=models.PROTECT)
#     create_at=models.DateTimeField(default=timezone.now)
#     content=models.TextField()
class blog_post(models.Model):
    blog_image=models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author, on_delete=models.PROTECT)
    create_at=models.DateTimeField(default=timezone.now)
    content=models.TextField()


    def __str__(self):
        return self.title
