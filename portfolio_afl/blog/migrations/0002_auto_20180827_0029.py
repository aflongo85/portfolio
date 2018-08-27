# Generated by Django 2.1 on 2018-08-27 00:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='body_text',
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 27, 0, 29, 22, 830762, tzinfo=utc)),
        ),
    ]
