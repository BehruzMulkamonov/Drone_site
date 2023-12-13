# Generated by Django 4.2.7 on 2023-11-18 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Country_origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Country_origin',
                'verbose_name_plural': 'Country_origins',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'postion',
                'verbose_name_plural': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Sensortype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Sensortype',
                'verbose_name_plural': 'Sensortypes',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_code', models.CharField(max_length=155)),
                ('name', models.CharField(max_length=155)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='spravchnik.region')),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
    ]
