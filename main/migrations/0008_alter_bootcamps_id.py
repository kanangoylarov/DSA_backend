# Generated by Django 5.1.6 on 2025-02-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_bootcamptipi_bootcamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamps',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
