from django.urls import path
from . import views

urlpatterns = [
    path('api/people/', views.api_posts, name='home'),
    path('api/people/<int:pk>/', views.api_posts_detail, name='pk'),
]