# Generated by Django 3.0.5 on 2020-04-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.CharField(db_index=True, default='00000000-0000-0000-0000-000000000000', max_length=36, primary_key='true', serialize=False),
        ),
    ]