from django.contrib import admin
from project.students.models import (
    Navigators,
    Students,
    ScheduleAvailability,
    Meeting,
    Task,
    Upload,
)

# Register your models here.
admin.site.register(Navigators)
admin.site.register(Students)
admin.site.register(ScheduleAvailability)
admin.site.register(Meeting)
admin.site.register(Task)
admin.site.register(Upload)
