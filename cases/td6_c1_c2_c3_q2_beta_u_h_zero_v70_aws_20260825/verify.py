#!/usr/bin/env python3
"""Lightweight evidence and custody verifier for V70."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def lines(path):
    return path.read_text().splitlines()


def value(path, key):
    prefix = key + "="
    found = [line[len(prefix):] for line in lines(path) if line.startswith(prefix)]
    assert len(found) == 1, (path, key, found)
    return found[0]


uh2 = HERE / "evidence/u-h-zero/box02/u-h-zero.stdout"
uh3 = HERE / "evidence/u-h-zero/box03/u-h-zero.stdout"
origin2 = HERE / "evidence/origin/box02/origin.stdout"
origin3 = HERE / "evidence/origin/box03/origin.stdout"
assert digest(uh2) == digest(uh3) == (
    "2431ed0217d8d71dce2929a8581036d0e11921396dff661466288901243f4ebd"
)
assert digest(origin2) == digest(origin3) == (
    "90df496c59c8283c85cec26521a2b422d6ca8d658aa0e8802c968052cd505d67"
)

for path in (uh2, uh3):
    assert value(path, "source_center") == "C=U=0 over Q(V)"
    assert value(path, "direct_qprime_retained") == "true"
    assert value(path, "transport_rank") == "3470/3602"
    assert value(path, "v70_transport_chart_denominator") == "(V^2)"
    assert value(path, "v70_first_source_denominator") == "(V)"
    assert value(path, "first_rank") == "36/132"
    assert value(path, "first_incompatibility[0]_key") == "('X-2', 14)"
    assert value(path, "first_incompatibility[0]_degree") == "0"
    assert value(path, "first_incompatibility[0]_source_row_count") == "14"
    assert value(path, "v70_first_complete_certificate_denominator") == "(V^3)"
    assert value(path, "v70_first_whole_raw_stratum_empty") == "false"
    assert value(path, "v70_first_incompatibility[0]_wrong_row_control") == "true"

for path in (origin2, origin3):
    assert value(path, "source_center") == "C=V=U=0"
    assert value(path, "direct_qprime_retained") == "true"
    assert value(path, "transport_rank") == "3468/3602"
    assert value(path, "transport_incompatibility[0]_row_index") == "6460"
    assert value(path, "transport_incompatibility[0]_key") == "('g', 'X', -19, 20)"
    assert value(path, "transport_incompatibility[0]_degree") == "0"
    assert value(path, "transport_incompatibility[0]_source_row_count") == "21"
    assert value(path, "v70_transport_complete_certificate_denominator") == "(1)"
    assert value(path, "v70_transport_whole_raw_stratum_empty") == "true"
    assert value(path, "v70_transport_incompatibility[0]_wrong_row_control") == "true"

for relative in (
    "evidence/u-h-zero/box02/rc",
    "evidence/u-h-zero/box03/rc",
    "evidence/origin/box02/rc",
    "evidence/origin/box03/rc",
    "evidence/controls/u-h-zero-omit-box02/rc",
    "evidence/controls/origin-omit-box02/rc",
):
    assert (HERE / relative).read_text() == "0\n"

uh_omit = HERE / "evidence/controls/u-h-zero-omit-box02/u-h-zero-omit.stdout"
origin_omit = HERE / "evidence/controls/origin-omit-box02/origin-omit.stdout"
assert value(uh_omit, "direct_qprime_retained") == "false"
assert value(origin_omit, "direct_qprime_retained") == "false"
for key in (
    "transport_rank",
    "v70_transport_chart_denominator",
    "first_rank",
    "first_incompatibility[0]_residual_sha256",
    "v70_first_complete_certificate_denominator",
):
    assert value(uh_omit, key) == value(uh2, key)
for key in (
    "transport_rank",
    "transport_incompatibility[0]_residual_sha256",
    "v70_transport_complete_certificate_denominator",
):
    assert value(origin_omit, key) == value(origin2, key)

assert digest(HERE / "source/replay_v70.py") == (
    "07cf6df3b4f7c5c43f02dcbc30bff118618630090cbc85bd0cb587975c303179"
)
assert digest(HERE / "source/td6-aws-handoff-20260825-v69.tar.gz") == (
    "9e89808cca9d24ec5182466b40e53d612317a4f03c70053a9c490e957ab51f38"
)
assert digest(
    ROOT / "xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-prereg-20260825.md"
) == "899c6df7438c9572a503b5a8039d110323ee9a35c8d13bddf5eb7aeb44f61cae"

for failure in (
    HERE / "evidence/operator-failure/origin-box02",
    HERE / "evidence/operator-failure/origin-box03",
):
    assert (failure / "rc").read_text() == "1\n"
    assert "KeyError: 'transport_source_denominator'" in (
        failure / "origin.stderr"
    ).read_text()

print("TD6-Q2-BETA-U-H-ZERO-V70 VERIFY PASS")
