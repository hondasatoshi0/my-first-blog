from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list')
    path('iot/', views.iot, name='iot')
    ]