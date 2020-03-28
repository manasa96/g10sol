from django.db import models

#Creating a model for making an entry in books database
class books(models.Model):
   Title = models.CharField(max_length = 50)
   Description = models.CharField(max_length = 1000)
   Author = models.CharField(max_length = 50)
   class Meta:
      db_table = "books"

