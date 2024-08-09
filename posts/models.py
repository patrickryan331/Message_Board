from django.db import models


class Post(models.Model):                                     #inheritance
    title = models.CharField(max_length=128)                  #lines 5-8: composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title