from pathlib import Path

import yaml

import vislam_tools

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_package_importable():
    assert vislam_tools.__version__ == "0.1.0"


def test_default_config_is_valid_yaml():
    config_path = REPO_ROOT / "configs" / "default_config.yaml"
    config = yaml.safe_load(config_path.read_text())
    assert isinstance(config, dict)
    for section in ("paths", "camera", "imu", "extrinsics", "frames", "reproducibility"):
        assert section in config
