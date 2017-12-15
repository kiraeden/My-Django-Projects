# Generated by Django 2.0 on 2017-12-06 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name', models.CharField(max_length=100)),
                ('spec_num', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HLTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epic', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=300)),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CommReq')),
            ],
        ),
        migrations.CreateModel(
            name='MLTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_section', models.CharField(max_length=50)),
                ('test_scenario_name', models.CharField(max_length=256)),
                ('test_scenario_notes', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=100)),
                ('fw_dev', models.BooleanField()),
                ('req_question', models.BooleanField()),
                ('tdd', models.CharField(max_length=100)),
                ('user_story', models.CharField(max_length=10)),
                ('product_spec', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('hltp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.HLTP')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Case_Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suite_name', models.CharField(max_length=100)),
                ('test_case_name', models.CharField(max_length=100)),
                ('automated', models.BooleanField()),
                ('new_test', models.BooleanField()),
                ('notes', models.CharField(max_length=200)),
                ('file_path', models.FilePathField()),
                ('mltp', models.ManyToManyField(to='main.MLTP')),
            ],
        ),
        migrations.CreateModel(
            name='Versions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Products')),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Versions'),
        ),
        migrations.AddField(
            model_name='commreq',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Model'),
        ),
    ]
