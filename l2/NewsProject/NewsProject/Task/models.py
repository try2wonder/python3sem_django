from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.Choices('male','female')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
