.PHONY: build run

build:
	docker build -t ecobici:latest .

run:
	docker run -it --rm -p 8000:8000 ecobici:latest

