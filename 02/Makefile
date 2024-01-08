PYTHON = python3

.PHONY: run clean test

run:
	$(PYTHON) main.py
clean:
	rm -rf __pycache__
test:
	$(PYTHON) -m unittest tests.Test
venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
