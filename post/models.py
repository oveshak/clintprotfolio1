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
    
class ExperienceandEducation(models.Model):
    TYPE_CHOICES=(
        ("Education","Education"),
        ("Experience","Experience")
    )
    type = models.CharField(max_length=40 ,choices=TYPE_CHOICES)
    in_name=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    date=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.type}"
    
class ExperienceandEducationResume(models.Model):
    TYPE_CHOICES=(
        ("EDUCATION","EDUCATION"),
        ("EXPRTIENCE","EXPRTIENCE")
    )
    type= models.CharField(max_length=40,choices=TYPE_CHOICES)
    desc=models.TextField()
    exprence=models.ManyToManyField(ExperienceandEducation)
    def __str__(self):
        return f"{self.type}"
    
class Skill(models.Model):
    TYPE_CHOICES=(
        ("Personal","Personal"),
        ("Professional","Professional")
    )
    type= models.CharField(max_length=40,choices=TYPE_CHOICES)
    title=models.CharField(max_length=30)
    parsentage=models.IntegerField()
    def __str__(self):
        return f"{self.type}"
    
class SkillResume(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    skill=models.ManyToManyField(Skill)
    def __str__(self):
        return f"{self.title}"