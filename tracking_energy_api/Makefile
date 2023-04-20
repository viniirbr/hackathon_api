VENV = test
PYTHON = $(VENV)/Scripts/python

.PHONY: run
run: $(PYTHON)
	$(PYTHON) api/app.py

$(PYTHON): requirements.txt
	py -m venv $(VENV)
	$(PYTHON) -m pip install --requirement requirements.txt

.PHONY: clean
clean:
	rmdir $(VENV) /s /q
	rmdir api\__pycache__ /s /q