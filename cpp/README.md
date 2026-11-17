# cpp/ — Core SLAM engine (C++17)

**Purpose:** the visual-inertial SLAM engine: frontend (features, tracking, keyframes, IMU preintegration) and backend (bundle adjustment, pose graph, loop closure).

**Inputs:** EuRoC-layout datasets (`cam0/`, `imu0/`) and YAML configs from `configs/`.
**Outputs:** trajectories (TUM / EuRoC `.csv`) and sparse maps (`.ply`) written under `data/outputs/`.

## Layout

```text
cpp/
├── include/vislam/   # Public headers (#include "vislam/...")
├── src/              # Implementation (.cpp)
└── tests/            # GoogleTest unit & integration tests
```

## Build & test

```bash
# from the repository root
cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build -j
ctest --test-dir build --output-on-failure
```

| CMake option | Default | Meaning |
|---|---|---|
| `VISLAM_BUILD_TESTS` | `ON` | Build GoogleTest tests (skipped with a notice if GTest is missing) |
| `VISLAM_WARNINGS_AS_ERRORS` | `OFF` | Add `-Werror` |

## Conventions

- Naming: `PascalCase` types, `snake_case` functions and variables, `m_` prefix for private/protected members, `kPascalCase` constants.
- RAII only. No raw `new` / `delete`.
- Pass Eigen objects as `const Eigen::Ref<...>&` or `const T&`. STL containers holding fixed-size Eigen types use `Eigen::aligned_allocator`.
- `#pragma once`. Include order: own header → stdlib → third-party → `vislam/...`.
- Doxygen comments on every public API, including the **frame and units** of each input and output.
