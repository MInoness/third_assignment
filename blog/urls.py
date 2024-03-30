from django.urls import path
from . import views

urlpatterns = [
    path('blog/create', views.create, name ='create'),
    path('blog/', views.detail, name='detail'),
    ]
