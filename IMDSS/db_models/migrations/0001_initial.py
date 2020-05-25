# Generated by Django 3.0.2 on 2020-05-25 13:43

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
                ('dep_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('dep_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('create_time', models.CharField(max_length=60, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emr_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmrId', models.CharField(max_length=50, unique=True)),
                ('Sequence', models.IntegerField()),
                ('EmrContent', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('medical_condition', models.CharField(max_length=200)),
                ('birth', models.DateField()),
                ('identification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Xsl_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('XslId', models.CharField(max_length=50)),
                ('Sequence', models.IntegerField()),
                ('XslContent', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Tpr_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100, null=True)),
                ('value', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('create_date', models.CharField(max_length=100, null=True)),
                ('create_time', models.CharField(max_length=100, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Patient', to_field='patient_id')),
                ('resident_doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='OutPatient_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('EmrId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Emr_data', to_field='EmrId')),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Department')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outpatient_doctor', to='db_models.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outpatient_patients', to='db_models.Patient', to_field='patient_id')),
            ],
        ),
        migrations.CreateModel(
            name='Memo_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=6000)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='memo_doctor', to='db_models.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='memo_patients', to='db_models.Patient', to_field='patient_id')),
            ],
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EncounterId', models.CharField(max_length=20)),
                ('OrderId', models.CharField(max_length=100)),
                ('MedPRS', models.CharField(max_length=100)),
                ('dose', models.IntegerField()),
                ('doseUnit', models.CharField(max_length=20)),
                ('exeDt', models.CharField(max_length=15)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.Patient', to_field='patient_id')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('medical_condition', models.CharField(max_length=200)),
                ('time_frame', models.CharField(max_length=50, null=True)),
                ('cuis_list', models.CharField(max_length=2500)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dep_evaluation', to='db_models.Department')),
            ],
        ),
    ]
