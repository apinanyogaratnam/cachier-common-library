IMAGE := base-repository-template
VERSION := 0.1.0
REGISTRY_URL := ghcr.io/apinanyogaratnam/${IMAGE}
IMAGE_VERSION_NAME := ${REGISTRY_URL}:${VERSION}
IMAGE_LATEST_VERSION_NAME := ${REGISTRY_URL}:latest

build:
	docker build -t ${IMAGE} .

run:
	docker run -d -p 8000:8000 ${IMAGE}

exec:
	docker exec -it $(sha) /bin/sh

auth:
	grep -v '^#' .env.local | grep -e "CR_PAT" | sed -e 's/.*=//' | docker login ghcr.io -u USERNAME --password-stdin

tag:
	docker tag ${IMAGE} ${IMAGE_LATEST_VERSION_NAME}
	docker tag ${IMAGE} ${IMAGE_VERSION_NAME}
	git tag -m "v${VERSION}" v${VERSION}

tag-image:
	docker tag ${IMAGE} ${IMAGE_LATEST_VERSION_NAME}
	docker tag ${IMAGE} ${IMAGE_VERSION_NAME}

push:
	docker push ${IMAGE_LATEST_VERSION_NAME}
	docker push ${IMAGE_VERSION_NAME}
	git push --tags

push-image:
	docker push ${IMAGE_LATEST_VERSION_NAME}
	docker push ${IMAGE_VERSION_NAME}

all:
	make build && make auth && make tag && make push
