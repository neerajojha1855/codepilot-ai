from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django_q.tasks import async_task
from .models import Repository, FileAnalysis
# We no longer import analyze_repository directly since it's a background task
# from .services.analyzer import analyze_repository

def dashboard(request):
    repositories = Repository.objects.all().order_by('-created_at')
    context = {
        'repositories': repositories,
    }
    return render(request, 'analysis/dashboard.html', context)


def repo_detail(request, pk):
    repo = get_object_or_404(Repository, pk=pk)
    files = repo.files.all()
    
    total_quality = sum(f.quality_score for f in files)
    avg_quality = total_quality / files.count() if files.count() > 0 else 0
    
    context = {
        'repo': repo,
        'files': files,
        'avg_quality': round(avg_quality, 1)
    }
    return render(request, 'analysis/repo_detail.html', context)


def analyze_repo(request):
    if request.method == "POST":
        github_url = request.POST.get('github_url')
        name = request.POST.get('name')
        owner = request.POST.get('owner')

        if github_url and name:
            repo = Repository.objects.create(
                name=name,
                github_url=github_url,
                owner=owner,
                status='PENDING'
            )
            # Enqueue the background task
            async_task('analysis.services.analyzer.process_repository_task', repo.pk)
            return redirect('dashboard')
    
    return redirect('dashboard')


def delete_repo(request, pk):
    if request.method == "POST":
        repo = get_object_or_404(Repository, pk=pk)
        repo.delete()
    return redirect('dashboard')
