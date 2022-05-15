.DEFAULT_GOAL := default_target

PROJECT_NAME := bidding_api
PYTHON_VERSION := 3.9.7
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools==62.2.0
	-apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
	-sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
	 pip install -r requirements-dev.txt

setup: .pip
	pip uninstall -y typing
	pip install -U setuptools==59.6.0
	-apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
	-sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
	 pip install -r requirements.txt


.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '_pycache_' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/
	rm -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

pycodestyle:
	echo "Running pycodestyle"
	pycodestyle

flake8:
	echo "Running flake8"
	flake8

code-convention: pycodestyle flake8

test:
	# "Running unit tests"
	pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=bidding_api --cov-fail-under=80

test-lf:
	# "Running unit tests"
	pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=bidding_api --cov-fail-under=0 --lf

# ARRUMAR
test-integration:
	# "Running integration tests"
	# pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=bidding_api --cov-fail-under=70

# Postgres Local
run-postgres:
	docker start bidding-api-postgres 2>/dev/null || docker run --name bidding-api-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:10-alpine

# Mongo Local
run-mongo:
	docker start bidding-api-mongo 2>/dev/null || docker run -d -p 27017:27017 --net=host --name bidding-api-mongo mongo:4.0.10

# Rabbit Local
run-rabbit:
	docker start bidding-api-rabbit 2>/dev/null || docker run -d --name bidding-api-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management

# Run Local Server
runserver: clean collectstatic run-postgres run-mongo
	python manage.py runserver

default_target: clean collectstatic code-convention test

docker_clear_containers:
	docker stop $(docker ps -aq); docker rm $(docker ps -aq)

containers-up: run-postgres run-mongo run-rabbit

containers-down:
	docker stop $$(docker ps -aq)

containers-reset: containers-down containers-up