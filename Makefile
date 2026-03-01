# Installation
site_install:
	pip install -r requirements.txt

dev_install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Testing
test:
	pytest tests/ -v

test_coverage:
	pytest tests/ --cov=sort --cov-report=term-missing --cov-report=html

# Documentation site
site_link:
	ln -sf $(CURDIR)/README.md $(CURDIR)/docs/index.md

site_preview: site_link
	mkdocs serve

site_build: site_link
	mkdocs build

site_deploy: site_link
	mkdocs gh-deploy --clean
