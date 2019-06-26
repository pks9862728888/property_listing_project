from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.IndexView.as_view(), name='listings'),
    path('<int:pk>/', views.listingView, name='listing'),
    path('search/', views.searchView, name='search')
]
