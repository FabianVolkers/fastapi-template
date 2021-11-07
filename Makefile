venv:
	[ ! -d "venv" ] && python3 -m venv venv

pip:
	pip install -r requirements.txt
	pip install -e .

setup-db:
	alembic upgrade head

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	flake8 app tests

autopep8:
	autopep8 --in-place --aggressive --aggressive --recursive app tests

isort:
	isort app tests

check-isort:
	isort app tests --check

format:
	isort autopep8

ci: check-isort lint test

bootstrap: venv pip setup-db