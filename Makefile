.PHONY: run
.ONESHELL:
run:
	@ docker-compose up --build --remove-orphans


.PHONY: run-detached
.ONESHELL:
run-detached:
	@ docker-compose up --build --remove-orphans -d


.PHONY: clean
.ONESHELL:
clean:
	@ docker-compose down --rmi all --volumes


.PHONY: build
.ONESHELL:
build:
	@ docker-compose build --no-cache


.PHONY: shell-django
.ONESHELL:
shell-django:
	@ docker-compose exec django /bin/bash
