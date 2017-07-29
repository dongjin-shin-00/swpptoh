from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
