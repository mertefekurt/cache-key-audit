<img src="assets/readme-cover.svg" alt="Cache Key Audit cover" width="100%" />

# Cache Key Audit

Find tenant and user isolation risks in cache key designs.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `cache-key-audit` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-tenant` | high | tenant dimension is missing |
| `missing-user` | medium | user dimension may be missing |
| `shared-cache` | low | shared cache is enabled |

## Command line

```bash
python -m pip install -e ".[dev]"
cache-key-audit examples/sample.txt
cache-key-audit examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
cache key /account/settings tenant missing user missing shared true
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
