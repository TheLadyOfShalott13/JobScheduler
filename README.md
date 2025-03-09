# JobScheduler

JobScheduler is a Django application designed to manage and schedule jobs using Django Rest Framework (DRF) and Celery. This project enables users to submit jobs, track their status, and view all their jobs in a user-friendly manner.

## Features

- User authentication and authorization using Django Allauth.
- RESTful API endpoints for job submission, status tracking, and listing jobs.
- Asynchronous job scheduling and processing using Celery.
- Customizable job priority and status tracking.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Django 5.1.7
- MySQL
- Redis (for Celery)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/TheLadyOfShalott13/JobScheduler.git
    cd JobScheduler
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required using the following command:

    ```sh
    pip install django channels channels-redis redis asgiref django-redis mysqlclient celery redis django-allauth djangorestframework
    ```

4. Configure the database in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'jobscheduler',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }
    ```

5. Run database migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```sh
    python manage.py runserver
    ```

8. Start Celery worker (inspect logs for any errors):

    ```sh
    celery -A job_scheduler worker --loglevel=info --logfile=celery.log 
    ```

## API Endpoints

The following API endpoints are available:

- `POST /api/submit-job/`: Submit a new job.
- `GET /api/status-job/<int:id>/`: Fetch the status of a specific job.
- `GET /api/user-jobs/`: List all jobs for the authenticated user.

## Logging
All error logs for the Django application is stored in django.log and for celery in celery.log

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or reach out to the maintainer.
