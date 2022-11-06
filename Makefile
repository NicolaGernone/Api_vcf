build:
	docker compose build

down:
	docker compose down

up: build makemigrations migrate
	docker compose up -d

first: build makemigrations migrate loaddatavcf
	docker compose up -d

migrate:
	docker compose run --rm api python manage.py migrate

makemigrations:
	docker compose run --rm api python manage.py makemigrations

showmig: 
	docker compose run --rm api python manage.py showmigrations

loaddata:
	docker compose run --rm api python manage.py loaddata data.json

loaddatavcf:
	docker compose run --rm api python manage.py loaddatavcf "NA12877_API_10.vcf.gz"

deps: deps_lock
	docker compose run --rm api poetry install

deps_lock:
	docker compose run --rm api poetry lock

user:
	docker compose run --rm api python manage.py createsuperuser

static:
	docker compose run --rm api python manage.py collectstatic --noinput --clear --no-post-process

bash:
	docker compose run --rm api /bin/sh

test:
	docker compose run --rm api python manage.py test

coverage: build makemigrations migrate
	docker compose run --rm api coverage run --source='api' --omit='api/tests/*' manage.py test
	docker compose run --rm api coverage report
	docker compose run --rm api coverage xml
