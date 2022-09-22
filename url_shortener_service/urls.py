from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create_url),
    path('<str:shortened_url_path>/', views.redirect_shortened_url),
]
