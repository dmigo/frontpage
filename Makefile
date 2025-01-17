install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	python -m pip install -r dev-requirements.txt
	python -m pip install isort black
	python -m spacy download en_core_web_sm

clean:
	python -m isort */*.py
	python -m black */*.py
	rm -rf **/__pycache__

docs:
	python -m spacy project document > README.md
