.PHONY: install run test lint format typecheck check docker-up docker-down

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"
	pre-commit install

run:
	uvicorn sheriaopen.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	ruff format .
typecheck:
	mypy src

check: lint typecheck test

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down
