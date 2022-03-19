release: flask db upgrade --directory migrations
web: gunicorn -w 4 -b "0.0.0.0: 5432" app:app