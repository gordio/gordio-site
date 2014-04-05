from datetime import datetime
from django.contrib.syndication.views import Feed
from .models import Article


class ArticlesFeed(Feed):
    title = 'Gordio Articles'
    description = 'Crazy Web/Django Developer'
    link = '/'

    def items(self):
        return Article.objects.filter(
            pub_date__lte=datetime.now()
        ).order_by('-pub_date')

    def item_pubdate(self, item):
        return item.pub_date

    def item_updateddate(self, item):
        return item.edited_date
