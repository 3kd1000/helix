.PHONY: help install dev up down logs clean test

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install local client dependencies
	cd local-client && pip install -r requirements.txt

dev:  ## Start development environment
	docker compose -f docker-compose.dev.yml up -d

up: dev  ## Alias for dev

down:  ## Stop development environment
	docker compose -f docker-compose.dev.yml down

logs:  ## Show logs
	docker compose -f docker-compose.dev.yml logs -f

clean:  ## Clean up containers and volumes
	docker compose -f docker-compose.dev.yml down -v

test:  ## Run tests (향후 추가)
	@echo "Tests not yet implemented"

.DEFAULT_GOAL := help
