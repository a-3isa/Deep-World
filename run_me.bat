start cmd /k python ip_puller.py
start cmd /k python manage.py runserver 0.0.0.0:599
start cmd /k plink -ssh debian@144.217.15.17 -pw dream  "cd deepdream; python3.7 manage.py runserver 144.217.15.17:8000"