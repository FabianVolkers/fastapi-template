run:
	uvicorn app.main:app --reload

setup-db:
	alembic upgrade head

test:
	pytest

lint:
	flake8 app tests

autopep8:
	autopep8 --in-place --aggressive --recursive app tests

isort:
	isort app tests

check-isort:
	isort app tests --check

format:
	isort autopep8

ci: check-isort lint test
