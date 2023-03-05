hello:
	echo "Hello World!"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py

lint:
	pylint --disable E1120 *.py

all: hello install
test_all: lint test