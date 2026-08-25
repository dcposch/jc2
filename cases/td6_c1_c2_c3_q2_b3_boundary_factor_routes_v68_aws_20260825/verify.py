#!/usr/bin/env python3
"""Lightweight custody and strict-scope verifier for V68."""

from hashlib import sha256
from pathlib import Path
from tarfile import open as taropen


HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "archives/td6-aws-handoff-20260825-v68.tar.gz"
assert sha256(ARCHIVE.read_bytes()).hexdigest() == (
    "876751020cb4f4465b0314a3bd2d79c2a6afee5008feda17290a946e94f6126a"
)

for host, stderr_sha in (
    ("aws_box02", "f0bbde92d78151f60f4daf008e0737a7ed54ef3f9cc795b00f75c42cadab0619"),
    ("aws_r6d", "716a3f3c1819a067b20947ce0682c6757165c35a68cacc7a7c26ef9d92387a80"),
):
    assert (HERE / host / "rc").read_text() == "0\n"
    assert sha256((HERE / host / "v68.stdout").read_bytes()).hexdigest() == (
        "c84447f961863fcd0c80a82ed3ec28d0e6efcfe0f89fa7de4f9bc1d5c90ffdce"
    )
    assert sha256((HERE / host / "v68.stderr").read_bytes()).hexdigest() == stderr_sha
    assert sha256((HERE / host / "source-check.txt").read_bytes()).hexdigest() == (
        "67df7098a87190a7908ff3cdac22bcef338b82b6292173042822f2a4d557d2b6"
    )

with taropen(ARCHIVE, "r:gz") as archive:
    prefix = "td6-aws-handoff-20260825-v68/"
    expected = {
        "SOURCE.sha256": "c41520929a4edfb9923973890f3b8977fbb3d63a7671ae20fecbc489dc6b66a2",
        "route_replay.py": "4b528bad9e8d13994343d7ab747a855c41e93f3a975d35c993fac6f8bc8b061c",
        "evidence/u_zero/n13-u-zero.stdout":
            "94e2267d62b162f44abaf32d36405440dd213e1efb4f446cc281ace08b47d0da",
        "evidence/rational_lines/v46.stdout":
            "01fa0f2ef212f1280f7b1cc4530da867df331b0892053c44f3edf89e1bbf6706",
        "evidence/rational_lines/v45-v-cplus5-zero.stdout":
            "0be0c4093c27d21778853908afc90a3021831cb75a926a60981cffa4e166e8e2",
    }
    for relative, digest in expected.items():
        member = archive.extractfile(prefix + relative)
        assert member is not None
        assert sha256(member.read()).hexdigest() == digest, relative

out_box = (HERE / "aws_box02/v68.stdout").read_text()
out_r6d = (HERE / "aws_r6d/v68.stdout").read_text()
assert out_box == out_r6d
for marker in (
    "normalized_line_pencil_factorization_exact=true",
    "t_zero_route=x_minus1_or_x_minus5=true",
    "t_two_route=x_minus5_only=true",
    "w_zero_on_DU_routes_to_V_zero=true",
    "B3_at_V_zero=4*U^2*(C+U^2)*(C+5U^2)",
    "U_zero_direct_source_dependency_verified=true",
    "Cplus1_direct_source_dependency_verified=true",
    "Cplus5_direct_source_dependency_verified=true",
    "route_wrong_coefficient_negative_control=true",
    "route_missing_branch_negative_controls=true",
    "source_marker_omission_controls=true",
    "whole_B3_killed=false",
    "TD6-A3-Q2-B3-BOUNDARY-ROUTES-V68 PASS",
):
    assert marker in out_box, marker

print("TD6-V68-B3-BOUNDARY-ROUTE-CUSTODY PASS")
print("exact_scope=route_of_t0_w0_t2_into_U0_and_two_V0_lines")
print("whole_B3_cover_complete=false")
