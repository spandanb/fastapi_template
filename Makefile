.PHONY: lint
lint:
	ruff check

.PHONY: rfix
rfix:
	ruff check --fix

.PHONY: run
run:
	fastapi dev app/main.py

.PHONY: tests
tests:
	python -m pytest --disable-warnings -s app/test_main.py
