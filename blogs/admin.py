from django.contrib import admin
from .models import Tag, Blog, Entry

# Register your models here.
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Entry)

