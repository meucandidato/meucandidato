.PHONY: clean pep8 test install develop help

clean: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.egg-info' -exec rm -fr {} +

pep8: ## check style with flake8
	flake8 meucandidato tests

test: pep8 ## run tests quickly with the default Python
	py.test -v

install: clean test ## install the package to the active Python's site-packages

develop: ## Install the package with develop mode
	python setup.py develop

help:  ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'