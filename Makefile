SHELL := /bin/bash

.PHONY: init requirements

init:
	rm -rf .venv
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install -r requirements.txt && \
	pip install -r test/requirements.txt

requirements:
	source .venv/bin/activate && \
	pip install -r requirements.txt && \
	pip install -r test/requirements.txt
