# Edward Hoffmann — personal site (Quarto)

Static website source built with [Quarto](https://quarto.org/). The Quarto project root is `website/` (`_quarto.yml`, pages, posts, styles).

**Live site:** [edwardchoffmann.github.io](https://edwardchoffmann.github.io/)

## Build and preview

From the repo root:

```bash
cd website
quarto preview
```

To render without serving:

```bash
quarto render
```

You only need Quarto installed for local site work.

## Python tooling and CI

This repo also ships a minimal Python package layout so GitHub Actions can run linting, formatting checks, type checking, and a tiny test suite. None of that is required to preview or publish the site.

[uv](https://docs.astral.sh/uv/) manages the dev environment:

```bash
uv sync --extra dev
uv run pre-commit install
```

Useful commands:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run ruff format .
uv run mypy tests
```

**CI** (on pushes and pull requests to `main`): Ruff lint, Ruff format check, Mypy on `tests/`, and Pytest on Python 3.10–3.13.

## Repository layout

```
├── .github/workflows/ci.yml   # GitHub Actions
├── website/                   # Quarto website (run quarto from here)
├── tests/                     # Lightweight checks (e.g. README present)
├── pyproject.toml             # uv, Ruff, Pytest, Mypy
├── .pre-commit-config.yaml
└── README.md
```