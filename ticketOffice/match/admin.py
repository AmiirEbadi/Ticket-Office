from django.contrib import admin
from .models import Team, Match

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name')
    list_display_links = ('team_id', 'name')
    search_fields = ('name', )
    list_per_page = 25
    
    
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'stadium', 'time')
    list_display_links = ('team1', 'team2', 'stadium', 'time')
    search_fields = ('team1', 'team2', 'stadium')
    list_per_page = 25
    
    
admin.site.register(Match, MatchAdmin)  
admin.site.register(Team, TeamAdmin)