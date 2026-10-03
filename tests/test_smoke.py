"""Packaged discovery must not expose a duplicate agent-routed selfie entry."""
from pathlib import Path

import pytest

from plugin.server.infrastructure.packaged_metadata import read_packaged_metadata


def test_packaged_metadata_matches_the_source_tree():
    root = Path(__file__).resolve().parents[1]
    if (root / "profiles.toml").exists() or (root / "profiles").exists():
        pytest.skip("Local runtime profiles are excluded; validate a clean source export instead")
    metadata = read_packaged_metadata(root)
    assert metadata is not None
    assert metadata.entries == []
    assert "send_selfie" not in metadata.entry_methods
