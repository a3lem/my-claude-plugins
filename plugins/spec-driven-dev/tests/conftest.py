"""Shared fixtures for spectl tests."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

SPECTL = Path(__file__).parent.parent / "scripts" / "spectl.py"


@pytest.fixture
def spec_root(tmp_path):
    """Create a minimal spec root with changes/ and reference/ dirs."""
    specs = tmp_path / "specs"
    specs.mkdir()
    (specs / "changes").mkdir()
    (specs / "reference").mkdir()
    return specs


def run_spectl(*args, cwd=None):
    """Run spectl as a subprocess and return (returncode, stdout, stderr).

    If --dir is in args, it's moved before the subcommand (argparse requires
    global flags before the subcommand name).
    """
    args = list(args)
    if "--dir" in args:
        idx = args.index("--dir")
        dir_flag = args.pop(idx)
        dir_val = args.pop(idx)
        args = [dir_flag, dir_val] + args
    result = subprocess.run(
        [sys.executable, str(SPECTL), *args],
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def make_change(spec_root, slug, *, id=None, created="2026-03-14",
                proposal=False, design=False, tasks=None, deltas=None,
                archived=None):
    """Create a change directory with specified artifacts."""
    changes_dir = spec_root / "changes"
    change_path = changes_dir / slug
    change_path.mkdir(parents=True, exist_ok=True)
    (change_path / "deltas").mkdir(exist_ok=True)

    cj = {"id": id or "test1", "created": created}
    if archived:
        cj["archived"] = archived
    (change_path / ".change.json").write_text(json.dumps(cj, indent=2) + "\n")

    if proposal:
        (change_path / "proposal.md").write_text("# Proposal\n## Why\nTest reason.\n")
    if design:
        (change_path / "design.md").write_text("# Design\n")
    if tasks is not None:
        (change_path / "tasks.md").write_text(tasks)
    if deltas:
        for cap, content in deltas.items():
            delta_dir = change_path / "deltas" / cap
            delta_dir.mkdir(parents=True, exist_ok=True)
            (delta_dir / "spec.md").write_text(content)

    return change_path


def make_archived_change(spec_root, slug, **kwargs):
    """Create a change in the archive/ directory."""
    archive_dir = spec_root / "changes" / "archive"
    archive_dir.mkdir(exist_ok=True)
    change_path = archive_dir / slug
    change_path.mkdir(parents=True, exist_ok=True)
    (change_path / "deltas").mkdir(exist_ok=True)

    cj = {"id": kwargs.get("id", "arc01"), "created": kwargs.get("created", "2026-03-14")}
    if "archived" in kwargs:
        cj["archived"] = kwargs["archived"]
    (change_path / ".change.json").write_text(json.dumps(cj, indent=2) + "\n")

    if kwargs.get("tasks"):
        (change_path / "tasks.md").write_text(kwargs["tasks"])

    return change_path
