# Generated by Django 4.2.1 on 2023-08-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0004_subphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
            ],
        ),
    ]
