pythonContainer = pythonCompose

# IF THIS NO LONGER WORK JUST MANUALLY PUT THE VERSION YOU WANT, (EX:PENULTIMATE_STABLE=3.17)
PENULTIMATE_STABLE=$(shell curl -s "https://www.alpinelinux.org/releases/" | grep "\-stable" | sed -n 2p  | sed -n 's/.*\/\([0-9.]\+\)-stable.*/\1/p')

############################################################################

all: stop build run

stop:
	@if [ -n "$$(sudo docker ps | grep $(pythonContainer))" ]; then \
		sudo docker stop $(pythonContainer); \
	fi
	@echo "\033[0;32m[✔️] Inception containers have been stopped\033[0m"

build:
	@sudo docker-compose -f ./srcs/docker-compose.yml build
	@echo "\033[0;32m[✔️] docker-compose built successfully\033[0m"

run:
	@sudo docker-compose -f ./srcs/docker-compose.yml up -d

exec:
	@sudo docker exec -it $(pythonContainer) sh

logs:
	@sudo docker logs -f $(pythonContainer)

############################################################################
