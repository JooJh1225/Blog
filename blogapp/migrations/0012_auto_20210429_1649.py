# Generated by Django 3.1.7 on 2021-04-29 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20210429_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 49, 16, 585069, tzinfo=utc)),
        ),
    ]
