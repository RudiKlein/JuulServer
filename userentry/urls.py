from django.urls import path
from . import views

app_name = 'userentry'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('doelstellingen/<int:pk>/', views.DoelstellingenView.as_view(), name='doelstellingen'),
    path('scorekaart/<int:pk>/', views.ScorekaartView.as_view(), name='scorekaart'),
    path('persoonsgegevens/<int:pk>/', views.PersoonsgegevensView.as_view(), name='persoonsgegevens'),

]