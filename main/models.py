from django.db import models

# Create your models here.
class Article(models.Model):
    title_en = models.CharField(max_length=200,)
    title_fr = models.CharField(max_length=200,)
    content_en = models.TextField()
    content_fr = models.TextField()
    publication_date = models.DateTimeField()

def __str__(self):
    return self.title