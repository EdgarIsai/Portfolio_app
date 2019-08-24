from django.contrib import admin

from hostels.models import Hostel


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'publish', 'updated')
    list_filter = ('publish', 'updated')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'publish'
    ordering = ('publish',)

