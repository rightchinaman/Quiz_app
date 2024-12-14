# Generated by Django 5.1.4 on 2024-12-14 04:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_backend', '0002_quizsession_current_question_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='quizsession',
            name='time_limit',
            field=models.IntegerField(default=300),
        ),
    ]
