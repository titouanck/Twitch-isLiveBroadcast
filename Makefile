user				= $(shell whoami)
pythonContainer		= pythonCompose
path_dockercompose	= docker/docker-compose.yml
__pycache__			= ./docker/app/__pycache__

############################################################################

all: stop build run

stop:
	@if [ -n "$$(docker ps | grep $(pythonContainer))" ]; then \
		docker stop $(pythonContainer); \
	fi
	@echo "\033[0;32m[✔️] Inception containers have been stopped\033[0m"

down:
	@if [ -n "$$(docker ps -a | grep $(pythonContainer))" ]; then \
		docker-compose -f docker/docker-compose.yml down; \
	fi

build:
	@docker-compose -f $(path_dockercompose) build
	@echo "\033[0;32m[✔️] docker-compose built successfully\033[0m"

run:
	@mkdir -p channels/
	@docker-compose -f $(path_dockercompose) --env-file env/credentials.env up -d

exec:
	@docker exec -it $(pythonContainer) sh

re: down build run

container_logs:
	@docker logs -f $(pythonContainer)

clean: stop
	rm -rf channels $(__pycache__)

.PHONY: all stop down build run exec container_logs clean re

############################################################################
