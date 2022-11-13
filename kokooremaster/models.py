from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=64)

class Template(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    fieldCount = models.IntegerField() 
    field = models.JSONField() #this field doesn't appear in other circumstances. so, rather than creating original class, just add JSON field.
    tag = models.JSONField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.FileField()
    published_date = models.TimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Result(models.Model):
    whole_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    original = models.ForeignKey(Template, on_delete=models.CASCADE)
    img = models.FileField()
    published_date = models.TimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# Create your models here.
