PYTHON = python3

.PHONY: lrucache descriptor clean test

lrucache:
	$(PYTHON) LRUcache.py
clean:
	rm -rf __pycache__
test:
	$(PYTHON) -m unittest tests
venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
