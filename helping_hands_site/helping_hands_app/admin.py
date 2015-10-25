from django.contrib import admin
from helping_hands_app.models import Event
from helping_hands_app.models import Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('event_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['event_text']
    date_hierarchy = 'pub_date'

admin.site.register(Event, EventAdmin)
