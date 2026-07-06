# Cache Key Audit

Find tenant and user isolation risks in cache key designs. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

## Project card

<img src="assets/readme-cover.svg" alt="Cache Key Audit cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | delivery and infrastructure |
| Command | `cache-key-audit` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `missing-tenant` | high | tenant dimension is missing |
| `missing-user` | medium | user dimension may be missing |
| `shared-cache` | low | shared cache is enabled |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/cache-key-audit.git
cd cache-key-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cache-key-audit examples/sample.txt
cache-key-audit examples/sample.txt --json
```
