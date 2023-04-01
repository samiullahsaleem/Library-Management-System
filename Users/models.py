from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True, unique=True, auto_created=True, editable=False)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=20)

    def __str__(self):
        return str(self.userId)
    
    class META:
        db_table = "User"
        verbose_name = "User"