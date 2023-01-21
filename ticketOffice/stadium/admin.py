from django.contrib import admin
from .models import Stadium, Section, Seat

# Register your models here.

class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'province', 'capacity')
    list_display_links = ('name', 'city', 'province')
    search_fields = ('name', 'city', 'province')
    list_per_page = 25
    
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_number', 'capacity', 'remain_count', 'stadium')
    
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'section', 'reserved')
    
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Seat, SeatAdmin)
