
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('1', views.render_pdf_view),
    path('', views.control_panel),
    path('delet', views.delet),
    path('pdf', views.ticket_gen),


]
