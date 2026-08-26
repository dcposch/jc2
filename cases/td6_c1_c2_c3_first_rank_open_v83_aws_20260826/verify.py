#!/usr/bin/env python3
"""Lightweight custody verifier; performs no TD6 algebra."""

from hashlib import sha256
from pathlib import Path
import tarfile


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


assert digest(HERE / "source.tar.gz") == (
    "881c76cf9cbc3d8b10d6820dad95f366f8f5038c3fe08643ba6ed5c44a75d71f"
)

# Verify the complete recursive source manifest inside the portable archive.
with tarfile.open(HERE / "source.tar.gz", "r:gz") as archive:
    members = {}
    for member in archive.getmembers():
        if not member.isfile():
            continue
        name = member.name[2:] if member.name.startswith("./") else member.name
        stream = archive.extractfile(member)
        assert stream is not None
        members[name] = stream.read()
    source_manifest = members["V83_SOURCE.sha256"].decode()
    for line in source_manifest.splitlines():
        expected, rel = line.split(None, 1)
        rel = rel[2:] if rel.startswith("./") else rel
        assert rel in members, rel
        assert sha256(members[rel]).hexdigest() == expected, rel

expected_ledgers = {
    "FIRST_PIVOT_LEDGER.tsv":
        "475d9ed061ea36e0f683724374463ffd31e5b3bd552ac104a258f32dbd7cb9f0",
    "FIRST_RANK_OPEN_FACTORS.tsv":
        "bb990f4f6164d35ecf1af2151a951332ac55cc752dbda0435ca957867506ee7a",
    "RAW_FIBRE_SUCCESSORS.tsv":
        "56e9c2027a76a61273e44408664d499d089bafe75427401c3686df67e412af0e",
}
for host in ("r6d", "box03"):
    root = HERE / "evidence" / host
    assert (root / "rc").read_text() == "0\n"
    assert not (root / "wrapper.log").read_bytes()
    for name, expected in expected_ledgers.items():
        assert digest(root / "evidence" / name) == expected, (host, name)
    stdout = (root / "stdout").read_text()
    required = (
        "transport_rank=3470/3602;free=132",
        "packed_first_rank=38/132",
        "packed_first_dependent_count=0",
        "selected_minor_size=38x38",
        "raw_fibre_successor_count=1",
        "pivot_omission_negative_control=true",
        "plus_one_negative_control=true",
        "rank37_row_omission_control=true",
        "principal_open_is_not_promoted_to_D_U_H_B3=true",
        "TD6-A3-FIRST-RANK-OPEN-V83 PASS",
    )
    assert all(marker in stdout for marker in required), host
    assert "Exit status: 0" in (root / "stderr").read_text()

# The exact ledgers and mathematical streams agree across hosts.
for name in expected_ledgers:
    assert (
        (HERE / "evidence/r6d/evidence" / name).read_bytes()
        == (HERE / "evidence/box03/evidence" / name).read_bytes()
    )


def normalized_stdout(host):
    lines = (HERE / "evidence" / host / "stdout").read_text().splitlines()
    return "\n".join(
        line for line in lines
        if not line.startswith(("aws_hostname=", "aws_run_tag="))
    ) + "\n"


assert normalized_stdout("r6d") == normalized_stdout("box03")

factor_text = (HERE / "evidence/r6d/evidence/FIRST_RANK_OPEN_FACTORS.tsv").read_text()
assert "\trank38_principal_open:inverted" not in factor_text
assert "rank38_principal_open\tinverted\t1\textra\t" in factor_text
assert "C*V^2*U + 8*C*U^4 - 1/2*V^4 - 7*V^2*U^3 + 8*U^6" in factor_text
raw_text = (HERE / "evidence/r6d/evidence/RAW_FIBRE_SUCCESSORS.tsv").read_text()
assert "REQUIRES_ORIGINAL_SOURCE_REBUILD" in raw_text
assert raw_text.count("\n") == 2

print("TD6-V83-FIRST-RANK-OPEN-CUSTODY-VERIFY PASS")
