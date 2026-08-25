#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def verify_source() -> None:
    for line in (ROOT / "SOURCE.sha256").read_text().splitlines():
        expected, name = line.split(maxsplit=1)
        assert digest(ROOT / name) == expected, name


def verify_run(name: str) -> tuple[str, str]:
    run = ROOT / "evidence" / name
    out = run / "out"
    assert (run / "runner.rc").read_text() == "0\n"
    assert (out / "status.txt").read_text() == "PASS squarefree Poisson recurrence\n"
    for line in (out / "OUTPUT.sha256").read_text().splitlines():
        expected, remote = line.split(maxsplit=1)
        local = out / Path(remote).name
        assert digest(local) == expected, local
    central = (out / "centralizer.stdout").read_text()
    identities = (out / "identities.stdout").read_text()
    assert "PASS_CENTRALIZER" in central
    for marker in (
        "DEGREE18_PACKAGE_IDENTITY_ZERO",
        "DEGREE18_SOLUTION_IDENTITY_ZERO",
        "DEGREE17_PACKAGE_IDENTITY_ZERO",
        "DEGREE16_PACKAGE_IDENTITY_ZERO",
        "DEGREE15_PACKAGE_IDENTITY_ZERO",
        "PREDICTED_FULL_DIMENSION 22",
        "PASS_IDENTITIES",
    ):
        assert marker in identities, marker
    bad = ("skipping text", "not defined", "error at token", "FAIL_")
    assert not any(token in identities for token in bad)
    return central, identities


verify_source()
r6d = verify_run("r6d_v4b")
box02 = verify_run("box02_v4b")
assert r6d == box02

assert "IndexError" in (ROOT / "evidence/r6d_v1_fail/centralizer.stderr").read_text()
assert "not defined" in (ROOT / "evidence/r6d_v2_false_pass/identities.stderr").read_text()
assert (ROOT / "evidence/r6d_v4_permission_negative/runner.rc").read_text() == "126\n"

print("SQUAREFREE_POISSON_RECURRENCE_FROZEN_REPLAY_PASS")
