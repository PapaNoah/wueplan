# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wueplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lines',
            name='endstation',
            field=models.ForeignKey(related_name='lines_endstation', default=0, to='wueplan.Station'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lines',
            name='startstation',
            field=models.ForeignKey(related_name='lines_startstation', default=0, to='wueplan.Station'),
            preserve_default=False,
        ),
    ]
