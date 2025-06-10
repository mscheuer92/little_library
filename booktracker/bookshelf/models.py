from django.db import models

# Create Book Model

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField()
    genre = models.CharField(max_length=50, null=True, blank=True)
    read = models.BooleanField()
    year_read = models.IntegerField(null=True, blank=True)
    

    def __str__(self): # method to return a string representation of the model object
        return self.title
