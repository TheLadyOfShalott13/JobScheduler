from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Job, JobStatus
from .forms import JobForm
from .tasks import process_job, test_task, schedule_jobs

@login_required
def job_submit_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            schedule_jobs.apply_async()
            return redirect('status-job', job_id=job.id)
    else:
        form = JobForm()
    return render(request, 'submit-job.html', {'form': form})

@login_required
def job_status_view(request, job_id):
    job = Job.objects.get(id=job_id)
    if job.user != request.user:
        return redirect('job_submit_view')
    statuses = JobStatus.objects.filter(job=job).order_by('-timestamp')
    return render(request, 'status-job.html', {'job': job, 'statuses': statuses})

@login_required
def user_jobs_view(request):
    user_jobs = Job.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user-jobs.html', {'jobs': user_jobs})