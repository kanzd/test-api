from django.db import models

# Create your models here.


class Testmodel(models.Model):
    id = models.AutoField
    res = models.TextField(max_length=1000)
    def __str__(self):
        return str(self.id)