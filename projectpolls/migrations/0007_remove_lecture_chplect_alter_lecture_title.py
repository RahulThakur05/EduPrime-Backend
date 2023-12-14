# Generated by Django 4.2.1 on 2023-08-17 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0006_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='chplect',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpolls.chapters'),
        ),
    ]
