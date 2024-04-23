from django.contrib import admin
from .models import Room, Topic

# Register the Room model with the admin site
admin.site.register(Room)

# Define a custom admin class for the Topic model
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

# Register the Topic model with the admin site using the custom admin class
admin.site.register(Topic, TopicAdmin)
