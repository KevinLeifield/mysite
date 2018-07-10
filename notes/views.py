from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Note

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = "notes_list"

    def get_queryset(self):
        return Note.objects.order_by("id")



class DetailView(generic.DetailView):
    model = Note
    template_name = 'notes/detail.html'


def add(request):
    new = Note(text=request.POST['note'])
    new.save()
    return HttpResponseRedirect(reverse('notes:detail', args=(new.id, )))