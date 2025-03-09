from django.urls import path
from .api_views import JobSubmitView, JobStatusView, UserJobsView
from . import views

urlpatterns = [
    path('submit/', views.job_submit_view, name='submit-job'),
    path('status/<int:job_id>/', views.job_status_view, name='status-job'),
    path('list/', views.user_jobs_view, name='user-jobs'),
    path('api/submit-job/', JobSubmitView.as_view(), name='api-submit-job'),
    path('api/status-job/<int:id>/', JobStatusView.as_view(), name='api-status-job'),
    path('api/user-jobs/', UserJobsView.as_view(), name='api-user-jobs'),
]
