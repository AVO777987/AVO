# Generated by Django 3.0.5 on 2020-04-15 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoserver', '0014_auto_20200415_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='job',
            name='command_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoserver.Command_line'),
        ),
        migrations.AlterField(
            model_name='job',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoserver.Storage'),
        ),
        migrations.AlterField(
            model_name='job',
            name='video_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoserver.Video_source'),
        ),
        migrations.AlterIndexTogether(
            name='backup',
            index_together={('videoserver', 'active')},
        ),
    ]