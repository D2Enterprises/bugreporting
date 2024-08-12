from django.db import models

class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reported_by = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ], default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title