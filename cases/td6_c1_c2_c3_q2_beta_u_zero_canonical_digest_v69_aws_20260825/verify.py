#!/usr/bin/env python3
"""Lightweight custody and scope verifier for the V69 U=0 digest repair."""

from hashlib import sha256
from pathlib import Path
import tarfile


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


archive = HERE / "source" / "td6-aws-handoff-20260825-v69.tar.gz"
assert digest(archive) == "9e89808cca9d24ec5182466b40e53d612317a4f03c70053a9c490e957ab51f38"
assert digest(HERE / "source" / "V69_SOURCE.sha256") == (
    "fe39baefa6bcec511646397b5060ee8a4d555d17c2310b40b0035ff5931900ac"
)

with tarfile.open(archive, "r:gz") as handle:
    member = handle.extractfile(
        "td6-aws-handoff-20260825-v69/jc2/cases/"
        "td6_c1_c2_c3_q2_n13_raw_canonical_v69_20260825/replay.py"
    )
    assert member is not None
    producer = member.read().decode()
assert "def canonical_mpoly(value):" in producer
assert "for monomial, coefficient in sorted(value.to_dict().items())" in producer
assert 'assert " object at 0x" not in serialized' in producer

box02 = HERE / "evidence" / "box02" / "v69.stdout"
box03 = HERE / "evidence" / "box03" / "v69.stdout"
assert (HERE / "evidence" / "box02" / "rc").read_text().strip() == "0"
assert (HERE / "evidence" / "box03" / "rc").read_text().strip() == "0"
assert box02.read_bytes() == box03.read_bytes()
assert digest(box02) == "9726fb09a9279c7c19c507eeafc5b541bfd2d89e9d34a7e972b73badde042734"

text = box02.read_text()
required = (
    "canonical_digest_serializer=sorted-Rat3-coordinate-v1",
    "canonical_digest_python_object_addresses=false",
    "source_center=U=0 over Q(C,V)",
    "transport_rank=3470/3602",
    "first_rank=36/132",
    "first_incompatibility[0]_key=('X-2', 14)",
    "first_incompatibility[0]_degree=0",
    "first_incompatibility[0]_source_row_count=14",
    "first_compatibility_gcd_degree=0",
    "first_compatibility_certificate_denominator=(1)",
    "first_compatibility_original_row_replay=true",
    "first_generic_raw_stratum_empty=true",
    "first_beta_root_stratum_required=false",
    "full_A3_beta_family_killed=false",
    "whole_TD6_killed=false",
    "SP2_killed=false",
    "JC2_resolved=false",
    "TD6-A3-Q2-N13-RAW-FIRST PASS",
)
for marker in required:
    assert marker in text, marker

# V69 changes reporter serialization only: after removing digest/sentinel lines,
# every mathematical marker agrees with each fresh noncanonical predecessor.
def nondigest_lines(value):
    return tuple(
        line for line in value.splitlines()
        if "sha256=" not in line
        and not line.endswith("_digest=" + line.rsplit("=", 1)[-1])
        and "_pivot_digest=" not in line
        and not line.startswith("canonical_digest_")
    )


for host in ("box02", "box03"):
    predecessor = (
        HERE / "evidence" / "noncanonical-predecessor" / f"{host}.stdout"
    ).read_text()
    assert nondigest_lines(text) == nondigest_lines(predecessor)

# Omitting the direct q-prime term changes the exact source support (14 -> 1)
# while leaving the same degree-zero unit obstruction.  It is a source-path
# control, not a claim that q-prime is load-bearing for this earlier first-band
# contradiction.
omission_dir = HERE / "evidence" / "omit-qprime-box02"
assert (omission_dir / "rc").read_text().strip() == "0"
omission = (omission_dir / "v69.stdout").read_text()
assert digest(omission_dir / "v69.stdout") == (
    "cc85d4cce23b7c377043ab9bb6ab1442cddaed285c564b919b9b21e6bfc67d64"
)
assert "direct_qprime_retained=false" in omission
assert "first_incompatibility[0]_source_row_count=1" in omission
assert "first_incompatibility[0]_residual_sha256=b302c4764091027f86d1129a66df5fbc5a39ee92c6e6e76dd880234bb5bb378a" in omission

# The first two launch tags passed an empty positional argument.  They are
# preserved as operator-failure controls and contribute no mathematical output.
for host in ("box02", "box03"):
    failure = HERE / "evidence" / f"operator-failure-{host}"
    assert (failure / "rc").read_text().strip() == "1"
    assert not (failure / "v69.stdout").read_bytes()
    assert "AssertionError" in (failure / "v69.stderr").read_text()

print("TD6-A3-Q2-U0-CANONICAL-DIGEST-V69 VERIFY PASS")
