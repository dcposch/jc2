#!/usr/bin/env python3
"""Exact DATA observation only; run solely in a registered JC2-JOB/v1 worker."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

TIER = "OBSERVATION/UNREVIEWED"
MAX_DATA_BYTES = 7 * 1024 * 1024
HQ = "i-0252f535410c26ebc"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def guard(args):
    # No scientific import, output creation, or arithmetic before this guard.
    require(re.fullmatch(r"i-[0-9a-f]{17}", args.instance) is not None,
            "invalid exact instance")
    require(args.instance != HQ, "HQ forbidden")
    require(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,59}", args.job_tag) is not None,
            "invalid job tag")
    require(os.uname().sysname == "Linux", "Linux required")
    require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip() == "Amazon EC2",
            "AWS EC2 required")
    require(Path("/sys/class/dmi/id/board_asset_tag").read_text().strip() == args.instance,
            "instance mismatch")
    require(Path("/proc/self/cgroup").read_text().strip() ==
            "0::/system.slice/jc2-job-" + args.job_tag + ".service",
            "exact job cgroup required")
    require(os.getresuid() == (65534, 65534, 65534) and
            os.getresgid() == (65534, 65534, 65534), "runner credentials required")
    root = Path("/var/lib/jc2-jobs") / args.job_tag
    output = root / "output"
    require(os.environ.get("JC2_JOB_OUTPUT") == str(output) and
            os.environ.get("JC2_JOB_PAYLOAD") == str(root / "payload"),
            "runner environment mismatch")
    require(Path.cwd() == output and output.resolve(strict=True) == output,
            "canonical runner output cwd required")
    return output


def event(phase, state):
    print(json.dumps({"tier": TIER, "phase": phase, "state": state,
                      "utc": datetime.now(timezone.utc).isoformat(),
                      "monotonic_ns": str(time.monotonic_ns())}, sort_keys=True), flush=True)
    os.fsync(sys.stdout.fileno())  # runner owns a regular durable phase stdout


def checkpoint(directory, name, data):
    raw = (json.dumps({"tier": TIER, "schema": "JC2-EXACT-DATA/v1", **data},
                      sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    require(len(raw) <= MAX_DATA_BYTES, "checkpoint exceeds 7 MiB bound")
    final = directory / (name + ".json")
    partial = directory / (name + ".json.partial")
    require(not final.exists() and not final.is_symlink(), "checkpoint already exists")
    with partial.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.link(partial, final)  # no-overwrite publication; failure keeps partial
    partial.unlink()
    fd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    event(name, "CHECKPOINT " + hashlib.sha256(raw).hexdigest())


def observe(args, directory):
    event("dependencies", "BEGIN")
    import sympy as s
    from math import factorial

    t, X, Y = s.symbols("t X Y")

    def rational(value):
        value = s.Rational(value)
        return str(value.p) + "/" + str(value.q)

    def polydata(poly):
        return {"variables": [str(v) for v in poly.gens],
                "terms": [{"exponents": [str(e) for e in powers],
                           "coefficient": rational(coefficient)}
                          for powers, coefficient in poly.terms()]}

    def classify(poly, unit, factors):
        rebuilt = s.Poly(unit, t, domain=s.QQ)
        for factor, multiplicity in factors:
            require(factor.gens == (t,) and factor.degree() >= 1 and
                    isinstance(multiplicity, int) and multiplicity >= 1,
                    "invalid factor shape")
            rebuilt *= factor ** multiplicity
        require(rebuilt == poly, "factor-product mismatch")
        roots, candidates = [], []
        for factor, multiplicity in factors:
            if factor.degree() != 1:
                continue
            root = -factor.nth(0) / factor.nth(1)
            require(poly.eval(root) == 0, "linear root reconstruction mismatch")
            item = {"t": rational(root), "multiplicity": str(multiplicity)}
            if 3 * root - 5 == 0:
                item["r"] = "NO_FINITE_R"
            else:
                r = s.cancel((2 - root) / (3 * root - 5))
                item["r"] = rational(r)
                if r.q == 1 and r >= 2:
                    require((5 * r + 2) / (3 * r + 1) == root,
                            "parameter inverse mismatch")
                    candidates.append(str(r.p))
            roots.append(item)
        return roots, sorted(set(candidates), key=int)

    checkpoint(directory, "00-dependencies", {
        "python": sys.version, "executable": sys.executable,
        "sympy_version": s.__version__, "sympy_file": s.__file__,
        "sympy_init_sha256": hashlib.sha256(Path(s.__file__).read_bytes()).hexdigest(),
        "observer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "instance": args.instance, "job_tag": args.job_tag,
        "note": "These are observations, not native/library qualification."})
    event("dependencies", "END")

    if args.mode == "smoke":
        event("smoke", "BEGIN")
        sample = s.Poly((7*t-12)*(t*t+1), t, domain=s.QQ)
        unit, factors = sample.factor_list()
        roots, candidates = classify(sample, unit, factors)
        require(candidates == ["2"], "positive smoke candidate mismatch")
        try:
            classify(sample, unit + 1, factors)
        except ValueError as exc:
            require(str(exc) == "factor-product mismatch", "wrong negative smoke cause")
        else:
            raise ValueError("corrupted factor product was accepted")
        checkpoint(directory, "01-smoke", {
            "positive_candidates": candidates, "linear_roots": roots,
            "negative_control": "factor-product mismatch rejected",
            "scope": "Synthetic factor/classification smoke only; no resultant validation."})
        event("smoke", "END")
        return

    event("reconstruct", "BEGIN")
    p3 = lambda expression: s.Poly(expression, t, X, Y, domain=s.QQ)
    p2 = lambda expression: s.Poly(expression, t, X, domain=s.QQ)
    zero3, one3 = p3(0), p3(1)

    def truncated_power(exponent):
        # [u^n](1+u+Xu^2+Yu^3)^exponent by literal multinomial expansion.
        falling = [s.Integer(1)]
        for ell in range(1, 8):
            falling.append(s.expand(falling[-1] * (exponent - ell + 1)))
        coefficients = []
        for n in range(8):
            coefficient = zero3
            for k in range(n // 3 + 1):
                for j in range((n - 3*k) // 2 + 1):
                    a = n - 2*j - 3*k
                    ell = a + j + k
                    coefficient += p3(falling[ell] * X**j * Y**k /
                                      (factorial(a)*factorial(j)*factorial(k)))
            coefficients.append(coefficient)
        return coefficients

    inverse = [one3]
    for n in range(1, 15):
        inverse.append(-inverse[n-1] - (p3(X)*inverse[n-2] if n >= 2 else zero3)
                       - (p3(Y)*inverse[n-3] if n >= 3 else zero3))
    logderivative = [inverse[n] + (p3(2*X)*inverse[n-1] if n >= 1 else zero3)
                     + (p3(3*Y)*inverse[n-2] if n >= 2 else zero3)
                     for n in range(15)]
    left, right = truncated_power(2*t-1), truncated_power(4-t)
    B = zero3
    for i in range(8):
        for j in range(8):
            B += logderivative[14-i-j] * left[i] * right[j]
    U = p2(3*X**2 - 3*(t-1)*X - (t-3)*(3*t-4)/4)
    V = p2(X**3 + (t-3)*(t-1)*X**2 + (t-3)*(t-4)*(4*t-5)*X/20
           + (t-3)*(t-4)*(t-5)*(3*t-4)/420)
    K = p2(X**3 + 3*(t-3)*X**2/2 + (t-3)*(t-4)*X/4
           + (t-3)*(t-4)*(t-5)/120)
    P0 = 3*V**2 + p2(t-2)*(p2(6*X+t-3)*V*U + K*U**2)
    upowers, vpowers = [U**k for k in range(6)], [V**k for k in range(6)]
    G = p2(0)
    for (i, j, k), coefficient in B.terms():
        require(i+j+2*k <= 14 and 2*j+3*k <= 15 and k <= 5 and j+k <= 7,
                "mixed B support outside imported bounds")
        G += p2(coefficient*t**i*X**j) * vpowers[k] * upowers[5-k]
    checkpoint(directory, "01-reconstructed", {
        "P0": polydata(P0), "U": polydata(U), "V": polydata(V),
        "B": polydata(B), "G": polydata(G), "generic_X_degree_G": str(G.degree(X)),
        "definition": "B=[u^14](phi'/phi)trunc_7(phi^(2t-1))trunc_7(phi^(4-t)); phi=1+u+Xu^2+Yu^3"})
    require(P0.degree(X) == 7 and P0.total_degree() <= 8 and
            G.degree(X) <= 17 and G.total_degree() <= 24, "degree bounds mismatch")
    event("reconstruct", "END")

    event("resultant", "BEGIN")
    # Exactly one resultant over QQ[t], retaining the literal G normalization.
    domain = s.QQ.poly_ring(t)
    px = s.Poly(P0.as_expr(), X, domain=domain)
    gx = s.Poly(G.as_expr(), X, domain=domain)
    R = s.Poly(px.resultant(gx), t, domain=s.QQ)
    checkpoint(directory, "02-resultant", {"R": polydata(R),
        "generic_X_degree_G": str(G.degree(X)), "orientation": "Res_X(P0,G)"})
    require(not R.is_zero and R.degree() <= 185, "resultant zero or degree mismatch")
    event("resultant", "END")

    event("deflate", "BEGIN")
    cube_factor = s.Poly((3*t-5)**34, t, domain=s.QQ)
    Q, remainder = R.div(cube_factor)
    checkpoint(directory, "03-deflated", {"Q": polydata(Q),
        "divisor": polydata(cube_factor), "remainder": polydata(remainder)})
    require(remainder.is_zero and Q*cube_factor == R, "cube division not exact")
    require(not Q.is_zero and Q.degree() <= 151 and Q.eval(s.Rational(5, 3)) != 0,
            "deflated polynomial violates imported bounds or exact multiplicity")
    event("deflate", "END")

    event("factor", "BEGIN")
    unit, factors = Q.factor_list()
    # Preserve the engine output even if the subsequent full reconstruction fails.
    checkpoint(directory, "04-factor-data", {"unit": rational(unit),
        "factors": [{"polynomial": polydata(f), "multiplicity": str(m)} for f, m in factors]})
    roots, candidates = classify(Q, unit, factors)
    checkpoint(directory, "05-observation", {"factor_product_reconstructed": True,
        "linear_roots": roots, "candidate_integer_r_ge_2": candidates,
        "limitation": "Engine factor labels and resultant unreviewed; no independent certificate, source-zero, or JC2 inference."})
    event("factor", "END")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instance", required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--mode", choices=("smoke", "observe"), required=True)
    args = parser.parse_args()
    output = guard(args)
    # Atomic exclusive directory creation refuses rerun, including empty prior output.
    directory = output / ("mixed-resultant-" + args.mode)
    directory.mkdir(mode=0o750)
    try:
        observe(args, directory)
    except BaseException:
        original = traceback.format_exc()
        sys.stderr.write(original)
        sys.stderr.flush()
        try:
            os.fsync(sys.stderr.fileno())
            checkpoint(directory, "99-error", {"traceback": original})
        except BaseException:
            sys.stderr.write("Error checkpoint failed; original traceback above remains authoritative.\n")
            traceback.print_exc()
            sys.stderr.flush()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
