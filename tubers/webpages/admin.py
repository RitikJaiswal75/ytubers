from django.contrib import admin
from .models import Slider, Team, Aboutpage
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src={} width="40"/>'.format(object.photo.url))

    list_display=('id','myphoto','first_name','role','created_date')
    list_display_links =('first_name',)
    search_fields=('first_name','role')
    list_filter=('role',)

class sliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src={} width="100"/>'.format(object.photo.url))
    list_display=('headline','myphoto','button_text')

class AboutpageAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src={} width="40"/>'.format(object.photo.url))
    list_display=('headline','myphoto')

admin.site.register(Slider,sliderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Aboutpage, AboutpageAdmin)