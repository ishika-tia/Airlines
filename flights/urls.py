from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('flights', views.index, name='index'),
    path('passenger', views.passenger, name='passengers'),
    path('<int:id>', views.view_flight, name='view_flight'),
    path('<int:id>', views.view_passenger, name='view_passenger'),
    path('add/', views.add, name='add'),
    path('addp/', views.addp, name='addp'),
]
    