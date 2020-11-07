
from django.contrib import admin
from mysite.models import Playlist, Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'vid', 'plist')

admin.site.register(Playlist)
admin.site.register(Video, VideoAdmin)