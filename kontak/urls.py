from django.urls import path
from .views import kontak_view
from django.shortcuts import render

urlpatterns = [
    path('', kontak_view, name='kontak'),
    path('thanks/', lambda r: render(r, 'thanks.html'), name='thanks'),
]
