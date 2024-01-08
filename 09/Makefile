PYTHON=python3

.PHONY: all test venv setup clean

all: venv setup

setup:
	./env/bin/pip install .
	./env/bin/pip install -r requirements.txt

venv:
	$(PYTHON) -m venv env

test:
	$(PYTHON) tests.py

clean:
	rm -rf build cjson.egg-info env