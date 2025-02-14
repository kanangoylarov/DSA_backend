# Generated by Django 5.1.6 on 2025-02-14 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_syllabus_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcasts',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='broadcasts',
            name='script',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast', to='main.scripts'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='information',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='script',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='syllabus', to='main.scripts'),
        ),
    ]
