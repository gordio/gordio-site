# encoding: utf8
from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20140312_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
