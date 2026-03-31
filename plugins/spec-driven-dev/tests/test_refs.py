"""Tests for `spectl refs`.
# spec: spectl requirement=list-reference-specs
"""

from conftest import run_spectl


# spec: spectl requirement=list-reference-specs scenario=list-references
def test_list_refs(spec_root):
    for name in ("billing", "user-auth"):
        cap_dir = spec_root / "reference" / name
        cap_dir.mkdir(parents=True)
        (cap_dir / "spec.md").write_text(f"# {name}\n## Overview\nHandles {name} logic.\n")

    rc, out, err = run_spectl("refs", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "user-auth" in out
    assert "billing" in out
    assert "Handles user-auth logic" in out


# spec: spectl requirement=list-reference-specs scenario=no-references
def test_no_refs(spec_root):
    rc, out, err = run_spectl("refs", "--dir", str(spec_root), cwd=spec_root.parent)
    assert rc == 0
    assert "No reference specs" in out
