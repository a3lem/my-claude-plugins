"""Tests for `spectl changes`.
# spec: spectl requirement=list-active-changes
"""

import json
from conftest import run_spectl, make_change


# spec: spectl requirement=list-active-changes scenario=default
def test_list_changes(spec_root):
    make_change(spec_root, "add-oauth", id="x7k2m")
    make_change(spec_root, "fix-sessions", id="p9r4n")
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "x7k2m" in out
    assert "add-oauth" in out
    assert "p9r4n" in out
    assert "fix-sessions" in out


def test_list_changes_json(spec_root):
    make_change(spec_root, "add-oauth", id="x7k2m")
    rc, out, err = run_spectl("changes", "--json", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    data = json.loads(out)
    assert len(data) == 1
    assert data[0]["changes"][0]["slug"] == "add-oauth"
    assert data[0]["changes"][0]["id"] == "x7k2m"


# spec: spectl requirement=list-active-changes scenario=recursive-discovery
def test_recursive_discovery(spec_root):
    # Create changes in two different spec roots under the same parent
    root1 = spec_root
    make_change(root1, "change-a", id="aaa01")
    root2 = spec_root.parent / "sub" / "specs"
    root2.mkdir(parents=True)
    (root2 / "changes").mkdir()
    make_change(root2, "change-b", id="bbb01")
    rc, out, err = run_spectl("changes", "-r", cwd=spec_root.parent)
    assert rc == 0
    assert "change-a" in out
    assert "change-b" in out


# spec: spectl requirement=list-active-changes scenario=no-changes
def test_no_changes(spec_root):
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "No active changes" in out


def test_excludes_archive(spec_root):
    make_change(spec_root, "active-one", id="act01")
    archive = spec_root / "changes" / "archive" / "2026-03-14-old"
    archive.mkdir(parents=True)
    (archive / ".change.json").write_text('{"id": "old01", "created": "2026-03-14"}')
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "old01" not in out
    assert "act01" in out


# spec: spectl requirement=list-active-changes scenario=default
def test_computed_status_in_list(spec_root):
    make_change(spec_root, "drafty", id="dft01")
    make_change(
        spec_root, "in-prog", id="prg01",
        proposal=True, design=True,
        tasks="# Tasks\n- [x] done\n- [ ] todo\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "drafting" in out
    assert "in progress" in out
