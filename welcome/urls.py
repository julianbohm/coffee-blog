# welcome/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('login/', views.login_view, name='login'),    # URL for login view
   path('register/', views.register, name='register'), # URL for registration view
   path('', views.login_view, name='welcome'),
]        