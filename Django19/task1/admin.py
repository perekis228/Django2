from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Post)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    fields = [('title', 'cost', 'size', 'age_limited'), 'description']
    search_fields = ('title',)
    list_filter = ('cost', 'size', 'age_limited')
