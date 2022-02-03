# Generated by Django 4.0.1 on 2022-02-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('intakeName', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
        ),
    ]