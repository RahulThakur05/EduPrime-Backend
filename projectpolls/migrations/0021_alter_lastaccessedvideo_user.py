# Generated by Django 4.2.1 on 2023-09-28 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0020_alter_lastaccessedvideo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastaccessedvideo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpolls.user'),
        ),
    ]