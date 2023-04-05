from django.urls import path
from . import views

# configure urls 
urlpatterns = [
    path('',views.index, name = 'index'),
    path('profile/', views.profile, name='profile'),
]