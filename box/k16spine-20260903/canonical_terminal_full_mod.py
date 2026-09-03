#!/usr/bin/env python3
"""Emit full 2t-row b4=1 and b4=0 modular terminal tests.

This consumes the finite-field Laurent recurrence implementation shared in
``terminal_laurent_mod.py``.  All output from this wrapper is prefixed
``canonical_`` and is explicitly discovery-only.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "terminal_laurent_mod.py"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source():
    spec = importlib.util.spec_from_file_location("canonical_terminal_mod_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_mod(expr, variables, prime):
    return sp.Poly(sp.expand(expr), *variables, modulus=prime).as_expr()


def singular_text(t, prime, branch, yvalue, b4value, variables, rows):
    rendered = [str(row).replace("**", "^") for row in rows]
    return "\n".join([
        "// MEASURED-MODULAR DISCOVERY ONLY; not a characteristic-zero proof",
        "// full 2t terminal family after b4=%d" % b4value,
        "ring R=%d,(%s),dp;" % (prime, ",".join(map(str, variables))),
        "option(redSB);",
        'print("MAIN t=%d p=%d branch=%d y=%d b4=%d rows=%d vars=%d");'
        % (t, prime, branch, yvalue, b4value, len(rows), len(variables)),
        "ideal I=%s;" % ",\n".join(rendered),
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        'print("BASIS_SIZE");',
        "size(G);",
        "G;",
        "quit;",
    ]) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    parser.add_argument("--prime-start", type=int, default=1009)
    parser.add_argument("--run-singular", action="store_true")
    parser.add_argument("--from-existing", action="store_true",
                        help="consume terminal_mod_t*_p*_branch*.json")
    args = parser.parse_args()
    source = load_source()
    for t in args.t:
        if args.from_existing:
            paths = sorted(HERE.glob(f"terminal_mod_t{t}_p*_branch*.json"))
            if len(paths) != 2:
                raise RuntimeError(f"expected two existing t={t} fibre records: {paths}")
            originals = [json.loads(path.read_text(encoding="utf-8"))
                         for path in paths]
            prime = int(originals[0]["prime"])
            if any(int(item["prime"]) != prime for item in originals):
                raise AssertionError("existing records use different primes")
            yvalues = [int(item["y"]) for item in originals]
            discriminant_roots = []
        else:
            prime, discriminant_roots, yvalues = source.choose_prime_and_roots(
                t, args.prime_start
            )
            originals = [source.build_fibre(t, prime, yvalue)
                         for yvalue in yvalues]
        print(json.dumps({"phase": "parameters", "t": t, "prime": prime,
                          "discriminant_roots": discriminant_roots,
                          "yvalues": yvalues}), flush=True)
        for branch, (yvalue, original) in enumerate(zip(yvalues, originals)):
            b3, b4 = sp.symbols("b3 b4")
            qs = [sp.Symbol(f"q{i}_0") for i in range(2, t)]
            direct_variables = [b3] + qs
            z = sp.Symbol("z")
            rs = [sp.Symbol(f"r{i}") for i in range(2, t)]
            invariant_variables = [z] + rs
            terminal = [(item["band"], sp.sympify(item["expr"]))
                        for item in original["terminal"]]
            if [band for band, _expr in terminal] != list(range(2*t)):
                raise AssertionError("full terminal bands differ")
            rows_b4_1_direct = [canonical_mod(expr.subs(b4, 1),
                                               direct_variables, prime)
                                for _band, expr in terminal]
            rename = {b3: z}
            rename.update({q: r for q, r in zip(qs, rs)})
            rows_b4_1 = [canonical_mod(expr.subs(rename), invariant_variables, prime)
                         for expr in rows_b4_1_direct]
            rows_b4_0 = [canonical_mod(expr.subs(b4, 0), direct_variables, prime)
                         for _band, expr in terminal]
            record = {
                "typing": "MEASURED-MODULAR DISCOVERY ONLY",
                "source": {"path": SOURCE.name, "sha256": digest(SOURCE),
                           "recurrence_exact_validated_elsewhere_t2_t3_only": True},
                "t": t, "prime": prime, "branch": branch, "y": yvalue,
                "H_split_y_values": yvalues,
                "full_terminal_row_count": len(terminal),
                "terminal_bands": [band for band, _expr in terminal],
                "b4_1": {"variables": list(map(str, invariant_variables)),
                         "rows": [str(expr) for expr in rows_b4_1]},
                "b4_0": {"variables": list(map(str, direct_variables)),
                         "rows": [str(expr) for expr in rows_b4_0]},
                "laurent_record": original,
            }
            prefix = f"canonical_terminal_mod_t{t}_p{prime}_branch{branch}"
            json_path = HERE/f"{prefix}.json"
            json_path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                                 encoding="utf-8")
            jobs = []
            for b4value, variables, rows in (
                    (1, invariant_variables, rows_b4_1),
                    (0, direct_variables, rows_b4_0)):
                sing_path = HERE/f"{prefix}_b4_{b4value}.sing"
                sing_path.write_text(singular_text(t, prime, branch, yvalue,
                                                   b4value, variables, rows),
                                     encoding="utf-8")
                job = {"b4": b4value, "input": sing_path.name,
                       "input_sha256": digest(sing_path)}
                if args.run_singular:
                    out_path = HERE/f"{prefix}_b4_{b4value}.out"
                    err_path = HERE/f"{prefix}_b4_{b4value}.err"
                    with out_path.open("w", encoding="utf-8") as stdout, \
                            err_path.open("w", encoding="utf-8") as stderr:
                        completed = subprocess.run(
                            ["Singular", "-q", str(sing_path)], stdout=stdout,
                            stderr=stderr, check=False,
                        )
                    output = out_path.read_text(encoding="utf-8")
                    job.update({"exit_code": completed.returncode,
                                "output": out_path.name,
                                "output_sha256": digest(out_path),
                                "stderr": err_path.name,
                                "stderr_sha256": digest(err_path),
                                "stderr_empty": err_path.stat().st_size == 0,
                                "verdict": ("UNIT" if "UNIT" in output
                                            and "NONUNIT" not in output
                                            else "NONUNIT" if "NONUNIT" in output
                                            else "NO_VERDICT")})
                jobs.append(job)
            record["singular_jobs"] = jobs
            json_path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                                 encoding="utf-8")
            print(json.dumps({"phase": "branch_done", "t": t, "prime": prime,
                              "branch": branch, "y": yvalue,
                              "json": json_path.name, "jobs": jobs},
                             sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
