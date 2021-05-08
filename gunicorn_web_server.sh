# Define workers as many cores you have on the server machines
gunicorn --workers 2 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info