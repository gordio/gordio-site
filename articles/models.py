from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager


class Article(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(default=datetime.now)
    tags = TaggableManager()

    @models.permalink
    def get_absolute_url(self):
        return ('articles:view', (), {'slug': self.slug})

    def __str__(self):
        return self.title
