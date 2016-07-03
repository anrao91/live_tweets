from django.contrib import admin
from app.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('hashtag', 'text', 'created_at', )

admin.site.register(Tweet, TweetAdmin)
