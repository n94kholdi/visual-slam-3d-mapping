# configs/ — YAML configuration

**Purpose:** the single source of truth for every runtime parameter: paths, camera intrinsics and distortion, IMU noise, camera-IMU extrinsics and time offset, sanity-check thresholds, algorithm thresholds, and random seeds.

| File | Description |
|---|---|
| `default_config.yaml` | Template with every section; unknown values are `null` |

## Rules

- **Nothing hardcoded in source.** If code needs a value, it lives here.
- **Never guess.** Values that are still `null` (intrinsics, IMU noise, `T_CB`) must be filled from calibration or device metadata. Code must raise an error if a required value is `null`.
- **SI units** (m, s, rad, m/s², rad/s). Every field's unit is written in a comment next to it.
- Per-device or per-sequence overrides go in separate files (e.g., `iphone13_cam0.yaml`). Don't edit the template for those.
