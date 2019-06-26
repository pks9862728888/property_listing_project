from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]
