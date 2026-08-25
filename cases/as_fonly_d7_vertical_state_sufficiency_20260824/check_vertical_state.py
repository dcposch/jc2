#!/usr/bin/env python3
"""Independent literal-F3 test of the vertical D8 adjugate state criterion."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import os
import runpy
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GEN = (ROOT / "cases" / "as_fonly_d7_postd10_d98_f3_corrected_20260824"
       / "generate_corrected.py")
os.environ.pop("ENUMERATE", None)
os.environ.pop("STRUCTURAL", None)
os.environ["BRANCH"] = "vertical"
with contextlib.redirect_stdout(io.StringIO()):
    NS = runpy.run_path(str(GEN))

eval_expr = NS["eval_expr"]
rank = NS["matrix_rank_mod3"]
matrix = NS["core_matrix"]
rhs = NS["core_rhs"]

BASE_NAMES = ["Pp", "Qq", "Rr", "Tt", "s", "w", "h"]
FROB_NAMES = ["fua", "fa", "fb", "fc", "fd", "fvb"]


def trim(a):
    a = [x % 3 for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, scale=1):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += scale * x
    return trim(out)


def mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def smul(c, a):
    return trim([c*x for x in a])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    assert b
    if len(a) < len(b):
        return [], a
    q = [0] * (len(a)-len(b)+1)
    inv = 1 if b[-1] == 1 else 2
    while a and len(a) >= len(b):
        d = len(a)-len(b)
        c = a[-1]*inv % 3
        q[d] = c
        for i, x in enumerate(b):
            a[i+d] = (a[i+d]-c*x) % 3
        a = trim(a)
    return trim(q), a


def degree(a):
    return len(trim(a))-1


def state_test(base, bvec):
    P, Q, R, T, s, w, h = (base[n] for n in BASE_NAMES)
    A = trim([P, Q])
    B = trim([s*R, s*T+w*R, w*T])
    H = pow(h, 3, 3)
    # Matrix equations are M(X,Y)+b=0, so use target (u,v)=-b.
    u = trim([-x for x in bvec[:4]])
    v = trim([-x for x in bvec[4:]])
    Delta = add(mul(A, A), smul(H, B))
    nx = add(smul(-1, mul(A, u)), smul(-1, mul(B, v)))
    ny = add(smul(H, u), mul(A, v), scale=-1)

    if Delta:
        X, rx = divmod_poly(nx, Delta)
        Y, ry = divmod_poly(ny, Delta)
        residue_only = not rx and not ry
        exact = residue_only and degree(X) <= 2 and degree(Y) <= 1
        return exact, residue_only, "Delta_nonzero", (Delta, nx, ny, X, Y)

    if H:
        # Delta=0 and H is a unit: Y=0 and X=-H^-1*v suffices precisely
        # when the sole row syzygy H*u-A*v vanishes.
        exact = not ny
        return exact, exact, "Delta_zero_H_unit", (Delta, nx, ny, [], [])

    assert not A, (base, A, B, Delta)
    if not B:
        exact = not u and not v
        return exact, exact, "zero_matrix", (Delta, nx, ny, [], [])
    Y, rem = divmod_poly(u, B)
    exact = not v and not rem and degree(Y) <= 1
    return exact, exact, "Delta_zero_HA_zero_B_nonzero", (
        Delta, nx, ny, [], Y
    )


def main():
    total = compatible = 0
    types = Counter()
    compat_types = Counter()
    residue_without_cap_false_positive = 0
    cap_fail_patterns = Counter()
    mismatches = []
    fiber_hist = Counter()
    digest = hashlib.sha256()
    state_digest = hashlib.sha256()
    kind_code = {
        "Delta_nonzero": 0,
        "Delta_zero_H_unit": 1,
        "Delta_zero_HA_zero_B_nonzero": 2,
        "zero_matrix": 3,
    }
    for base_values in itertools.product(range(3), repeat=len(BASE_NAMES)):
        base = dict(zip(BASE_NAMES, base_values))
        fiber_compatible = 0
        for frob_values in itertools.product(range(3), repeat=len(FROB_NAMES)):
            assignment = dict(base)
            assignment.update(zip(FROB_NAMES, frob_values))
            numeric = [[eval_expr(x, assignment) for x in row]
                       for row in matrix]
            bvec = [eval_expr(x, assignment) for x in rhs]
            ra = rank(numeric)
            raug = rank([row+[b] for row, b in zip(numeric, bvec)])
            direct = ra == raug
            exact, residue_only, kind, witness = state_test(base, bvec)
            types[kind] += 1
            if direct:
                compatible += 1
                fiber_compatible += 1
                compat_types[kind] += 1
            if residue_only and not exact:
                residue_without_cap_false_positive += 1
                cap_fail_patterns[(degree(witness[3]),
                                   degree(witness[4]))] += 1
            if exact != direct and len(mismatches) < 20:
                mismatches.append((base_values, frob_values, direct, exact,
                                   kind, bvec, witness))
            digest.update(bytes(base_values+frob_values+(ra, raug)))
            state_digest.update(bytes(base_values+frob_values+(
                kind_code[kind], int(direct), int(exact), int(residue_only)
            )))
            total += 1
        fiber_hist[fiber_compatible] += 1

    print("total", total)
    print("compatible", compatible)
    print("types", sorted(types.items()))
    print("compatible_types", sorted(compat_types.items()))
    print("fiber_histogram", sorted(fiber_hist.items()))
    print("residue_without_cap_false_positive",
          residue_without_cap_false_positive)
    print("cap_fail_patterns", sorted(cap_fail_patterns.items()))
    print("rank_stream_sha256", digest.hexdigest())
    print("state_stream_sha256", state_digest.hexdigest())
    print("mismatch_count_prefix", len(mismatches))
    for item in mismatches:
        print("MISMATCH", item)
    assert not mismatches
    assert total == 1594323
    assert compatible == 314127
    assert dict(fiber_hist) == {0: 12, 3: 36, 9: 16, 81: 1904, 729: 219}
    assert digest.hexdigest() == (
        "e86fd1ec2724b5089039378c07e1a19a089042eeb4172b0342474f85d4d8b23d"
    )
    print("PASS-VERTICAL-STATE-SUFFICIENCY")


if __name__ == "__main__":
    main()
