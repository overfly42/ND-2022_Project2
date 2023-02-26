hello:
	echo "Hello World!"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

all: hello install
