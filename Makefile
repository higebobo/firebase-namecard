MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := test

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

FIREBASE_PROJECT_ID=xxx
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nxxx\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=xxx
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_COLLECTION=data

# .env
ifneq ("$(wildcard ./.env)","")
  include ./.env
endif

pip: ## Install package by pip
	@pip install -r requirements.txt

run: ## Insert dat
	@python -m app -m insert -r -v

test: test-verbose ## Run test

test-quiet: ## Run test quiet
	@py.test -s -m "not integration"

test-verbose: ## Run test verbose
	@py.test -s --verbose -m "not integration"

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
