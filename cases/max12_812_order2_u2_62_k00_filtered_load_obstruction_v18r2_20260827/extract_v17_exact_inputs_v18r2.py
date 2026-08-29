#!/usr/bin/env python3
"""Extract exact six-row V17 images/targets before its local-colon blocks."""

from __future__ import annotations

import argparse
from hashlib import sha256
import os
from pathlib import Path
import platform


EXPECTED_SOURCE = "9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c"
EXPECTED_P_RESULT = "6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc"
LOADS = ("K10", "K6", "K2")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only exact-input extractor refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only exact-input extractor refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def between(text: str, start: str, stop: str, offset: int = 0) -> str:
    left = text.find(start, offset)
    if left < 0:
        fail(("missing start marker", start))
    right = text.find(stop, left)
    if right < 0:
        fail(("missing stop marker", stop))
    return text[left:right]


def direction_block(text: str, suffix: str) -> str:
    image = between(text, f"ideal Load{suffix}=", f"ideal GE{suffix}=std(E{suffix});")
    target = between(text, f"poly D{suffix}=h*", f"ideal J{suffix}=I,E{suffix};")
    return "\n".join([
        f'print("K00_V18_EXACT_INPUT_{suffix}_START");',
        image.rstrip(),
        target.rstrip(),
        f'write("LOAD_ROWS_{suffix}.txt",Load{suffix});',
        f'write("IMAGE_{suffix}.txt",E{suffix});',
        f'write("TARGET_{suffix}.txt",D{suffix});',
        f'print("K00_V18_EXACT_INPUT_{suffix}_IMAGE_GENERATORS="+string(size(E{suffix})));',
        f'print("K00_V18_EXACT_INPUT_{suffix}_DONE");',
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("compiled_v17_q", type=Path)
    parser.add_argument("p_v17_result", type=Path)
    parser.add_argument("output_singular", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    if digest(args.compiled_v17_q) != EXPECTED_SOURCE:
        fail(("compiled V17-Q hash mismatch", digest(args.compiled_v17_q)))
    if digest(args.p_v17_result) != EXPECTED_P_RESULT:
        fail(("V17-p result hash mismatch", digest(args.p_v17_result)))
    text = args.compiled_v17_q.read_text()
    prefix_stop = text.find("module S87=")
    if prefix_stop < 0:
        fail("missing seven-row-module boundary")
    prefix = text[:prefix_stop]
    if 'print("K00_V17_SYZ6_REPLAY="+string(treplay));' not in prefix:
        fail("six-row replay sentinel missing from exact source")
    blocks = [direction_block(text, suffix) for suffix in LOADS]
    output = prefix + "\n" + '\n'.join([
        'if ((nt!=66)||(treplay!=1)) { print("K00_V18_EXACT_INPUT_FAIL=SYZ6"); quit; }',
        'write("SYZ6_MODULE.txt",T);',
        *blocks,
        f'print("K00_V18_EXACT_INPUT_SOURCE_SHA256={EXPECTED_SOURCE}");',
        f'print("K00_V18_EXACT_INPUT_P_RESULT_SHA256={EXPECTED_P_RESULT}");',
        f'print("K00_V18_EXACT_INPUT_LANE={tag}");',
        'print("K00_V18_EXACT_INPUT_DONE");',
        'quit;',
        '',
    ])
    args.output_singular.parent.mkdir(parents=True, exist_ok=False)
    args.output_singular.write_text(output)
    print("K00_V18_EXACT_INPUT_COMPILER=PASS")
    print(f"K00_V18_EXACT_INPUT_COMPILED_SHA256={digest(args.output_singular)}")


if __name__ == "__main__":
    main()
