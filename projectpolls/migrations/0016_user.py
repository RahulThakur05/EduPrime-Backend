# Generated by Django 4.2.1 on 2023-09-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0015_alter_pyqdocument_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Num', models.CharField(max_length=12)),
                ('Pass', models.CharField(max_length=100)),
            ],
        ),
    ]