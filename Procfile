web: gunicorn --pythonpath="$PWD/pillbox-engine" wsgi:application
worker: celery -A pillbox-engine worker --app=pillbox-engine._celery -B --loglevel=info --concurrency=1
