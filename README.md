# cache-key-audit

**Notebook Style.** Find tenant and user isolation risks in cache key designs.

## Context

Bad cache keys can leak data across users or tenants. This CLI checks cache-key notes and configs for missing isolation dimensions.

## Cell 1: Install

`cache-key-audit` accepts cache key design notes or config text in text, JSON, JSONL, or CSV form.

## Cell 2: Run

```bash
python -m pip install -e ".[dev]"
cache-key-audit examples/sample.txt
cache-key-audit examples/sample.txt --json --fail-on medium
```

## Cell 3: Interpret

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-tenant` | high | tenant dimension is missing |
| `missing-user` | medium | user dimension may be missing |
| `shared-cache` | low | shared cache is enabled |

## Tests

```bash
ruff check .
pytest
python -m cache_key_audit --help
```

License: MIT

### Example Input

```text
cache key /account/settings tenant missing user missing shared true
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the cache-key-audit policy surface explicit.
