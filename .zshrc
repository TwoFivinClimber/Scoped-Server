alias reseed="
  python3 manage.py loaddata skill
  python3 manage.py loaddata gear
  python3 manage.py loaddata user
  python3 manage.py loaddata job
  python3 manage.py loaddata crew
  python3 manage.py loaddata job_gear
  python3 manage.py loaddata message
  python3 manage.py loaddata user_skill
  python3 manage.py loaddata image
  "

alias runit="python manage.py runserver"
