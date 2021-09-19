from django.db import models

# Create your models here.

class Laptop(models.Model):
    name=models.CharField(max_length=32)
    company=models.CharField(max_length=32)
    ram=models.CharField(max_length=20)
    rom=models.IntegerField()
    price=models.FloatField()
    processor=models.CharField(max_length=32)
    document=models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
