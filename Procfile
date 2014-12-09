web: gunicorn --pythonpath="$PWD/pillbox-engine" wsgi:application
worker: celery worker --app=pillbox-engine._celery -B --loglevel=DEBUG --concurrency=1
