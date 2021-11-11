install-poetry:
	@echo "\nLooking for poetry\n"
	@./install-poetry.sh

install-dependencies:
	@echo "\nInstalling dependencies...\n"
	@poetry install

setup-db:
	@echo "\nSetting up development database\n"
	@poetry run setup-db

bootstrap: install-poetry install-dependencies setup-db
