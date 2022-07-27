from django.db import models

class Merchandise(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20, unique=True)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=120)
    description = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
