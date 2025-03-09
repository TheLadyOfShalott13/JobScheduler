from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    HIGH    = 'High'
    MEDIUM  = 'Medium'
    LOW     = 'Low'

    PRIORITY_LEVEL_CHOICES = [
        (HIGH   , 'High'),
        (MEDIUM , 'Medium'),
        (LOW    , 'Low'),
    ]
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    duration    = models.IntegerField(default=3)
    desc        = models.TextField()
    status      = models.CharField(max_length=50, default='Pending')
    priority    = models.CharField(max_length=50, choices=PRIORITY_LEVEL_CHOICES, default=LOW)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    start_time  = models.DateTimeField(null=True, blank=True)
    end_time    = models.DateTimeField(null=True, blank=True)
    deadline    = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class JobStatus(models.Model):
    PENDING     = 'Pending'
    RUNNING     = 'Running'
    COMPLETED   = 'Completed'
    FAILED      = 'Failed'

    STATUS_CHOICES = [
        (PENDING    , 'Pending'),
        (RUNNING    , 'Running'),
        (COMPLETED  , 'Completed'),
        (FAILED     , 'Failed'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job.name} - {self.status}"
