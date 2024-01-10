JSON_FILES 			= $(wildcard configurations/*.json)
JSON_FILE_NOTDIR 	= $(notdir $(wildcard configurations/*.json))
IMAGE				= message_on_live:twitch
DOCKER_COMPOSE_FILE	= docker/docker-compose.yml

############################################################################

all: stop build run

stop:
	@if [ -n "$$(docker ps --filter ancestor=$(IMAGE) | grep $(IMAGE))" ]; then \
		docker stop $$(docker ps --filter ancestor=$(IMAGE) -q); \
	fi
	@echo "\033[0;32m[✔️] All containers have been stopped\033[0m"

build:
	@mkdir -p logs/
	@docker pull python:alpine3.19
	@docker-compose -f $(DOCKER_COMPOSE_FILE) build
	@echo "\033[0;32m[✔️] docker-compose built successfully\033[0m"

check-characters:
	@if find configurations -name '*.json' -exec basename {} .json \; | cat | grep -q '[^[:alnum:]_-]'; then \
        echo "\033[0;31m[X] At least one invalid .json filename, use only [a-z, A-Z, 0-9, _, -]\033[0m"; \
		exit 1; \
	fi

mkdir-logs:
	@mkdir -p logs/

run: $(mkdir-logs) $(check-characters) $(JSON_FILES:.json=.up)

%.up: %.json
	echo "Launching docker-compose up for $(notdir $<)"
	$(shell export JSON_FILE=$(notdir $<) && docker-compose -p mol_$(notdir $<) -f $(DOCKER_COMPOSE_FILE) up -d)

.PHONY: all stop build run check-characters mkdir-logs

############################################################################
