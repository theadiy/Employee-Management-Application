from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('list', views.list, name='list'),
    path('detail', views.detail, name='detail')
]