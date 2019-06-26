from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboardView, name='dashboard'),
]
