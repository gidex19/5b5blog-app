
from django.urls import path
from my_app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.signup, name='register'),    
    path('blocktest/', views.blocktest, name='blocktest'),    
    path('details/<int:pk>', views.post_detail, name='post-detail'),    
    path('login/', auth_views.LoginView.as_view(template_name = 'my_app/builtin-login.html'), name='loginpage'),    
    path('logout/', auth_views.LogoutView.as_view(template_name = 'my_app/builtin-logout.html'), name='logoutpage'),    
]

