from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate, name='generate'),
    path('login/', views.Login, name='Login'),
    path('signup/', views.signup, name='signup'),
]