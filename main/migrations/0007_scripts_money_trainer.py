# Generated by Django 5.1.6 on 2025-02-14 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_broadcasts_link_alter_broadcasts_script_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scripts',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('work_location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='trainers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('script', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trainers', to='main.scripts')),
            ],
        ),
    ]
