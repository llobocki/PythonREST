.PHONY: help prepare-dev test lint run doc

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "prepare development environment, use only once"
	@echo "make test"
	@echo "run tests"
	@echo "make lint"
	@echo "       run pylint and mypy"
	@echo "make run"
	@echo "       run project"
	@echo "make doc"
	@echo "       build sphinx documentation"

# prepare-dev:
#     sudo apt-get -y install python3.5 python3-pip
#     python3 -m pip install virtualenv
#     make venv
#
# # Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
# venv: $(VENV_NAME)/bin/activate
# $(VENV_NAME)/bin/activate: setup.py
#     test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
#     ${PYTHON} -m pip install -U pip
#     ${PYTHON} -m pip install -e .
#     touch $(VENV_NAME)/bin/activate
#
#


test: venv
	pytest test/test*.py --junitxml=nosetests.xml --cov=app  --cov-branch
	coverage xml

sonar:
	sonnar-scanner
#
# lint: venv
#     ${PYTHON} -m pylint
#     ${PYTHON} -m mypy
#
run:
	python run.py
#
# doc: venv
#     $(VENV_ACTIVATE) && cd docs; make html

.PHONY: clean clean-env clean-all clean-build clean-test clean-dist

clean: clean-dist clean-test clean-build

clean-env: clean
	-@rm -rf $(ENV)
	-@rm -rf $(REQUIREMENTS_LOG)
	-@rm -rf .tox

clean-all: clean clean-env

clean-build:
	@find $(PKGDIR) -name '*.pyc' -delete
	@find $(PKGDIR) -name '__pycache__' -delete
	@find $(TESTDIR) -name '*.pyc' -delete 2>/dev/null || true
	@find $(TESTDIR) -name '__pycache__' -delete 2>/dev/null || true
	-@rm -rf $(EGG_INFO)
	-@rm -rf __pycache__

clean-test:
	-@rm -rf .cache
	-@rm -rf .coverage

clean-dist:
	-@rm -rf dist build
