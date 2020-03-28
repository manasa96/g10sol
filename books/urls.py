from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.addbook, name='addbook'),
    path('search/', views.search, name='search'),
]
