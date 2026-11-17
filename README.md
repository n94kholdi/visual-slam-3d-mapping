# visual-slam-3d-mapping

Offline Visual-Inertial SLAM for 3D mapping with a smartphone. It takes monocular RGB video and raw IMU data (accelerometer + gyroscope) from an iPhone 13 (no LiDAR, no RGB-D) and recovers metric-scale 6-DoF camera trajectories and a sparse 3D point cloud.

> **Status:** project scaffolding only. No SLAM or ingestion logic yet.

## Pipeline

```text
[iPhone 13: RGB + Raw IMU]
  → Stage 1  Ingestion & Standardization   → EuRoC-layout dataset + YAML
  → Stage 2  Calibration & Synchronization → intrinsics / extrinsics YAML, aligned streams
  → Stage 3  VIO frontend                  → keyframes, feature tracks, IMU preintegration
  → Stage 4  Mapping & optimization        → loop closure, bundle adjustment, pose graph
  → Stage 5  Post-processing & evaluation  → .ply cloud, trajectory (TUM / EuRoC), metrics
```

Stages talk to each other only through files on disk with fixed formats.

## Repository layout

| Path | Purpose |
|---|---|
| [`cpp/`](cpp/README.md) | Core C++17 SLAM engine (CMake, GoogleTest) |
| [`python/`](python/README.md) | `vislam_tools`: ingestion, calibration helpers, visualization, evaluation |
| [`configs/`](configs/README.md) | YAML configs (camera, IMU, extrinsics, thresholds) |
| [`scripts/`](scripts/README.md) | CLI entry points and Docker wrappers (e.g., Kalibr) |
| [`docs/`](docs/README.md) | Architecture notes and [ADRs](docs/decisions/README.md) |
| `data/` | Local datasets and outputs (git-ignored) |

## Quick start

### C++ (requires CMake ≥ 3.22 and a C++17 compiler)

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build -j
ctest --test-dir build --output-on-failure
```

### Python (requires Python ≥ 3.10)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"          # add ,viz,eval for Open3D / matplotlib / evo
ruff check python && ruff format --check python
pytest
```

## Conventions

- **Units:** SI everywhere inside the engine (m, s, rad, m/s², rad/s). Timestamps are int64 ns. Unit conversion happens only during ingestion.
- **Frames:** camera `C` uses the optical convention (+Z forward, +X right, +Y down). IMU body frame is `B`, related to `C` by `T_CB`. World frame `W` is gravity-aligned with +Z up (ENU).
- **Config-driven:** no hardcoded paths, intrinsics, noise parameters or thresholds. Everything comes from `configs/*.yaml`.
- **Validation gate:** every SLAM module must pass EuRoC MAV `MH_01_easy` before it runs on iPhone data.
