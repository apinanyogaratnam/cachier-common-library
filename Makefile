IMAGE := cachier-common-library
VERSION := 0.0.1
REGISTRY_URL := ghcr.io/apinanyogaratnam/${IMAGE}
IMAGE_VERSION_NAME := ${REGISTRY_URL}:${VERSION}
IMAGE_LATEST_VERSION_NAME := ${REGISTRY_URL}:latest

.PHONY: venv, build

freeze:
	pip freeze > requirements.txt

freeze-dev:
	pip freeze > requirements_dev.txt

build:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/cachier_python-${VERSION}-py3-none-any.whl
