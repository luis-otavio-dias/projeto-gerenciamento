from django.contrib import admin
from students.models import Navigators, Students, ScheduleAvailability, Meeting

# Register your models here.
admin.site.register(Navigators)
admin.site.register(Students)
admin.site.register(ScheduleAvailability)
admin.site.register(Meeting)
