IMAGE := cachier-common-library
VERSION := 0.2.0
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
	twine upload dist/cachier_common_library-${VERSION}-py3-none-any.whl

workflow:
	git tag -m 'v${VERSION}' v${VERSION}
	git push --tags
