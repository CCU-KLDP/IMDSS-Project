# Generated by Django 2.0.2 on 2020-03-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='department',
            field=models.IntegerField(choices=[(1, 'dept1'), (2, 'dept2'), (3, 'dept3')], max_length=100),
        ),
    ]