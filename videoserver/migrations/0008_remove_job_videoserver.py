# Generated by Django 3.0.5 on 2020-04-15 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0007_job_take_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='videoserver',
        ),
    ]
