#!/usr/bin/env python3
"""Lightweight custody/marker verifier for the frozen V77 AWS package.

This script hashes and parses stored text only.  It never imports or executes
the heavy producer.
"""

from hashlib import sha256
from pathlib import Path
import tarfile


HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "archives" / "td6-aws-handoff-20260825-v77.tar.gz"


def digest_bytes(data):
    return sha256(data).hexdigest()


def digest(path):
    return digest_bytes(path.read_bytes())


assert digest(ARCHIVE) == (
    "333e25718c3e492497822b64c9b6e732cc6f26853bf2196a296ebc9db10a2293"
)

with tarfile.open(ARCHIVE, "r:gz") as archive:
    source_member = (
        "td6-aws-handoff-20260825-v77/jc2/cases/"
        "td6_c1_c2_c3_q3_gamma_dual_20260825/replay.py"
    )
    manifest_member = "td6-aws-handoff-20260825-v77/SOURCE.sha256"
    source = archive.extractfile(source_member).read()
    source_manifest = archive.extractfile(manifest_member).read()

assert digest_bytes(source) == (
    "5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22"
)
assert digest_bytes(source_manifest) == (
    "83eff5e28413162cb4f89379e4994a55462bf2520afaf564ffc7136991e259de"
)


def normalized_stdout(path):
    lines = path.read_text().splitlines(keepends=True)
    return "".join(
        line for line in lines
        if not line.startswith(("aws_hostname=", "aws_run_tag="))
    ).encode()


required = (
    "gamma_parameter_name=gamma",
    "q_gamma=t+gamma*t^3+t^25",
    "q_gamma_prime=1+3*gamma*t^2+25*t^24",
    "base_q2_beta=0",
    "scope_open=D(U*(C-3U^2)*B3)",
    "transport_rank=3470/3602",
    "transport_gamma_rhs_pivot_count=1",
    "transport_matrix_gamma_derivative_zero=true",
    "first_gamma_coefficient_count=221",
    "first_gamma_without_direct_qprime_count=2",
    "direct_qprime_omission_negative_control=true",
    "first_rank=38/132",
    "first_minor_gamma_sha256=c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1",
    "first_dual_original_row_replay=true",
    "genuine_P12_source_compiler=true",
    "raw_base_terms=2893",
    "raw_gamma_terms=4",
    "raw_gamma_sha256=70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c",
    "remainder_base_terms=1",
    "remainder_gamma_terms=3",
    "remainder_gamma_degree=1",
    "remainder_gamma_sha256=3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458",
    "dual_remainder_base_is_minus_k_over_50=true",
    "lambda_zero_source_row_support=28",
    "lambda_prime_source_row_support=14",
    "lambda0_bprime_terms=3386",
    "lambdaprime_b0_terms=3386",
    "derivative_source_identity_exact=true",
    "lambda_prime_omission_negative_control=true",
    "termwise_dual_slot_count=77512",
    "dual_denominator_radical_subset_U_H_B3=true",
    "source_base_multiplier_terms=1489",
    "source_gamma_support_terms=1149",
    "dual_emptiness_is_automatic_over_unit_base_ideal=true",
    "result_use=source_support_degree_denominator_discriminator_only",
    "gamma_independent_unit_identity=false",
    "finite_gamma_neighborhood_killed=false",
    "full_gamma_family_killed=false",
    "whole_TD6_killed=false",
    "SP2_killed=false",
    "JC2_resolved=false",
    "TD6-C1-C2-C3-Q3-GAMMA-DUAL-ADJOINT PASS",
)

expected = {
    "aws_box02": {
        "stdout": "c046639746e5916c0ff6226695d39aa11a0ed004838c5e8ffa544b6ebe226328",
        "stderr": "042831bb4bc7f5756bd859f428f153a0c432d718018addfd99e27025fcc2637e",
        "host": "ip-172-30-0-186",
    },
    "aws_box03": {
        "stdout": "0b0b953295c02325fd8ee9617cacc7b36ca2fd93b941c73c64bff2c1d100ea2b",
        "stderr": "7dcf34513dbf828b0aea7233e66d37173b82d720f3f9c0d590bbdb099f9c81e0",
        "host": "ip-172-30-0-249",
    },
}

normalized = []
for directory, metadata in expected.items():
    root = HERE / directory
    stdout = root / "v77.stdout"
    stderr = root / "v77.stderr"
    assert digest(stdout) == metadata["stdout"]
    assert digest(stderr) == metadata["stderr"]
    assert (root / "rc").read_text().strip() == "0"
    assert (root / "hostname").read_text().strip() == metadata["host"]
    text = stdout.read_text()
    for marker in required:
        assert marker in text, (directory, marker)
    assert "Exit status: 0" in stderr.read_text()
    body = normalized_stdout(stdout)
    assert digest_bytes(body) == (
        "52273c663073270c777c21d0da018f671b3e3e74cb892dc3e70b94749743f76c"
    )
    normalized.append(body)

assert normalized[0] == normalized[1]

for directory in ("box02", "box03"):
    root = HERE / "deployment_negative" / directory
    assert (root / "rc").read_text().strip() == "1"
    assert "ModuleNotFoundError: No module named 'flint'" in (
        root / "v77.stderr"
    ).read_text()
    assert "TD6-C1-C2-C3-Q3-GAMMA-DUAL-ADJOINT PASS" not in (
        root / "v77.stdout"
    ).read_text()

print("TD6-V77-AWS-CUSTODY PASS")
