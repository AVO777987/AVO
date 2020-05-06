from django.contrib import admin
from .models import Job, Storage, Video_source, Backup, Calendar, Command_line, Drive, Event, Log, Schedule, Smtp_server, Main_menu

admin.site.register(Main_menu)
admin.site.register(Job)
admin.site.register(Storage)
admin.site.register(Video_source)
admin.site.register(Backup)
admin.site.register(Calendar)
admin.site.register(Command_line)
admin.site.register(Drive)
admin.site.register(Event)
admin.site.register(Log)
admin.site.register(Schedule)
admin.site.register(Smtp_server)

# Register your models here.
