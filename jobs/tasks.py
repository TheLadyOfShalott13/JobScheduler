import time
import heapq
from celery import shared_task,states
from django.utils.timezone import now
from .models import Job, JobStatus

@shared_task(bind=True)
def process_job(self, job_id):
    job = Job.objects.get(id=job_id)
    job.status = JobStatus.RUNNING
    job.start_time = now()
    job.save()
    JobStatus.objects.create(job=job, status=JobStatus.RUNNING)

    try:
        time.sleep(3)
        job.status = JobStatus.COMPLETED
    except Exception as e:
        job.status = JobStatus.FAILED
        self.update_state(state=states.FAILURE, meta={'exc': str(e)})
    finally:
        job.end_time = now()
        job.save()
        JobStatus.objects.create(job=job, status=job.status)


def job_priority_key(job):
    priority_mapping = { 'High': 1, 'Medium': 2, 'Low': 3 }
    return priority_mapping[job.priority], job.deadline


@shared_task
def schedule_jobs():
    jobs = Job.objects.filter(status='Pending').order_by('deadline')
    job_heap = []

    for job in jobs:
        heapq.heappush(job_heap, (job_priority_key(job), job.id))

    while job_heap:
        _, job_id = heapq.heappop(job_heap)
        process_job.apply_async(args=[str(job_id)])


@shared_task
def test_task(job_id):
    print("Test task executed " + job_id)


# Schedule this task periodically using Celery beat or manually call it as needed
#schedule_jobs.apply_async()