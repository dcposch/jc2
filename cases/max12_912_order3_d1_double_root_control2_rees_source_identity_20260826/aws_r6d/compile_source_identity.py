#!/usr/bin/env python3
"""AWS-only compiler for exact polynomial identity of frozen A/B sources."""

from hashlib import sha256
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
A = HERE / "base_A.sing"
B = HERE / "base_B.sing"
A_SHA = "2b416cb8209dd9d220d8f57ec78044bddb7d83d5ea4899d59ab7b4b6b4f49e52"
B_SHA = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"
NAMES = [f"E{i}" for i in range(1, 9)] + ["LT"]


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_rees_source_identity_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def extract(path: Path, expected_sha: str) -> dict[str, str]:
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != expected_sha:
        raise SystemExit(f"REFUSE_HASH_{path.name}")
    text = raw.decode()
    out = {}
    for name in NAMES:
        matches = re.findall(rf"^poly {name}=(.*);$", text, flags=re.MULTILINE)
        if len(matches) != 1:
            raise SystemExit(f"REFUSE_ANCHOR_{path.name}_{name}_{len(matches)}")
        out[name] = matches[0]
    return out


def block(order: str, a: dict[str, str], b: dict[str, str], label: str) -> str:
    lines = [
        f"ring R{label}=0,(s,la,tau,rho,q1,q0,r2,r1,r0),{order};",
    ]
    for name in NAMES:
        lines.append(f"poly A{name}={a[name]};")
        lines.append(f"poly B{name}={b[name]};")
        lines.append(
            f'if (A{name}-B{name}!=0) '
            f'{{ print("FAIL_{label}_{name}"); A{name}-B{name}; quit; }}'
        )
        lines.append(f'print("PASS_{label}_{name}");')
    return "\n".join(lines)


def main() -> None:
    tag = require_aws()
    a = extract(A, A_SHA)
    b = extract(B, B_SHA)
    source = "\n".join(
        [
            "// Frozen A/B exact generator identity control.",
            f'print("AWS_TAG={tag}");',
            block("dp", a, b, "DP"),
            block("(lp(1),dp(8))", a, b, "LPDP"),
            'print("PASS_CONTROL2_REES_SOURCE_IDENTITY");',
            "quit;",
            "",
        ]
    )
    output = HERE / "source_identity.sing"
    output.write_text(source)
    print(f"base_A_sha256={A_SHA}")
    print(f"base_B_sha256={B_SHA}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("PASS_CONTROL2_REES_SOURCE_IDENTITY_COMPILER")


if __name__ == "__main__":
    main()
