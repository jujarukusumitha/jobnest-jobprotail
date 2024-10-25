from django.urls import path
from . import views

urlpatterns = [
    path('', views.inserthrdetails),  # Root URL for inserting HR details
    path('get/', views.gethrdetails, name='selecturl'),  # Fetch or update HR details
    path('get/<int:no>/', views.gethrdetails, name='updatehrdetails'),  # Update URL without 'get/'
    path('db/del/<int:no>/', views.deletehrdetails, name='deletehrdetails'), # Delete specific HR details by ID
]
