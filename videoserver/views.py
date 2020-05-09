from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Main_menu, Job, Storage, Video_source, Backup, Calendar, Command_line, Drive, Event, Log, Schedule, \
    Smtp_server
import uuid
from _datetime import datetime

menu = Main_menu.objects.all().order_by('sort')


def list(request):
    category_url = request.GET.get('cat', '')
    for i in Main_menu.objects.all():
        if str(i.url) == category_url:
            title = Main_menu.objects.get(url=category_url).title
            url = Main_menu.objects.get(url=category_url).url
            break
        else:
            url = 'job'
            title = 'Камеры'

    if url == 'job':
        job = Job.objects.all()
        return render(request, 'list.html', {'menu': menu, 'job': job, 'title': title, 'url': url})
    if url == 'storage':
        storage = Storage.objects.all()
        return render(request, 'list.html', {'menu': menu, 'storage': storage, 'title': title, 'url': url})
    if url == 'video_source':
        video_source = Video_source.objects.all()
        return render(request, 'list.html', {'menu': menu, 'video_source': video_source, 'title': title, 'url': url})
    if url == 'backup':
        backup = Backup.objects.all()
        return render(request, 'list.html', {'menu': menu, 'backup': backup, 'title': title, 'url': url})
    if url == 'calendar':
        calendar = Calendar.objects.all()
        return render(request, 'list.html', {'menu': menu, 'calendar': calendar, 'title': title, 'url': url})
    if url == 'command_line':
        command_line = Command_line.objects.all()
        return render(request, 'list.html', {'menu': menu, 'command_line': command_line, 'title': title, 'url': url})
    if url == 'drive':
        drive = Drive.objects.all()
        return render(request, 'list.html', {'menu': menu, 'drive': drive, 'title': title, 'url': url})
    if url == 'smtp_server':
        smtp_server = Smtp_server.objects.all()
        return render(request, 'list.html', {'menu': menu, 'smtp_server': smtp_server, 'title': title, 'url': url})
    if url == 'logs':
        log = Log.objects.all()
        return render(request, 'list.html', {'menu': menu, 'log': log, 'title': title, 'url': url})
    if url == 'schedule':
        schedule = Schedule.objects.all()
        return render(request, 'list.html', {'menu': menu, 'schedule': schedule, 'title': title, 'url': url})


def edit(request):
    category_url = request.GET.get('cat', '')
    dev_id = request.GET.get('dev', '')
    for i in Main_menu.objects.all():
        if str(i.url) == category_url:
            title = Main_menu.objects.get(url=category_url).title
            url = Main_menu.objects.get(url=category_url).url
            break
        else:
            url = 'job'
            title = 'Камеры'
    if url == 'job':
        job = Job.objects.get(id=dev_id)
        video_source = Video_source.objects.all()
        command_line = Command_line.objects.all()
        schedule = Schedule.objects.all()
        storage = Storage.objects.all()
        return render(request, 'edit.html',
                      {'menu': menu, 'job': job, 'title': title, 'url': url, 'video_source': video_source,
                       'command_line': command_line, 'schedule': schedule, 'storage': storage})
    if url == 'storage':
        storage = Storage.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'storage': storage, 'title': title, 'url': url})
    if url == 'video_source':
        video_source = Video_source.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'video_source': video_source, 'title': title, 'url': url})
    if url == 'backup':
        backup = Backup.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'backup': backup, 'title': title, 'url': url})
    if url == 'calendar':
        calendar = Calendar.objects.all()
        return render(request, 'edit.html', {'menu': menu, 'calendar': calendar, 'title': title, 'url': url})
    if url == 'command_line':
        command_line = Command_line.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'command_line': command_line, 'title': title, 'url': url})
    if url == 'drive':
        drive = Drive.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'drive': drive, 'title': title, 'url': url})
    if url == 'smtp_server':
        smtp_server = Smtp_server.objects.all()
        return render(request, 'edit.html', {'menu': menu, 'smtp_server': smtp_server, 'title': title, 'url': url})
    if url == 'logs':
        log = Log.objects.all()
        return render(request, 'edit.html', {'menu': menu, 'log': log, 'title': title, 'url': url})
    if url == 'schedule':
        schedule = Schedule.objects.get(id=dev_id)
        return render(request, 'edit.html', {'menu': menu, 'schedule': schedule, 'title': title, 'url': url})


