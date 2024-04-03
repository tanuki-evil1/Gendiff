install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

# TODO: Надо ли добавлять удаление пакета, как быструю команду
package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml