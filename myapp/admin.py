from django.contrib import admin
from .models import task
# Register your models here.
@admin.register(task)
class Taskadmin(admin.ModelAdmin):
	list_display = ['title','description','created','date_completed','important','user']
	readonly_fields = ('created',)