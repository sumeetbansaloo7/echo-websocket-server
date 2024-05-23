DOCKER_USERNAME := sumeetbansal007
IMAGE_NAME := echo-websocket-server
TAG := $(shell git rev-parse --short HEAD)

.PHONY: build
build:
	docker build -t $(DOCKER_USERNAME)/$(IMAGE_NAME):$(TAG) .

.PHONY: push
push:
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):$(TAG)

.PHONY: deploy
deploy:
	kubectl apply -f k8sdeploy.yaml

.PHONY: all
all: build push deploy
