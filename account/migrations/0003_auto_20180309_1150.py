# Generated by Django 2.0.1 on 2018-03-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180309_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login_time',
            field=models.DateTimeField(),
        ),
    ]
