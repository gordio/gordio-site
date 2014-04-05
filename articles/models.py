from datetime import datetime
from django.db import models
from taggit.managers import TaggableManager


class Article(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=25000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(default=datetime.today)
    tags = TaggableManager()

    @property
    def description(self):
        try:
            desc = self.content.split('\n')[0]
        except Exception:
            desc = self.content
        return desc

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles:view', (), {'slug': self.slug})
