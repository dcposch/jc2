#!/usr/bin/env python3
"""Subprocess worker: one Groebner job, JSON in/out on argv files.

stdin unused.  argv:  cmd  in.json  out.json
cmds: d2e3_ab | moh1612
The parent kills the process group at the per-system cap.
"""
from __future__ import annotations

import json
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from solve import solve_d2e3_ab, solve_1612  # noqa: E402


def conv(o):
    if isinstance(o, dict):
        return {str(k): conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [conv(x) for x in o]
    if isinstance(o, (int, float, str, bool)) or o is None:
        return o
    return str(o)


def main():
    cmd, inp, outp = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(inp) as f:
        spec = json.load(f)
    if cmd == "d2e3_ab":
        r = solve_d2e3_ab(spec["n"], spec["m"], spec["M2"], spec["V2"], spec["k"],
                          timeout=spec.get("timeout", 10000), order=spec.get("order", "grevlex"))
    elif cmd == "moh1612":
        r = solve_1612(timeout=spec.get("timeout", 10000))
    else:
        r = dict(verdict="ERROR", error="unknown cmd %s" % cmd)
    # drop bulky C
    r.pop("C", None)
    with open(outp, "w") as f:
        json.dump(conv(r), f)
    print("WORKER_DONE", r.get("verdict"), file=sys.stderr)


if __name__ == "__main__":
    main()
