# scripts/ — CLI entry points & wrappers

**Purpose:** thin command-line entry points that connect `vislam_tools` (Python) and the C++ engine, plus Docker wrappers for external tools (e.g., Kalibr).

**Inputs / outputs:** set through CLI arguments and a `--config` YAML from `configs/`. Scripts contain no hardcoded paths or parameters.

## Planned scripts

| Script | Phase | Purpose |
|---|---|---|
| `ingest_sequence.py` | 1 | Raw iPhone export → EuRoC-layout dataset |
| `inspect_dataset.py` | 1 | Timestamp, rate, overlap and IMU-unit sanity checks and plots |
| `run_kalibr.sh` | 2 | Dockerized Kalibr camera / camera-IMU calibration |

Business logic lives in `python/vislam_tools/`. Scripts only parse arguments and call into the package.
