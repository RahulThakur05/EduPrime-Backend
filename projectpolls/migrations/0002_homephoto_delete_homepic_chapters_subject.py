# Generated by Django 4.2.1 on 2023-08-12 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(default='', upload_to='images')),
                ('subname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectpolls.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='HomePic',
        ),
        migrations.AddField(
            model_name='chapters',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectpolls.subject'),
        ),
    ]
