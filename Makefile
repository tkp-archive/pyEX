tests: ## Make unit tests
	IEX_TOKEN=Tpk_ecc89ddf30a611e9958142010a80043c python -m pytest -v pyEX --cov=pyEX --junitxml=python_junit.xml --cov-report=xml --cov-branch

lint: ## run linter
	python -m flake8 pyEX 

fix:  ## run black fix
	python -m black pyEX/

annotate: ## MyPy type annotation check
	python -m mypy -s pyEX

annotate_l: ## MyPy type annotation check - count only
	python -m mypy -s pyEX | wc -l 

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf 
	find . -name "*.pyc" | xargs rm -rf 
	rm -rf .coverage cover htmlcov logs build dist *.egg-info
	make -C ./docs clean
	rm -rf ./docs/*.*.rst  # generated

docs:  ## make documentation
	make -C ./docs html
	open ./docs/_build/html/index.html

install:  ## install to site-packages
	python -m pip install .

dev:
	python -m pip install .[dev]

dist:  ## dist to pypi
	rm -rf dist build
	python setup.py sdist bdist_wheel
	python -m twine check dist/* && twine upload dist/*

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean test tests help annotate annotate_l docs dist
