from django.db import models

# Create your models here.
class stats(models.Model):
   number = models.IntegerField(null=True)

   def __str__(self):
        return f"{self.id}: {self.number} "
   

class calstats(models.Model):
   number = models.IntegerField(null=True)

   def __str__(self):
        return f"{self.id}: {self.number} "
