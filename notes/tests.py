from django.test import TestCase
from .models import Note

# Create your tests here.
class NoteModelTests(TestCase):
    def test_note_available(self):
        