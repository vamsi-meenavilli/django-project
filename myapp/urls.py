
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello),
    path('base/', views.base),
    path('register/', views.registration),
    
]
