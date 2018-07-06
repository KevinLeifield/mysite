from django.contrib import admin

# testing
# Register your models here.
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note


admin.site.register(Note, NoteAdmin)