
from django.urls import path
from my_app import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.signup, name='register'),
]

