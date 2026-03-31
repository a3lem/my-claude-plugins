"""Tests for `spectl new`.
# spec: spectl requirement=create-change
"""

import json
from conftest import run_spectl, make_change


# spec: spectl requirement=create-change scenario=basic-creation
def test_basic_creation(spec_root):
    rc, out, err = run_spectl("new", "add-oauth", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "Created" in out
    assert "(id:" in out

    change_path = spec_root / "changes" / "add-oauth"
    assert change_path.is_dir()
    assert (change_path / "deltas").is_dir()

    cj = json.loads((change_path / ".change.json").read_text())
    assert "id" in cj
    assert len(cj["id"]) == 5
    assert cj["id"].isalnum()
    assert "created" in cj
    assert "status" not in cj  # status is computed, not stored


# spec: spectl requirement=create-change scenario=slug-collision
def test_slug_collision(spec_root):
    make_change(spec_root, "add-oauth")
    rc, out, err = run_spectl("new", "add-oauth", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 1
    assert "already exists" in err


# spec: spectl requirement=create-change scenario=custom-spec-directory
def test_custom_spec_directory(spec_root):
    backend = spec_root.parent / "alt-specs"
    backend.mkdir()
    (backend / "changes").mkdir()
    rc, out, err = run_spectl("new", "add-oauth", "--dir", str(backend), cwd=spec_root.parent)
    assert rc == 0
    assert (backend / "changes" / "add-oauth" / ".change.json").is_file()
