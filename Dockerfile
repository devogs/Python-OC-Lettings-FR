FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /usr/src/app/staticfiles

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]