# CONFIGURATION

# Where to put HTML reports that you wan to expose using a web interface
REPORTS_DIR = notebooks
SOURCE_DIR = mask_detection

# Documentation
DOCUMENTATION_OUTPUT = $(REPORTS_DIR)/documentation
APIDOC_OPTIONS = -d 1 --no-toc --separate --force --private

COVERAGE_OUTPUT = $(REPORTS_DIR)/coverage
COVERAGE_OPTIONS = --cov-config coverage/.coveragerc --cov-report term --cov-report html

# .PHONY is used to distinguish between a task and an existing folder
.PHONY: doc pipeline tests coverage data_tests
.DEFAULT_GOAL := help


# PRODUCTION COMMANDS
pipeline: install   ## run main project pipeline
	python $(SOURCE_DIR)/application/main.py

# DEVELOPMENT COMMANDS
doc: install-dev   ## build documentation from docstring
	rm -rf doc/source/generated
	sphinx-apidoc $(APIDOC_OPTIONS) -o doc/source/generated/ $(SOURCE_DIR) $(SOURCE_DIR)/tests
	cd doc; make html
	mkdir -p $(DOCUMENTATION_OUTPUT)
	cp -r doc/build/html/* $(DOCUMENTATION_OUTPUT)

tests: install-dev   ## run unit tests
	pytest -s tests/unit_tests/

data_tests: install-dev
	pytest data_tests/

coverage: install-dev   ## run code coverage (% of code tested)
	py.test $(COVERAGE_OPTIONS) --cov=$(SOURCE_DIR) tests/unit_tests/ | tee coverage/coverage.txt
	mv -f .coverage coverage/.coverage  # don't know how else to move it
	mkdir -p $(COVERAGE_OUTPUT)
	cp -r coverage/htmlcov/* $(COVERAGE_OUTPUT)

lint: install-dev   ## Check that your code follows the PEP8 standards
	flake8 $(SOURCE_DIR)

# PROJECT SETUP COMMANDS
install: requirements.txt  ## install project dependencies (requirements.txt)
	pip install -r requirements.txt
	touch install

install-dev: install requirements.dev.txt  ## install developpment dependencies (for testing, linting etc.)
	pip install -r requirements.dev.txt
	touch install-dev

init: ## initiate virtual environment
	bash init.sh
	touch init

# OTHER
help:           ## Show this help.
	# @fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'