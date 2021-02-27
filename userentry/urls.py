from django.urls import path
from . import views

app_name = 'userentry'
urlpatterns = [
    path('testme', views.IndexView.as_view(), name='index'),
    path('detail', views.detail, name='index'),
]