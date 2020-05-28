build:
	@docker build -t tuipik/develops_today:latest .
pull:
	@docker pull tuipik/develops_today:latest
run:
	@docker-compose up
db:
	@docker-compose run app sh -c "python manage.py fill_up_db"
test:
	@docker-compose run app sh -c "python manage.py test -v 2 && flake8"