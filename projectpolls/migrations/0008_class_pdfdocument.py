# Generated by Django 4.2.1 on 2023-08-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0007_remove_lecture_chplect_alter_lecture_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpolls.class')),
            ],
        ),
    ]