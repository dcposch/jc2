#!/usr/bin/env python3
"""Re-emit Singular jobs from a finished t*_canonical_audit.json.

Used after the pipeline so wrapper rings contain the Rabinowitsch variable W,
and so later emitter fixes apply without redoing the affine elimination.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import k16t56_pipeline as P  # noqa: E402


def emit(audit_path: pathlib.Path, primes: tuple[int, ...]) -> list[pathlib.Path]:
    audit = json.loads(audit_path.read_text())
    t = int(audit["t"])
    order = audit["order"]
    y = sp.Symbol(audit["grading"]["y"])
    remaining = [sp.Symbol(name) for name in audit["terminal"]["variables"]]
    H = sp.sympify(audit["normalizer"]["H"])
    cbar = audit["normalizer"]["cbar"]
    out_dir = audit_path.parent
    symbols = {str(y): y, **{str(v): v for v in remaining}}
    tp = P.load_module(P.LANE_INPUTS / "triangular_preprocess.py",
                       "emit_tp_%d" % t)
    generators = []
    for rec in audit["terminal"]["rows"]:
        expr = sp.sympify(rec["primitive"], locals=symbols)
        generators.append(tp.singular_polynomial(expr, [y] + remaining))
    written = []
    exact_std = out_dir / ("t%d_%s_exact_At_std.sing" % (t, order))
    exact_nf = out_dir / ("t%d_%s_exact_At_nfmodStd.sing" % (t, order))
    exact_qhy = out_dir / ("t%d_%s_exact_QHy_std.sing" % (t, order))
    exact_std.write_text(P.emit_extension(
        t, H, y, remaining, generators, cbar, "std"))
    exact_nf.write_text(P.emit_extension(
        t, H, y, remaining, generators, cbar, "nfmodStd"))
    exact_qhy.write_text(P.emit_qhy(
        t, H, y, remaining, generators, cbar, 0, "std"))
    written.extend([exact_std, exact_nf, exact_qhy])
    for prime in primes:
        path = out_dir / ("t%d_%s_mod_p%d_std.sing" % (t, order, prime))
        path.write_text(P.emit_qhy(
            t, H, y, remaining, generators, cbar, prime, "std"))
        written.append(path)
    classifier = out_dir / "actual_pair_classifier.sing"
    classifier.write_text(P.emit_actual_pair_classifier())
    written.append(classifier)
    for path in written:
        print(path.name, path.stat().st_size, P.sha256_file(path), flush=True)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audits", nargs="+", type=pathlib.Path)
    parser.add_argument("--primes", type=int, nargs="+",
                        default=list(P.DEFAULT_PRIMES))
    args = parser.parse_args()
    for path in args.audits:
        emit(path, tuple(args.primes))


if __name__ == "__main__":
    main()
