PYTHON = python3

.PHONY: meta descriptor clean test

meta:
	$(PYTHON) meta_class.py
desctiptor:
	$(PYTHON) descriptor.py
clean:
	rm -rf __pycache__
test:
	$(PYTHON) -m unittest tests
venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt