from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('analyze/', views.analyze_repo, name='analyze_repo'),
    path('repo/<int:pk>/', views.repo_detail, name='repo_detail'),
    path('repo/<int:pk>/delete/', views.delete_repo, name='delete_repo'),
    path('404/', views.custom_404, {'exception': None}, name='preview_404'),  # Preview route
    path('403/', views.custom_403, {'exception': None}, name='preview_403'),  # Preview route
    re_path(r'^.*$', views.custom_404, {'exception': None}),  # Catch-all for 404
]
