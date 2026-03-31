"""Tests for `spectl archived`.
# spec: spectl requirement=list-archived-changes
"""

from conftest import run_spectl, make_archived_change


# spec: spectl requirement=list-archived-changes scenario=default
def test_list_archived(spec_root):
    make_archived_change(
        spec_root, "2026-03-14-add-oauth",
        id="x7k2m", archived={"reason": "merged"},
    )
    make_archived_change(
        spec_root, "2026-03-10-old-feature",
        id="r3t8w", archived={"reason": "rejected"},
    )
    rc, out, err = run_spectl("archived", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "x7k2m" in out
    assert "merged" in out
    assert "r3t8w" in out
    assert "rejected" in out


# spec: spectl requirement=list-archived-changes scenario=no-archived-changes
def test_no_archived(spec_root):
    rc, out, err = run_spectl("archived", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "No archived changes" in out
