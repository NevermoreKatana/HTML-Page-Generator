install:
	poetry install
start:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate