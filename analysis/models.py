from django.db import models

class Repository(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ANALYZING', 'Analyzing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    name = models.CharField(max_length=255)
    github_url = models.URLField(max_length=500, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}/{self.name}" if self.owner else self.name


class FileAnalysis(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name="files")
    file_path = models.CharField(max_length=500)
    quality_score = models.IntegerField(default=100) # 0 to 100
    risk_score = models.IntegerField(default=0) # 0 to 100

    def __str__(self):
        return f"{self.repository.name} - {self.file_path}"


class Vulnerability(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    file = models.ForeignKey(FileAnalysis, on_delete=models.CASCADE, related_name="vulnerabilities")
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='MEDIUM')
    description = models.TextField()
    fix_suggestion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.severity}] {self.file.file_path}"


class ReviewComment(models.Model):
    ISSUE_TYPE_CHOICES = [
        ('BUG', 'Bug'),
        ('CODE_SMELL', 'Code Smell'),
        ('OPTIMIZATION', 'Optimization'),
    ]

    file = models.ForeignKey(FileAnalysis, on_delete=models.CASCADE, related_name="comments")
    line_number = models.PositiveIntegerField(blank=True, null=True)
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES, default='CODE_SMELL')
    recommendation = models.TextField()

    def __str__(self):
        return f"{self.issue_type} at {self.file.file_path}:{self.line_number}"
