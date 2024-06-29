# Use the official Python image from the Docker Hub
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE blog_application_system.settings

# Set the working directory
WORKDIR /../blog_application_system

# Install dependencies
COPY requirements.txt /../blog_application_system/
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files
COPY . /../blog_application_system/

# Expose the port on which the app will run
EXPOSE 8000

# Run migrations and collect static files
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Run the Gunicorn server
CMD ["gunicorn", "--config", "gunicorn_config.py", "blog_application_system.wsgi:application"]
