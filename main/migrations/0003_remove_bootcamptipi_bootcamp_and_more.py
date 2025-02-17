# Generated by Django 5.1.6 on 2025-02-17 13:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_faq_alter_təlimlər_bootcamp_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootcamptipi',
            name='bootcamp',
        ),
        migrations.AddField(
            model_name='bootcamptipi',
            name='bootcamp_type',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='bootcamp_type', to='main.bootcamps'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='təlimlər',
            name='bootcamp_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='təlimlər', to='main.bootcamptipi'),
        ),
    ]
