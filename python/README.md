# python/ — `vislam_tools`

**Purpose:** Python tooling around the C++ engine: dataset ingestion and standardization, sanity checks, calibration helpers, visualization (Open3D) and trajectory evaluation (`evo`).

**Inputs:** raw iPhone exports, EuRoC-layout datasets, engine outputs.
**Outputs:** standardized datasets under `data/datasets/`, diagnostic plots, metric reports.

## Layout

```text
python/
├── vislam_tools/   # Reusable package (imported by scripts/)
└── tests/          # Pytest suite
```

## Setup & checks

```bash
# from the repository root
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"            # extras: viz (open3d, matplotlib), eval (evo)
ruff check python                  # lint
ruff format --check python         # formatting
pytest                             # tests
```

## Conventions

- PEP 8 enforced by `ruff`. Every function signature has type annotations.
- Use `pathlib.Path` for all filesystem access. Load structured config with `dataclasses` + `PyYAML`.
- Google-style docstrings.
