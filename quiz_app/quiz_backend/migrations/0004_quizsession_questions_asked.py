# Generated by Django 5.1.4 on 2024-12-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_backend', '0003_quizsession_start_time_quizsession_time_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='questions_asked',
            field=models.ManyToManyField(blank=True, to='quiz_backend.question'),
        ),
    ]
