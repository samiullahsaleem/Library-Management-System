from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorId = models.AutoField(primary_key=True, unique=True, null=False, auto_created=True)
    Author = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Author)
    class META:
        db_table = "Author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Book(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    BookId = models.AutoField(primary_key=True, unique=True, null=False, auto_created=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    isbn = models.CharField(max_length=100)
    def __str__(self):
        return str(self.title)