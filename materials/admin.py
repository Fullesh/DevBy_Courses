from django.contrib import admin

from materials.models import Lession, Course


# Register your models here.

@admin.register(Lession)
class LessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'URL')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
