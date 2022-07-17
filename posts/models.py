from django.db import models

#  create a model for the posts
class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


