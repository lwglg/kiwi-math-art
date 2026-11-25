# Project automation. Run `make help`.
SHELL := /bin/bash
.DEFAULT_GOAL := help

LANG_CODE ?= en
DECIMATION ?= 1
QUIET ?=
QFLAG := $(if $(QUIET),--quiet,)
PDF_en := build/kiwi-en-GB.pdf
PDF_de := build/kiwi-de-DE.pdf
PDF_pt := build/kiwi-pt-BR.pdf
PDF_ru := build/kiwi-ru-RU.pdf
PDF_fa := build/kiwi-fa-IR.pdf
PDF = $(PDF_$(LANG_CODE))
VIEWER ?= $(shell command -v xdg-open || command -v open || echo echo)

.PHONY: help install-uv install image pdf pdf-all view test format lint typecheck qa clean

help: ## List the available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  %-12s %s\n", $$1, $$2}'
	@echo; echo "  Usage: make pdf LANG_CODE=en|de|pt|ru|fa   |   make view LANG_CODE=pt"

install-uv: ## Install uv if it is missing
	@command -v uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

install: install-uv ## Install Python (see .python-version) and all dependencies
	uv sync

image: ## Render the kiwi PNG with progress (DECIMATION=4 for a preview, QUIET=1 to silence)
	uv run kiwi --decimation $(DECIMATION) --output build/kiwi.png $(QFLAG)

pdf: ## Compile the PDF for LANG_CODE (en | de | pt | ru | fa)
	@test -f build/kiwi.png || $(MAKE) image
	uv run kiwi-docs --lang $(LANG_CODE) $(QFLAG)

pdf-all: ## Compile the PDFs in all five languages (one progress run)
	@test -f build/kiwi.png || $(MAKE) image
	uv run kiwi-docs --lang all $(QFLAG)

view: pdf ## Compile and open the PDF for LANG_CODE
	$(VIEWER) $(PDF)

test: ## Unit tests with coverage (fails under 80 %)
	uv run pytest

format: ## Space statements (tools/spacing.py), then format with Ruff
	uv run python -m tools.spacing src tools
	uv run ruff format .

lint: ## Ruff lint, Ruff format check and statement-spacing check
	uv run ruff check .
	uv run ruff format --check .
	uv run python -m tools.spacing --check src tools

typecheck: ## Static type analysis with Mypy
	uv run mypy

qa: lint typecheck test ## Every quality gate

clean: ## Remove generated files
	rm -rf build .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
