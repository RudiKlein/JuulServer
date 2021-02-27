from django.urls import path
from . import views

app_name = 'userentry'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('doelstellingen/<int:pk>/', views.DoelstellingenView.as_view(), name='doelstellingen'),
    path('persoonsgegevens/<int:pk>/', views.DetailView.as_view(), name='persoonsgegevens'),

]