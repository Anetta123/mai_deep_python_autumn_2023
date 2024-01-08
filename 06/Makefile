PYTHON = python3

.PHONY: clean test venv install

clean:
	rm -rf __pycache__
test:
	$(PYTHON) -m unittest tests
venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
install:
	pip3 install -r requirements.txt