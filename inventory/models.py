from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    unit = models.CharField(max_length=255, default='item')
    count = models.IntegerField()

    def __str__(self):
        return self.name
