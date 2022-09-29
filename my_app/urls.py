
from django.urls import path
from my_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.signup, name='register'), 
    path('profile/<int:pk>/', views.profile, name='profile'), 
    path('createpost/', views.createpost, name='createpost'),    
    path('blocktest/', views.blocktest, name='blocktest'),    
    path('details/<int:pk>', views.post_detail, name='post-detail'),    
    path('login/', auth_views.LoginView.as_view(template_name = 'my_app/builtin-login.html'), name='loginpage'),    
    path('logout/', auth_views.LogoutView.as_view(template_name = 'my_app/builtin-logout.html'), name='logoutpage'),    
    path('plist/', views.PostListView.as_view(template_name = 'my_app/plist.html'), name='listpage'),    
    path('pdetail/<int:pk>/', views.PostDetailView.as_view(template_name = 'my_app/pdetail.html'), name='detailpage'),    
    path('create/', views.ClassCreatePost.as_view(), name='classcreatepost'),    
    path('update/<int:pk>/', views.ClassUpdatePost.as_view(template_name = 'my_app/post_update.html' ), name='classupdatepost'),    
    path('delete/<int:pk>/', views.ClassDeletePost.as_view(), name='classdeletepost'),    
    path('funcdelete/<int:pk>/', views.postdelete, name='func_delete'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


