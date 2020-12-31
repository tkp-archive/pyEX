tests: ## Make unit tests
	IEX_TOKEN=Tpk_ecc89ddf30a611e9958142010a80043c python -m pytest -v pyEX --cov=pyEX --junitxml=python_junit.xml --cov-report=xml --cov-branch

lint: ## run linter
	python -m flake8 pyEX 

fix:  ## run black fix
	python -m black pyEX/

talib_nix:  ## install talib for *nix
	wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
	tar xfzv ta-lib-0.4.0-src.tar.gz
	cd ta-lib && ./configure --prefix=/usr LDFLAGS="-lm" && make && sudo make install

talib_darwin:  ## install talib for mac
	wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
	tar xfzv ta-lib-0.4.0-src.tar.gz
	cd ta-lib && ./configure && make &&	make install

talib_windows_py37:  ## install talib for windows
	python -m pip install https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/TA_Lib-0.4.19-cp37-cp37m-win_amd64.whl

talib_windows_py38:  ## install talib for windows
	python -m pip install https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/TA_Lib-0.4.19-cp38-cp38-win_amd64.whl

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
