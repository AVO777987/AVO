# Generated by Django 3.0.5 on 2020-04-15 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0005_auto_20200415_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='take_time',
        ),
    ]