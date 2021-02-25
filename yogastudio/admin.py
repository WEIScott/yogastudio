from django.contrib import admin
from .models import Yogacourse

@admin.register(Yogacourse)
class YogacourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'instructor', 'datetime_start', 
                        'start_end_time', 'level')
    list_filter = ('instructor', 'level', 'datetime_start')
