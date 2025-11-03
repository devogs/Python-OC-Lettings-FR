FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /usr/src/app/staticfiles && python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]