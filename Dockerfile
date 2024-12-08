FROM python:3.12-slim

# Optional: Avoid writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a system group and user (won't switch to this user)
RUN addgroup --system app && adduser --system --ingroup app app

# Set the working directory
WORKDIR /app

# Install system dependencies (PostgreSQL client for example)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port for the Django app
EXPOSE 8000

# Set the environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=sabzshop.settings

# Command to run migrations and start Django development server
CMD ["python3", "manage.py",  "runserver", "0.0.0.0:8000"]