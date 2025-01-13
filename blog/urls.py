from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),  
]