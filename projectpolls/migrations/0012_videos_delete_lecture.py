# Generated by Django 4.2.1 on 2023-09-15 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpolls', '0011_qchp_que_alter_option_questions_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('video_url', models.CharField(max_length=300)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpolls.subject')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpolls.chapters')),
            ],
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
