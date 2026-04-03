from django.contrib import admin
from .models import VolleyPlayer


@admin.register(VolleyPlayer)
class VolleyPlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'name', 'date_joined', 'position', 'salary', 'contact_person')
    search_fields = ('name', 'position', 'contact_person')
