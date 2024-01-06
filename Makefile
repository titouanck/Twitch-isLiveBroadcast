pythonContainer    = pythonCompose
path_dockercompose = docker/docker-compose.yml

############################################################################

all: stop build run

stop:
	@if [ -n "$$(sudo docker ps | grep $(pythonContainer))" ]; then \
		sudo docker stop $(pythonContainer); \
	fi
	@echo "\033[0;32m[✔️] Inception containers have been stopped\033[0m"

build:
	@sudo docker-compose -f $(path_dockercompose) build
	@echo "\033[0;32m[✔️] docker-compose built successfully\033[0m"

run:
	@sudo docker-compose -f $(path_dockercompose) up -d

exec:
	@sudo docker exec -it $(pythonContainer) sh

logs:
	@sudo docker logs -f $(pythonContainer)

############################################################################
