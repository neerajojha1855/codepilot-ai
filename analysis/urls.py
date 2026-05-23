from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('analyze/', views.analyze_repo, name='analyze_repo'),
    path('repo/<int:pk>/', views.repo_detail, name='repo_detail'),
    path('repo/<int:pk>/delete/', views.delete_repo, name='delete_repo'),
]
