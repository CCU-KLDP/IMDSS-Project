# Generated by Django 2.0.2 on 2020-04-06 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('dep_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('create_time', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('medical_condition', models.CharField(max_length=200)),
                ('time_form', models.IntegerField()),
                ('cuis_list', models.CharField(max_length=500)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalized_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hospitalized_doctor', to='db_models.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedPRS', models.CharField(max_length=100)),
                ('OrderId', models.CharField(max_length=50)),
                ('begin_at', models.DateField()),
                ('end_at', models.DateField()),
                ('routePmName', models.CharField(max_length=50)),
                ('dose', models.IntegerField()),
                ('doseUnit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OutPatient_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outpatient_doctor', to='db_models.Doctor')),
                ('med_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Med')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('medical_condition', models.CharField(max_length=200)),
                ('birth', models.DateField()),
                ('identification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tpr_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField()),
                ('medical_record', models.IntegerField()),
                ('source', models.IntegerField()),
                ('BT_TA', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('HR', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('RR', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('DBP', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('SBP', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('login_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Patient', to_field='patient_id')),
                ('resident_doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='outpatient_data',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outpatient_patients', to='db_models.Patient', to_field='patient_id'),
        ),
        migrations.AddField(
            model_name='hospitalized_data',
            name='med_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Med'),
        ),
        migrations.AddField(
            model_name='hospitalized_data',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hospitalized_patients', to='db_models.Patient', to_field='patient_id'),
        ),
        migrations.AddField(
            model_name='hospitalized_data',
            name='tpr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Tpr_data'),
        ),
    ]