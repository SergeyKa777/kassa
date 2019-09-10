
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_pdf_view),
    path('1', views.control_panel),
    path('delet', views.delet),


]
