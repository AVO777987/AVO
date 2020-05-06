# Generated by Django 3.0.5 on 2020-04-17 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0024_auto_20200417_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='storage',
            field=models.ForeignKey(default='177c0150-6ad4-11e2-8e22-00262d167feb', on_delete=django.db.models.deletion.CASCADE, to='videoserver.Storage'),
        ),
        migrations.AlterField(
            model_name='job',
            name='video_source',
            field=models.ForeignKey(default='286beed5-702a-11e2-b34f-00262d167feb', on_delete=django.db.models.deletion.CASCADE, to='videoserver.Video_source'),
        ),
    ]