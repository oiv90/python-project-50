install:
	uv sync

check:
	uv sync --dry-run

build:
	uv build

package-install:
	uv tool install dist/*.whl --reinstall

publish:
	uv publish --dry-run

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests
