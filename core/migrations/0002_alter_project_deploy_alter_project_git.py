# Generated by Django 5.0.7 on 2024-07-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deploy',
            field=models.URLField(blank=True, max_length=100, verbose_name='Deploy'),
        ),
        migrations.AlterField(
            model_name='project',
            name='git',
            field=models.URLField(blank=True, max_length=100, verbose_name='Git'),
        ),
    ]