def update(request):
    action = request.GET.get('action')
    category_url = request.GET.get('cat')
    if category_url == 'job':
        job = Job()
        name = request.POST.get('name')
        if request.POST.get('videoserver') != "":
            videoserver = request.POST.get('videoserver')
        else:
            videoserver = job.videoserver
        video_source_id = request.POST.get('video_source_id')
        command_line_id = request.POST.get('command_line_id')
        schedule_id = request.POST.get('schedule_id')
        storage_id = request.POST.get('storage_id')
        if request.POST.get('record_time') != "":
            record_time = request.POST.get('record_time')
        else:
            record_time = job.record_time
        if request.POST.get('intersection') != "":
            intersection = request.POST.get('intersection')
        else:
            intersection = job.intersection
        transcode = request.POST.get('transcode')
        active = request.POST.get('active')
        if action == 'create':
            job.id = uuid.uuid1()
            job.name = name
            job.videoserver = videoserver
            job.command_line_id = command_line_id
            job.video_source_id = video_source_id
            job.schedule_id = schedule_id
            job.storage_id = storage_id
            job.record_time = record_time
            job.intersection = intersection
            job.transcode = transcode
            job.active = active
            job.take_time = datetime.now()
            job.save()

        if action == 'update':
            job_id = request.POST.get('job_id')
            Job.objects.filter(id=job_id).update(name=name,
                                                 videoserver=videoserver,
                                                 video_source_id=video_source_id,
                                                 command_line_id=command_line_id,
                                                 schedule_id=schedule_id,
                                                 storage_id=storage_id,
                                                 record_time=record_time,
                                                 intersection=intersection,
                                                 transcode=transcode,
                                                 active=active,
                                                 take_time=datetime.now())
        return HttpResponseRedirect("/videoserver/?сat=job")
    if category_url == 'drive':
        drive = Drive()
        if request.POST.get('videoserver') != "":
            videoserver = request.POST.get('videoserver')
        else:
            videoserver = drive.videoserver
        if request.POST.get('path') != "":
            path = request.POST.get('path')
        else:
            path = drive.path
        if request.POST.get('min_free_space_percent') != "":
            min_free_space_percent = request.POST.get('min_free_space_percent')
        else:
            min_free_space_percent = drive.min_free_space_percent
        active = request.POST.get('active')
        if action == 'create':
            drive.id = uuid.uuid1()
            drive.videoserver = videoserver
            drive.path = path
            drive.min_free_space_percent = min_free_space_percent
            drive.active = active
            drive.save()
        if action == 'update':
            drive_id = request.POST.get('drive_id')
            Drive.objects.filter(id=drive_id).update(videoserver=videoserver,
                                                     path=path,
                                                     min_free_space_percent=min_free_space_percent,
                                                     active=active)
        return HttpResponseRedirect("/videoserver/?cat=drive")
    if category_url == 'backup':
        backup = Backup()
        if request.POST.get('videoserver') != "":
            videoserver = request.POST.get('videoserver')
        else:
            videoserver = backup.videoserver
        if request.POST.get('path') != "":
            path = request.POST.get('path')
        else:
            path = backup.path
        if request.POST.get('min_free_space_percent') != "":
            min_free_space_percent = request.POST.get('min_free_space_percent')
        else:
            min_free_space_percent = backup.min_free_space_percent
        active = request.POST.get('active')
        if action == 'create':
            backup.id = uuid.uuid1()
            backup.videoserver = videoserver
            backup.path = path
            backup.min_free_space_percent = min_free_space_percent
            backup.active = active
            backup.save()
        if action == 'update':
            backup_id = request.POST.get('backup_id')
            Backup.objects.filter(id=backup_id).update(videoserver=videoserver,
                                                       path=path,
                                                       min_free_space_percent=min_free_space_percent,
                                                       active=active)
        return HttpResponseRedirect("/videoserver/?cat=backup")
    if category_url == 'video_source':
        video_source = Video_source()
        if request.POST.get('url') != "":
            url = request.POST.get('url')
        else:
            url = video_source.url
        if request.POST.get('options') != "":
            options = request.POST.get('options')
        else:
            options = video_source.options
        if action == 'create':
            video_source.id = uuid.uuid1()
            video_source.url = url
            video_source.options = options
            video_source.save()
        if action == 'update':
            video_source_id = request.POST.get('video_source_id')
            Video_source.objects.filter(id=video_source_id).update(url=url,
                                                                   options=options)
        return HttpResponseRedirect("/videoserver/?cat=video_source")
    if category_url == 'schedule':
        schedule = Schedule()
        if request.POST.get('calendar') != "":
            calendar = request.POST.get('calendar')
        else:
            calendar = schedule.calendar
        if request.POST.get('calendar') != "":
            week_days = request.POST.get('week_days')
        else:
            week_days = schedule.week_days
        if request.POST.get('hours') != "":
            hours = request.POST.get('hours')
        else:
            hours = schedule.hours
        if request.POST.get('event_second_before') != "":
            event_second_before = request.POST.get('event_second_before')
        else:
            event_second_before = schedule.event_second_before
        if request.POST.get('event_second_after') != "":
            event_second_after = request.POST.get('event_second_after')
        else:
            event_second_after = schedule.event_second_after
        if action == 'update':
            schedule_id = request.POST.get('schedule_id')
            Schedule.objects.filter(id=schedule_id).update(calendar=calendar,
                                                           week_days=week_days,
                                                           hours=hours,
                                                           event_second_before=event_second_before,
                                                           event_second_after=event_second_after)
        if action == 'create':
            schedule.id = uuid.uuid1()
            schedule.calendar = calendar
            schedule.week_days = week_days
            schedule.hours = hours
            schedule.event_second_before = event_second_before
            schedule.event_second_after = event_second_after
            schedule.save()
        return HttpResponseRedirect("/videoserver/?cat=schedule")
    if category_url == 'storage':
        storage = Storage()
        if request.POST.get('size') != "":
            size = request.POST.get('size')
        else:
            size = storage.size
        if request.POST.get('size_add_hours') != "":
            size_add_hours = request.POST.get('size_add_hours')
        else:
            size_add_hours = storage.size_add_hours
        if request.POST.get('backup') != "":
            backup = request.POST.get('backup')
        else:
            backup = storage.backup
        if request.POST.get('backup_size') != "":
            backup_size = request.POST.get('backup_size')
        else:
            backup_size = storage.backup_size
        if action == 'update':
            storage_id = request.POST.get('storage_id')
            Storage.objects.filter(id=storage_id).update(size=size,
                                                         size_add_hours=size_add_hours,
                                                         backup=backup,
                                                         backup_size=backup_size)
        if action == 'create':
            storage.id = uuid.uuid1()
            storage.size = size
            storage.size_add_hours = size_add_hours
            storage.backup = backup
            storage.backup_size = backup_size
            storage.save()
        return HttpResponseRedirect("/videoserver/?cat=storage")
    if category_url == 'command_line':
        command_line = Command_line()
        if request.POST.get('value') != "":
            value = request.POST.get('value')
        else:
            value = command_line.value
        if action == 'update':
            command_line_id = request.POST.get('command_line_id')
            Command_line.objects.filter(id=command_line_id).update(value=value)
        if action == 'create':
            command_line.id = uuid.uuid1()
            command_line.value = value
            command_line.save()
        return HttpResponseRedirect("/videoserver/?cat=command_line")

def create(request):
    category_url = request.GET.get('cat', '')
    for i in Main_menu.objects.all():
        if str(i.url) == category_url:
            title = Main_menu.objects.get(url=category_url).title
            url = Main_menu.objects.get(url=category_url).url
            break
        else:
            url = 'job'
            title = 'Камеры'

    if url == 'job':
        video_source = Video_source.objects.all()
        command_line = Command_line.objects.all()
        schedule = Schedule.objects.all()
        storage = Storage.objects.all()
        return render(request, 'create.html',
                      {'menu': menu, 'title': title, 'url': url, 'video_source': video_source,
                       'command_line': command_line, 'schedule': schedule, 'storage': storage})
    if url == 'drive':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})
    if url == 'backup':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})
    if url == 'video_source':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})
    if url == 'schedule':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})
    if url == 'storage':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})
    if url == 'command_line':
        return render(request, 'create.html', {'menu': menu, 'title': title, 'url': url})