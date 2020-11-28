default: help;

dependencies: ## install dependencies from the lockfile
	poetry install --no-root

run:	## run python script which resolve one day problem. the name should be day-{N}.py. For example to run problem day 23rd: "make run day=23"
	poetry run ipython advent_of_code_2020/day-${day}.py

help:	## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY:
	dependencies run help

.SILENT:
	dependencies run help