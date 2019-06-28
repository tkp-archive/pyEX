tests: ## Clean and Make unit tests
	IEX_TOKEN=Tpk_ecc89ddf30a611e9958142010a80043c python3 -m pytest -v tests --cov=pyEX

test: lint ## run the tests for travis CI
	IEX_TOKEN=Tpk_ecc89ddf30a611e9958142010a80043c python3 -m pytest -v tests --cov=pyEX

lint: ## run linter
	flake8 pyEX 

annotate: ## MyPy type annotation check
	mypy -s pyEX

annotate_l: ## MyPy type annotation check - count only
	mypy -s pyEX | wc -l 

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
	pip3 install .

micro:  ## steps before dist, defaults to previous tag + one micro
	. scripts/deploy.sh MICRO

minor:  ## steps before dist, defaults to previous tag + one micro
	. scripts/deploy.sh MINOR

major:  ## steps before dist, defaults to previous tag + one micro
	. scripts/deploy.sh MAJOR

dist:  ## dist to pypi
	python3 setup.py sdist upload -r pypi

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean test tests help annotate annotate_l docs dist
