#!/usr/bin/env python3
"""Generate bounded TOP-TAIL quotient/determinant probes from the frozen emitter."""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import subprocess


FROZEN = pathlib.Path("/tmp/jc2-lane.ZvRDkK/inputs/top_tail_fast_recurrence.py")
HERE = pathlib.Path(__file__).resolve().parent


def load_frozen():
    spec = importlib.util.spec_from_file_location("frozen_top_tail", FROZEN)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen recurrence")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("--mode", choices=("exact", "split-exact", "mod"), default="mod")
    parser.add_argument("--prime", type=int, default=1009)
    parser.add_argument("--branch", type=int, choices=(0, 1), default=0)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--dump-basis", action="store_true")
    parser.add_argument("--dump-leading", action="store_true")
    parser.add_argument("--dump-row-leading", action="store_true")
    parser.add_argument("--no-det", action="store_true")
    parser.add_argument("--tag", default="")
    args = parser.parse_args()

    frozen = load_frozen()
    prime = args.prime if args.mode == "mod" else None
    branch = args.branch if args.mode in ("mod", "split-exact") else None
    source, _ = frozen.emit(args.t, args.mode, prime, branch, "top", None, False)

    residual = ["b3", *[f"q{j}_0" for j in range(2, args.t)]]
    omitted = "I[1]"
    generators = ",".join(f"I[{j}]" for j in range(2, args.t + 1))
    va = "*".join(residual)
    dump = "GJ; KB;" if args.dump_basis else ""
    leading = ""
    if args.dump_leading:
        leading = "int lli; for (lli=1; lli<=size(GJ); lli++) { lead(GJ[lli]); }"
    row_leading = ""
    if args.dump_row_leading:
        row_leading = "int rri; int rrd; for (rri=2; rri<=" + str(args.t) + "; rri++) { rrd=deg(I[rri]); jet(I[rri],rrd)-jet(I[rri],rrd-1); }"
    determinant = [] if args.no_det else [
        "int DD=vdim(GJ);",
        "matrix MM[DD][DD]; matrix CC; poly rrnf; int jj;",
        f"poly va={va};",
        "for (jj=1; jj<=DD; jj++)",
        "{",
        f"  rrnf=reduce(({omitted})*KB[jj],GJ);",
        "  CC=coeffs(rrnf,KB,va);",
        "  MM[jj,1..DD]=CC[1..DD,1];",
        "}",
        "poly DELTA=det(MM);",
        'print("PROBE_DELTA"); DELTA;',
    ]
    injected = "\n".join([
        f"ideal J={generators};",
        "ideal GJ=std(J);",
        'print("PROBE_DIM"); int PROBE_D=dim(GJ); PROBE_D;',
        'if (PROBE_D!=0) { print("PROBE_NOT_ZERO_DIMENSION"); quit; }',
        "vdim(GJ); size(GJ);",
        "ideal KB=kbase(GJ);",
        dump,
        row_leading,
        leading,
        *determinant,
        'print("PROBE_DONE");',
        "quit;",
    ])
    needle = "ideal I=imap(R,Itop);\noption(redSB);"
    if needle not in source:
        raise RuntimeError("injection point absent")
    source = source.replace(needle, needle + "\n" + injected, 1)

    suffix = f"_{args.tag}" if args.tag else ""
    stem = f"probe_t{args.t}_{args.mode}_b{branch}{suffix}"
    sing = HERE / f"{stem}.sing"
    out = HERE / f"{stem}.out"
    err = HERE / f"{stem}.err"
    sing.write_text(source, encoding="utf-8")
    try:
        run = subprocess.run(
            ["Singular", "--cpus=4", "--threads=4", "--flint-threads=4", "-q", str(sing)],
            capture_output=True,
            timeout=args.timeout,
            check=False,
        )
        out.write_bytes(run.stdout)
        err.write_bytes(run.stderr)
        print(f"exit={run.returncode} out={out} err={err}")
    except subprocess.TimeoutExpired as exc:
        out.write_bytes(exc.stdout or b"")
        err.write_bytes(exc.stderr or b"")
        print(f"exit=124 timeout={args.timeout} out={out} err={err}")


if __name__ == "__main__":
    main()
