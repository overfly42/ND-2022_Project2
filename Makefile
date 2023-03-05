hello:
	echo "Hello World!"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py

all: hello install
