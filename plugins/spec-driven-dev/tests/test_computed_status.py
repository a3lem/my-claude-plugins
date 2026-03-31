"""Tests for computed status.
# spec: spectl requirement=computed-status
"""

from conftest import run_spectl, make_change


# spec: spectl requirement=computed-status scenario=drafting
def test_status_drafting(spec_root):
    make_change(spec_root, "incomplete", id="inc01")
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "drafting" in out


# spec: spectl requirement=computed-status scenario=drafting
def test_status_drafting_missing_design(spec_root):
    make_change(
        spec_root, "no-design", id="nod01",
        proposal=True,
        tasks="# Tasks\n- [ ] todo\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "drafting" in out


# spec: spectl requirement=computed-status scenario=ready
def test_status_ready(spec_root):
    make_change(
        spec_root, "all-open", id="rdy01",
        proposal=True, design=True,
        tasks="# Tasks\n- [ ] task 1\n- [ ] task 2\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "ready" in out


# spec: spectl requirement=computed-status scenario=in-progress
def test_status_in_progress(spec_root):
    make_change(
        spec_root, "mixed", id="prg01",
        proposal=True, design=True,
        tasks="# Tasks\n- [x] done\n- [ ] todo\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "in progress" in out


# spec: spectl requirement=computed-status scenario=complete
def test_status_complete(spec_root):
    make_change(
        spec_root, "all-done", id="cmp01",
        proposal=True, design=True,
        tasks="# Tasks\n- [x] done 1\n- [x] done 2\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "complete" in out


# spec: spectl requirement=computed-status scenario=backward-transition
def test_status_backward_transition(spec_root):
    cp = make_change(
        spec_root, "was-complete", id="bck01",
        proposal=True, design=True,
        tasks="# Tasks\n- [x] done 1\n- [x] done 2\n",
        deltas={"auth": "# auth\n## ADDED Requirements\n### Requirement: foo\n"},
    )
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "complete" in out

    # Add a new unchecked task
    (cp / "tasks.md").write_text("# Tasks\n- [x] done 1\n- [x] done 2\n- [ ] new task\n")
    rc, out, err = run_spectl("changes", "--dir", str(spec_root), cwd=spec_root.parent)
    assert "in progress" in out
