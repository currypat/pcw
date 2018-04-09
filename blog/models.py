# patcurryworks.com/blog/models.py
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    post_slug = models.SlugField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.post_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
