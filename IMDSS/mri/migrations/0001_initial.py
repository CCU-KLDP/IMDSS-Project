# Generated by Django 2.0.2 on 2020-05-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mri_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=20, null=True)),
                ('doctor_id', models.CharField(max_length=20, null=True)),
                ('mri_image', models.ImageField(upload_to='mri/images')),
            ],
        ),
    ]