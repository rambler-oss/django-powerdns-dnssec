# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerdns', '0033_auto_20161114_1442'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('name', 'type', 'content', 'domain')]),
        ),
    ]
