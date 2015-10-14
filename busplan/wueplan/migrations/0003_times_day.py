# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wueplan', '0002_auto_20150422_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='day',
            field=models.CharField(default='NO', max_length=2, choices=[(b'NO', b'Normal'), (b'SA', b'Samstag'), (b'SU', b'Sonntag/Feiertag')]),
            preserve_default=False,
        ),
    ]
