# Generated by Django 3.0.5 on 2020-04-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0010_auto_20200415_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='id',
            field=models.IntegerField(default='0000', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='name',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='videoserver',
            field=models.CharField(default='%.%.%.%', max_length=128, unique=True),
        ),
    ]
