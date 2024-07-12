from django.db import models

# This will Store what type of Data will the django will store 

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro =models.TextField()
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ('-created_at',)