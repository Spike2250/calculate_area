install:
	poetry install

calc-area:
	poetry run start-app

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 calc_area

check:
	poetry run flake8 calc_area
	poetry run flake8 tests

test:
	poetry run pytest
