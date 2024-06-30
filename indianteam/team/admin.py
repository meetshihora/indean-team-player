from django.contrib import admin

# Register your models here.
from team.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'GarsiNumber')
    
admin.site.register(Team)