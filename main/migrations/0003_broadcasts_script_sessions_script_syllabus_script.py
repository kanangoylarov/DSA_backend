# Generated by Django 5.1.6 on 2025-02-13 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_broadcasts_scripts_sessions_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcasts',
            name='script',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='broadcasts', to='main.scripts'),
        ),
        migrations.AddField(
            model_name='sessions',
            name='script',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='main.scripts'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='script',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='syllabi', to='main.scripts'),
        ),
    ]
