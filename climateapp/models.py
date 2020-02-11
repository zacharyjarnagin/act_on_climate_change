from django.db import models


class Politician(models.Model):
    state = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
