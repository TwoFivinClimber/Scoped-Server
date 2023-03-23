alias reseed="
  python3 manage.py loaddata user
  python3 manage.py loaddata company
  python3 manage.py loaddata skill
  python3 manage.py loaddata gear
  python3 manage.py loaddata job
  python3 manage.py loaddata crew
  python3 manage.py loaddata job_gear
  python3 manage.py loaddata message
  python3 manage.py loaddata image
  python3 manage.py loaddata employee
  python3 manage.py loaddata blog
  python3 manage.py loaddata invite
  "

alias runit="python manage.py runserver"
