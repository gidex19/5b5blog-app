
from django.urls import path
from my_app import views
urlpatterns = [
    path('home/', views.home, name='homepage'),
    path('register/', views.signup, name='register'),    
    path('blocktest/', views.blocktest, name='blocktest'),    
    path('details/<int:pk>', views.post_detail, name='post-detail'),    
]


