export PYTHONPATH := $(PWD)

.PHONY: install test test-fast test-ui report docker-test

install:
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt

test:
	pytest -k "not ui" -v

test-ui:
	pytest -m ui -v

report:
	pytest --html=report.html --self-contained-html --cov=src --cov-report=html -q

docker-test:
	docker compose up --build --exit-code-from tests
