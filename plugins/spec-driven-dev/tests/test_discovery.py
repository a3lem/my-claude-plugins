"""Tests for spec directory discovery.
# spec: spectl requirement=spec-directory-discovery
"""

from conftest import run_spectl


# spec: spectl requirement=spec-directory-discovery scenario=specs-in-current-directory
def test_default_discovery(spec_root):
    rc, out, err = run_spectl("changes", cwd=spec_root.parent)
    assert rc == 0
    assert "No active changes" in out


# spec: spectl requirement=spec-directory-discovery scenario=no-specs-directory-found
def test_no_specs_directory(tmp_path):
    rc, out, err = run_spectl("changes", cwd=tmp_path)
    assert rc == 1
    assert "No specs/ directory found" in err


# spec: spectl requirement=spec-directory-discovery scenario=explicit-directory
def test_explicit_directory(spec_root):
    alt = spec_root.parent / "elsewhere"
    alt.mkdir()
    (alt / "changes").mkdir()
    rc, out, err = run_spectl("changes", "--dir", str(alt), cwd=spec_root.parent)
    assert rc == 0
    assert "No active changes" in out
