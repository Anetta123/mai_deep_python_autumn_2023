PYTHON = python3

.PHONY: run test clean

run:
	$(PYTHON) main.py
test:
	$(PYTHON) -m unittest game_test.Test
clean:
	rm -rf __pycache__
venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
