"""Host-visible discovery must retain the selfie entry after packaging."""
from pathlib import Path

import pytest

from plugin.server.infrastructure.packaged_metadata import read_packaged_metadata


def test_packaged_metadata_matches_the_source_tree():
    root = Path(__file__).resolve().parents[1]
    if (root / "profiles.toml").exists() or (root / "profiles").exists():
        pytest.skip("Local runtime profiles are excluded; validate a clean source export instead")
    metadata = read_packaged_metadata(root)
    assert metadata is not None
    assert any(entry["id"] == "send_selfie" for entry in metadata.entries)
