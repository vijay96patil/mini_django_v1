# Create your models here.
"""
ORM - Object Relational Mapper
models.CharField  :: limiting characters
models.TextField :: defining limitless characters
models.DateTimeField  :: timestamp
"""


from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    #breakpoint()
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __str__(self):
        return self.published_date