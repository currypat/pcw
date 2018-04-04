# patcurryworks.com/blog/models.py
from django.db import models


class Post(models.Model):
    text = models.TextField(blank=True, null=True)
