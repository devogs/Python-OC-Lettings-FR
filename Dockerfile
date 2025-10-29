# Dockerfile

# --- Stage 1: Builder (Used to install dependencies and collect static files) ---
FROM python:3.12-slim as builder

# Set environment variables for the build
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_STATIC_ROOT /vol/web/static
ENV DJANGO_MEDIA_ROOT /vol/web/media

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Collect static files (CRUCIAL for production look and feel)
RUN python manage.py collectstatic --noinput

# --- Stage 2: Final Image (Lighter, production-ready image) ---
FROM python:3.12-slim

# Install necessary libraries (e.g., for serving static files)
# We don't need a full web server like nginx for this project; 
# Gunicorn will serve the files from the volume using WhiteNoise or similar (if configured).

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_STATIC_ROOT /vol/web/static
ENV DJANGO_MEDIA_ROOT /vol/web/media

# Create volumes/directories for static files and media
RUN mkdir -p $DJANGO_STATIC_ROOT
RUN mkdir -p $DJANGO_MEDIA_ROOT

WORKDIR /usr/src/app

# Copy collected static files from the builder stage
COPY --from=builder $DJANGO_STATIC_ROOT $DJANGO_STATIC_ROOT

# Copy only runtime dependencies and application code
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY . .

# Expose the port (Gunicorn default is 8000)
EXPOSE 8000

# Command to run the application using Gunicorn (production WSGI server)
# oc_lettings_site.wsgi refers to the WSGI file location
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]