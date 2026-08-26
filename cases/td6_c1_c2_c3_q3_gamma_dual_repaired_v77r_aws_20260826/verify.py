#!/usr/bin/env python3
"""Lightweight frozen-custody verifier; no producer/CAS execution."""

from hashlib import sha256
from pathlib import Path
import tarfile


HERE = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def digest_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


corrected = HERE / "archives" / "td6-v79b-corrected-q3-allq-source-20260825.tar.gz"
control = HERE / "archives" / "td6-v79a-control-source-20260825.tar.gz"
assert digest(corrected) == "5973b82953c919df1a28b1b86eed40feafbe4a3ea69bde14e7df68374e83942d"
assert digest(control) == "cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579"

member = "./jc2/cases/td6_c1_c2_c3_q3_gamma_dual_repaired_20260825/replay.py"
with tarfile.open(corrected, "r:gz") as archive:
    source = archive.extractfile(member).read()
    source_manifest = archive.extractfile("./SOURCE.sha256").read()
assert digest_bytes(source) == "7a961c02002dabb5f8ae363e88a4a041b855ec03fc8ea370bea576ae12e47d80"
assert digest_bytes(source_manifest) == "b1f1d48466b12748112dc054ee435051f1afdb67b816eaf1bc7c7ffe27742c2b"

expected = {
    "box02": (
        "9f3be97b1f2ad2c04f896e031e9a5318b4e6dc2fe4ccdbb55c56dcf697dc49e3",
        "0c9d05fa7891e877709a4bc0f4feac975ea54e082a77fa96844b6b661c377e97",
        "ip-172-30-0-186",
    ),
    "r6d": (
        "1d05d1be98e988a47032ae653dd71002cc42589e0c83a2189ff7ff76d5616ab9",
        "b62380449015ffaed44ab0f998556f97f13fb55d12044e447d5eb68c05312198",
        "ip-172-30-0-45",
    ),
}

required = (
    "producer=TD6-V77R-PURE-Q3-SCALAR-AUDIT",
    "q_gamma=t+gamma*t^3+t^25",
    "base_q2_beta=0",
    "scope_open=D(U*(C-3U^2)*B3)",
    "transport_rank=3470/3602",
    "transport_q3_source_omission_negative_control=true",
    "legacy_qd_B_state_is_semantically_inert=true",
    "q2_Q_PRIME_leakage_negative_control=true",
    "pure_q3_B_value_zero=true",
    "pure_q3_B_derivative_zero=true",
    "first_rank=38/132",
    "first_minor_gamma_sha256=c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1",
    "first_minor_gamma_is_exact_zero=true",
    "zero_scalar_digest_semantics_asserted=true",
    "raw_gamma_terms=4",
    "raw_gamma_sha256=70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c",
    "P12_source_row_omission_negative_control=true",
    "remainder_gamma_terms=3",
    "remainder_gamma_sha256=3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458",
    "dual_remainder_base_is_minus_k_over_50=true",
    "dual_remainder_is_unit_exactly=true",
    "lambda_zero_source_row_support=28",
    "lambda_prime_source_row_support=14",
    "derivative_source_identity_exact=true",
    "lambda_prime_omission_negative_control=true",
    "termwise_dual_slot_count=77512",
    "dual_denominator_radical_subset_U_H_B3=true",
    "source_base_multiplier_terms=1489",
    "source_gamma_support_terms=1149",
    "result_use=source_support_degree_denominator_discriminator_only",
    "finite_gamma_neighborhood_killed=false",
    "full_gamma_family_killed=false",
    "whole_TD6_killed=false",
    "SP2_killed=false",
    "JC2_resolved=false",
    "TD6-V77R-PURE-Q3-SCALAR-AUDIT PASS",
)


def normalized(data: bytes) -> bytes:
    return b"".join(
        line
        for line in data.splitlines(keepends=True)
        if not line.startswith(b"aws_")
    )


bodies = []
for host, (stdout_sha, stderr_sha, hostname) in expected.items():
    root = HERE / "evidence" / host
    stdout = root / "stdout"
    stderr = root / "stderr"
    assert digest(stdout) == stdout_sha
    assert digest(stderr) == stderr_sha
    assert (root / "rc").read_text().strip() == "0"
    assert f"hostname={hostname}" in (root / "launch.meta").read_text()
    text = stdout.read_text()
    for marker in required:
        assert marker in text, (host, marker)
    assert "Exit status: 0" in stderr.read_text()
    bodies.append(normalized(stdout.read_bytes()))

assert bodies[0] == bodies[1]
assert digest_bytes(bodies[0]) == "f6aaf1c9f4e9f1e6961525a5cf79fd53ac4e3ee226520e34d652a7642fdabf1e"

for host in ("box02", "r6d"):
    root = HERE / "control_v79a_stale_B_miscontrol" / host
    assert (root / "rc").read_text().strip() == "1"
    error = (root / "stderr").read_text()
    assert "assert first_rows_q2_leak != first_rows" in error
    assert "AssertionError" in error
    assert "TD6-V77R-PURE-Q3-SCALAR-AUDIT PASS" not in (root / "stdout").read_text()

print("TD6-V77R-FROZEN-CUSTODY PASS")
