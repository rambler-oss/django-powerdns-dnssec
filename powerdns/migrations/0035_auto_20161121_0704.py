# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerdns', '0034_auto_20161115_1452'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('name', 'type', 'content', 'domain')]),
        ),
    ]
