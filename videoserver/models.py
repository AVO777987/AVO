from django.db import models


class Main_menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    par_dir = models.CharField(max_length=50)
    sort = models.IntegerField(default='0')


class Job(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    active = models.IntegerField(default='0', db_index=True)
    name = models.CharField(max_length=64)
    videoserver = models.CharField(max_length=128, default='%.%.%.%')
#    command_line = models.CharField(max_length=36, default='87ea865c-7028-11e2-b34f-00262d167feb', db_index=True)
    command_line = models.ForeignKey('Command_line', on_delete=models.CASCADE)
#    video_source = models.CharField(max_length=36, default='286beed5-702a-11e2-b34f-00262d167feb', db_index=True)
    video_source = models.ForeignKey('Video_source', on_delete=models.CASCADE)
    record_time = models.IntegerField(default='180', db_index=True)
    intersection = models.IntegerField(default='2', db_index=True)
    transcode = models.CharField(max_length=256, default='')
#    storage = models.CharField(max_length=36, default='177c0150-6ad4-11e2-8e22-00262d167feb', db_index=True)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
#    schedule = models.CharField(max_length=36, default='308b5899-71bc-11e2-b935-00262d167feb', db_index=True)
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    take_time = models.DateTimeField(db_index=True)
    take_videoserver = models.CharField(max_length=128, default='192.168.0.0')
    take_uuid = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', db_index=True)

    class Meta:
        unique_together = ['name', 'videoserver']
        index_together = ['active', 'videoserver', 'record_time', 'intersection']


class Storage(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    size = models.IntegerField(default='7')
    size_add_hours = models.IntegerField(default='0')
    backup = models.IntegerField(default='0')
    backup_size = models.IntegerField(default='28')


class Video_source(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    url = models.CharField(max_length=512, default='rtsp://user:password@ip:554/h2')
    options = models.CharField(max_length=512)


class Backup(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    videoserver = models.CharField(max_length=128, default='%.%.%.%')
    path = models.CharField(max_length=256, default='/backup/disk1', db_index=True)
    min_free_space_percent = models.IntegerField(default='8')
    active = models.IntegerField(default='0')

    class Meta:
        index_together = ['videoserver', 'active']


class Calendar(models.Model):
    year = models.IntegerField(default='0000', primary_key=False)
    name = models.CharField(max_length=4)
    value = models.IntegerField(default='0')

    class Meta:
        unique_together = ['year', 'name']


class Command_line(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    value = models.CharField(max_length=512, default='/opt/record/record.py -u %url% -t %time% -o %media%')


class Drive(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    videoserver = models.CharField(max_length=128, default='%.%.%.%')
    path = models.CharField(max_length=256, default='/archive', db_index=True)
    min_free_space_percent = models.FloatField(default='10')
    active = models.IntegerField(default='0')

    class Meta:
        index_together = ['videoserver', 'active']


class Event(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    videoserver = models.CharField(max_length=128)
    job = models.CharField(max_length=36)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        index_together = [['begin_time', 'end_time'], ['videoserver', 'job']]


class Log(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    time = models.DateTimeField(auto_now=True)
    table = models.CharField(max_length=64)
    action = models.IntegerField
    fields = models.CharField(max_length=500, default='NULL', null=True)
    oldvalues = models.CharField(max_length=500, default='NULL', null=True)
    newvalues = models.CharField(max_length=500, default='NULL', null=True)


class Schedule(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    calendar = models.CharField(max_length=4, default='0000', db_index=True)
    week_days = models.CharField(max_length=7, default='1111111', db_index=True)
    hours = models.CharField(max_length=24, default='111111111111111111111111', db_index=True)
    event_second_before = models.IntegerField(default='NULL', null=True)
    event_second_after = models.IntegerField(default='NULL', null=True)


class Smtp_server(models.Model):
    id = models.CharField(max_length=36, default='00000000-0000-0000-0000-000000000000', primary_key=True)
    videoserver = models.CharField(max_length=128, default='%.%.%.%', unique=True)
    active = models.IntegerField(default='1')
    host = models.CharField(max_length=64, default='localhost')
    port = models.IntegerField(default='30000')
    encoding = models.CharField(max_length=64, default='windows-1251')

