from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'date']
    search_fields = ['title', 'description']
    list_filter = ['date']