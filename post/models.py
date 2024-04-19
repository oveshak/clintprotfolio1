from django.db import models

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=40)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='heroImage/')
    def __str__(self):
        return f"{self.title}"
    
class About(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    def __str__(self):
        return f"{self.title}"
    
class Blog(models.Model):
    image=models.ImageField(upload_to="blog/")
    title=models.CharField(max_length=100)
    date=models.DateField()
    type=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.type}"