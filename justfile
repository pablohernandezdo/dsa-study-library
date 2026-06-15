ruff:
    uv run ruff check src/ tests/

mypy:
    uv run mypy src/ tests/

test:
    uv run pytest

cov:
    uv run pytest --cov=dsa --cov-report=term-missing

cov-html:
    uv run pytest --cov=dsa --cov-report=html

pre-commit:
    uv run pre-commit run --all-files

publish:
    uv build
    uv publish --token $(python3 -c "import configparser, pathlib; c = configparser.ConfigParser(); c.read(pathlib.Path.home() / '.pypirc'); print(c['pypi']['password'])")
