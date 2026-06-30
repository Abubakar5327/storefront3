
#!/bin/bash
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn storefront.wsgi --bind 0.0.0.0:${PORT:-8000}