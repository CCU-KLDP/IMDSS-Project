# Generated by Django 2.0.2 on 2020-04-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200315_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_data',
        ),
    ]
