# Generated by Django 5.1.6 on 2025-02-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_bootcamps_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamps',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
