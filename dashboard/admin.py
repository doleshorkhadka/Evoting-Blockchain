from django.contrib import admin
from .models import Candidate, Feedback
# Register your models here.

admin.site.register(Candidate)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    # date_hierarchy = 'date'


admin.site.register(Feedback, FeedbackAdmin)