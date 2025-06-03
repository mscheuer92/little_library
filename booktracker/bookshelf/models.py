from django.db import models

# Create Book Model

class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    read = models.BooleanField(default=False) # default False means the book is not read yet
    year_read = models.IntegerField() # null allows the field to be left blank


    def __str__(self): # method to return a string representation of the model object
        return self.title
