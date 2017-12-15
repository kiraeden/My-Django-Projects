# Generated by Django 2.0 on 2017-12-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('current_project', models.CharField(max_length=50)),
                ('working', models.BooleanField()),
                ('clapper', models.BooleanField()),
                ('dac', models.BooleanField()),
                ('pmd', models.BooleanField()),
                ('in_use_for', models.CharField(max_length=50)),
                ('checked_out', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('sspec', models.CharField(max_length=10)),
            ],
        ),
    ]
