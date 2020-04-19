# Generated by Django 3.0.4 on 2020-04-19 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_Record', models.CharField(choices=[('Prescription', 'Prescription'), ('Bloodtest', 'Bloodtest'), ('X_Ray', 'X-Ray'), ('AIDS_Test', 'AIDS Test'), ('Aldosterone_in_Urine', 'Aldosterone in Urine'), ('Eye_Angiogram', 'Eye Angiogram'), ('Electroencephalogram ', 'Electroencephalogram '), ('ECT', 'ECT')], max_length=100, null=True)),
                ('file', models.FileField(null=True, upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.TextField()),
                ('comment', models.CharField(max_length=250, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eprescription', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eprescription', to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='users.Doctor')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
