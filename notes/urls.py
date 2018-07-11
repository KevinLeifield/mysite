from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from django.contrib import admin

admin.autodiscover()

app_name = 'notes'
urlpatterns = [
    # ex: /notes/
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
]