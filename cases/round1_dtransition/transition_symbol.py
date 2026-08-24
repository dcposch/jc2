#!/usr/bin/env python3
"""Exact X27 -> X25 relative-band discriminator from the D25 source.

This tool deliberately does not import any D43 driver or artifact.  It
reconstructs certified points of the promoted modular D25 cells and invokes
the unreduced product/Euler recurrence in ``valuation_e2.py``.  X27 is the
same source system with the single next even residual band, band 26.  The
projection forgets exactly the ten source coefficients whose measured first
occurrence is band 26.

The output is a pointwise, first-order modular signal.  Relative ranks are
not component dimensions, do not prove dominance or emptiness, and say
nothing about an inverse limit.

Run with the Python carrying NumPy, for example:

  /opt/homebrew/opt/python@3.14/bin/python3.14 \
      cases/round1_dtransition/transition_symbol.py --selftest
  /opt/homebrew/opt/python@3.14/bin/python3.14 \
      cases/round1_dtransition/transition_symbol.py --run \
      --out cases/round1_dtransition/samples.json
"""

import argparse
import hashlib
import json
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.dirname(HERE)
ROOT = os.path.dirname(CASES)
sys.path.insert(0, CASES)

import d25_eplus as DE
import valuation_e as V
import valuation_e2 as V2


TOOL = "cases/round1_dtransition/transition_symbol.py"
PRIMES = (105337, 105673)
FIBER = "a00pp"
D25_LAST_BAND = 24
NEXT_BAND = 26
ORDINARY = ("tf1", "tf2", "tg1", "tg2")
NEW_COORDS = ([(f, NEXT_BAND - 5) for f in ORDINARY] +
              [(f, NEXT_BAND) for f in V2.FAMS])
S30 = list(V2.S_A) + [V2.S_29]
NEW_ROWS = [a for a in range(30)
            if S30[a] <= NEXT_BAND and
            S30[a] % 6 == NEXT_BAND % 6]

# Files that define the source recurrence, D25 reconstruction, and the two
# sampled promoted modular cells.  Runtime data are hashed rather than
# trusted by filename.  /tmp/directionb_tails_D21.pkl, if restored by the
# banked loader, must equal the repository copy byte for byte.
SOURCE_FILES = [
    "directionb_tails_D21.pkl",
    "cases/r1_experiment.py",
    "cases/r1_fullcore.py",
    "cases/directionb_compress.py",
    "cases/directionb_residual32_emit.py",
    "cases/valuation_e.py",
    "cases/valuation_e2.py",
    "cases/d25_eplus.py",
    "cases/d25_certificate_replay.json",
]
for _p in PRIMES:
    SOURCE_FILES += [
        "cases/d23_atlas_p%d.json" % _p,
        "cases/d25fam_p%d_a00pp.ms" % _p,
        "cases/directionb_core23_p%d.ms" % _p,
        "cases/directionb_row22compat_p%d.ms" % _p,
        "cases/directionb_row22red_p%d.ms" % _p,
    ]


class TypedMapError(RuntimeError):
    """A fail-closed source/provenance/type failure."""


def require(condition, message):
    if not condition:
        raise TypedMapError(message)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def json_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        .encode()).hexdigest()


def source_manifest():
    out = {}
    for rel in SOURCE_FILES:
        path = os.path.join(ROOT, rel)
        require(os.path.isfile(path), "missing source artifact: %s" % rel)
        out[rel] = {"bytes": os.path.getsize(path),
                    "sha256": sha256_file(path)}
    # The banked loader may restore this cache.  It is not a second source.
    V.raw_rows21()
    tmp = "/tmp/directionb_tails_D21.pkl"
    require(os.path.isfile(tmp), "banked D21 source cache was not restored")
    require(sha256_file(tmp) == out["directionb_tails_D21.pkl"]["sha256"],
            "/tmp D21 source differs from the repository artifact")
    return out


def rref(matrix, p):
    """Canonical modular RREF plus pivot columns/original pivot rows."""
    M = [[int(x) % p for x in row] for row in matrix]
    if not M:
        return M, [], []
    nrow, ncol = len(M), len(M[0])
    origin = list(range(nrow))
    pivots, pivot_rows = [], []
    r = 0
    for c in range(ncol):
        q = next((i for i in range(r, nrow) if M[i][c]), None)
        if q is None:
            continue
        M[r], M[q] = M[q], M[r]
        origin[r], origin[q] = origin[q], origin[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c]:
                m = M[i][c]
                M[i] = [(x - m * y) % p for x, y in zip(M[i], M[r])]
        pivots.append(c)
        pivot_rows.append(origin[r])
        r += 1
        if r == nrow:
            break
    return M, pivots, pivot_rows


def rank(matrix, p):
    return len(rref(matrix, p)[1])


def kernel_basis(matrix, p):
    """Basis of the right kernel, with one vector per canonical free col."""
    R, pivots, _ = rref(matrix, p)
    ncol = len(matrix[0]) if matrix else 0
    free = [j for j in range(ncol) if j not in pivots]
    basis = []
    for f in free:
        v = [0] * ncol
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-R[i][f]) % p
        basis.append(v)
    return basis, pivots, free


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matvec(A, x, p):
    return [sum(a * b for a, b in zip(row, x)) % p for row in A]


def determinant(matrix, p):
    M = [[int(x) % p for x in row] for row in matrix]
    n = len(M)
    det = 1
    for c in range(n):
        q = next((i for i in range(c, n) if M[i][c]), None)
        if q is None:
            return 0
        if q != c:
            M[c], M[q] = M[q], M[c]
            det = -det
        pivot = M[c][c]
        det = det * pivot % p
        inv = pow(pivot, p - 2, p)
        for i in range(c + 1, n):
            if M[i][c]:
                m = M[i][c] * inv % p
                for j in range(c, n):
                    M[i][j] = (M[i][j] - m * M[c][j]) % p
    return det % p


def solve(A, b, p):
    """Canonical particular solution (free columns zero), or None."""
    aug = [list(row) + [int(bb) % p] for row, bb in zip(A, b)]
    R, pivots_aug, _ = rref(aug, p)
    n = len(A[0])
    if n in pivots_aug:
        return None
    pivots = [c for c in pivots_aug if c < n]
    for row in R:
        if not any(row[:n]) and row[n]:
            return None
    x = [0] * n
    for i, c in enumerate(pivots):
        x[c] = R[i][n]
    require(matvec(A, x, p) == [bb % p for bb in b],
            "internal modular solve replay failed")
    return x


def point_copy(point):
    return {"tails": {f: dict(point["tails"][f]) for f in V2.FAMS},
            "fixed": dict(point["fixed"]),
            "zc_hash": point["zc_hash"]}


def build_E(point, p, Z):
    jf, jg = V2.build_jets(point, p, Z)
    E = V2.euler_rows(jf, jg, p)
    independent_gradient = V2.path_A_rows(jf, jg, p)
    require(np.array_equal(E.G[:, :NEXT_BAND + 1],
                           independent_gradient[:, :NEXT_BAND + 1]),
            "dual-jet and independently grouped source derivatives differ")
    return E


def set_new_vector(point, vector, p):
    q = point_copy(point)
    for (fam, r), value in zip(NEW_COORDS, vector):
        require(r not in q["tails"][fam],
                "new coordinate already belongs to the D25 point: %s_%d"
                % (fam, 32 + r))
        if value % p:
            q["tails"][fam][r] = int(value) % p
    return q


def d25_sample(p, kind):
    """Reconstruct one exact a00pp D25 cell point and its completion."""
    env = DE.fiber_env(p, FIBER)
    require(env["is_radical_frame"], "a00pp radical frame drifted")
    header, rows = DE.parse_fiber_ms(p, FIBER)
    cells = DE.cells_of_fiber(p, FIBER)
    if kind == "witness":
        cellval = DE.witness_cellval(p, FIBER)
        free_values = None
        cell = cells.index((int(cellval["W1"]), int(cellval["W2"])))
    elif kind == "interior-sequence":
        free_values = {name: i + 1 for i, name in
                       enumerate(DE.FREE_BASE + DE.FREE_LIFT)}
        cell = 0
        cellval = DE.solve_cell_point(p, header, rows, free_values,
                                      *cells[cell])
    else:
        raise ValueError(kind)
    bad = [i for i, row in enumerate(rows)
           if DE.eval_row(row, cellval, p)]
    require(not bad, "sample is not on the 34-row D25 cell: %r" % bad)
    require(int(cellval["W1"]) % p and int(cellval["W2"]) % p,
            "sample left the W1*W2 non-origin chart")

    dval, reconstruction = DE.reconstruct_point(p, cellval, env)
    pristine = DE.verify_full_point(p, dval, env, a00pp_frozen=True)
    require(all(pristine.values()),
            "D25 pristine reconstruction failed: %r" % pristine)
    wit72, deep = DE.witness72_of(p, dval)
    point = DE.build_point_f(p, wit72, deep, env)
    zpoint, _r3, _h = V.radical_env(p)
    Z = [pow(zpoint["z"], m, p) for m in range(42)]
    E = build_E(point, p, Z)
    frontier = {"applied": False, "values": {}}
    if E.V.astype(np.int64)[:30, D25_LAST_BAND].any():
        y, diag = DE.frontier_solve(E, p)
        require(y is not None, "promoted D25 frontier completion failed")
        frontier = {"applied": True,
                    "diag": diag,
                    "values": {"%s_%d" % (f, 32 + r): int(v)
                               for (f, r), v in y.items()}}
        for (fam, r), value in y.items():
            if value:
                point["tails"][fam][r] = int(value)
        E = build_E(point, p, Z)
    values = E.V.astype(np.int64) % p
    require(not values[:, :D25_LAST_BAND + 1].any(),
            "reconstructed D25 point has a residual through band 24")
    for fam, r in NEW_COORDS:
        require(r not in point["tails"][fam],
                "D25 completion already assigns an X27-only coordinate")
    meta = {
        "prime": p,
        "fiber": FIBER,
        "cell": cell,
        "kind": kind,
        "free_values": free_values,
        "nonorigin_chart": bool(cellval["W1"] % p and cellval["W2"] % p),
        "cell_34_rows_zero": True,
        "pristine_checks": pristine,
        "reconstruction": reconstruction,
        "frontier": frontier,
        "cell_point_sha256": json_hash(
            sorted((str(k), int(v)) for k, v in cellval.items())),
        "completed_point_sha256": json_hash({
            "fixed": sorted((k, int(v)) for k, v in point["fixed"].items()),
            "tails": {f: sorted((int(r), int(v)) for r, v in
                                 point["tails"][f].items())
                      for f in V2.FAMS},
        }),
    }
    return point, E, Z, meta


def first_support_census(G):
    first = {}
    for label, c in V2.GIDX.items():
        hit = next((n for n in range(V2._S)
                    if G[:, n, c].any()), None)
        first[label] = hit
    return first


def audit_sample(p, kind):
    point, E, Z, meta = d25_sample(p, kind)
    V0 = E.V.astype(np.int64) % p
    G0 = E.G.astype(np.int64) % p
    columns = [V2.GIDX[x] for x in NEW_COORDS]

    # Exact projection/type gates.  The source engine itself identifies
    # precisely ten first-occurrence columns at band 26.
    census = first_support_census(G0)
    got_new = sorted(label for label, band in census.items()
                     if band == NEXT_BAND)
    require(got_new == sorted(NEW_COORDS),
            "source first-occurrence census is not the declared ten")
    require(not G0[:, :NEXT_BAND, :][:, :, columns].any(),
            "X27-only coordinate changes an X25 equation")
    outside = [a for a in range(V2.HMAX)
               if (V0[a, NEXT_BAND] or
                   G0[a, NEXT_BAND, columns].any()) and a not in NEW_ROWS]
    require(not outside,
            "band-26 source has an undeclared output component: %r" % outside)

    finite_difference = []
    for j, label in enumerate(NEW_COORDS):
        unit = [0] * len(NEW_COORDS)
        unit[j] = 1
        E1 = build_E(set_new_vector(point, unit, p), p, Z)
        delta = ((E1.V.astype(np.int64) % p) - V0) % p
        expected = G0[:, :, columns[j]] % p
        exact = bool(np.array_equal(delta[:, :NEXT_BAND + 1],
                                    expected[:, :NEXT_BAND + 1]))
        lower_unchanged = bool(not delta[:, :NEXT_BAND].any())
        require(exact and lower_unchanged,
                "finite-difference projection gate failed at %r" % (label,))
        finite_difference.append({
            "coordinate": [label[0], label[1], 32 + label[1]],
            "lower_rows_unchanged": lower_unchanged,
            "band26_equals_source_derivative": exact,
            "band26_support_eta": [a for a in range(V2.HMAX)
                                    if delta[a, NEXT_BAND]],
        })
    mixed = [i + 1 for i in range(len(NEW_COORDS))]
    Em = build_E(set_new_vector(point, mixed, p), p, Z)
    delta_m = ((Em.V.astype(np.int64) % p) - V0) % p
    expected_m = np.zeros_like(delta_m)
    for value, c in zip(mixed, columns):
        expected_m += value * G0[:, :, c]
    expected_m %= p
    affine_gate = bool(np.array_equal(
        delta_m[:, :NEXT_BAND + 1], expected_m[:, :NEXT_BAND + 1]))
    require(affine_gate, "joint band-26 dependence is not affine")

    A = [[int(G0[a, NEXT_BAND, c]) for c in columns]
         for a in NEW_ROWS]
    rhs = [(-int(V0[a, NEXT_BAND])) % p for a in NEW_ROWS]
    R, pivots, pivot_rows = rref(A, p)
    rk = len(pivots)
    rank_aug = rank([row + [bb] for row, bb in zip(A, rhs)], p)
    kbasis, _p, free = kernel_basis(A, p)
    left, _lp, _lf = kernel_basis(transpose(A), p)
    pairings = [sum(lam[i] * rhs[i] for i in range(len(rhs))) % p
                for lam in left]
    particular = solve(A, rhs, p)
    require((particular is not None) == (rk == rank_aug),
            "rank and solve consistency tests disagree")
    require(all(not any(matvec(A, v, p)) for v in kbasis),
            "right-kernel replay failed")
    require(all(not any(matvec(transpose(A), v, p)) for v in left),
            "left-kernel replay failed")
    minor = [[A[i][j] for j in pivots] for i in pivot_rows]
    minor_det = determinant(minor, p)
    require(bool(minor_det) == bool(rk),
            "canonical rank minor failed")

    lifts = []
    if particular is not None:
        for i, direction in enumerate(kbasis):
            vector = [(x + y) % p for x, y in zip(particular, direction)]
            El = build_E(set_new_vector(point, vector, p), p, Z)
            Vl = El.V.astype(np.int64) % p
            zeros = bool(not Vl[:, :NEXT_BAND + 1].any())
            require(zeros, "actual next-band kernel lift failed to replay")
            lifts.append({
                "free_direction": i,
                "new_coordinate_vector": vector,
                "all_residuals_through_band26_zero": zeros,
                "residual_array_sha256": json_hash(
                    Vl[:, :NEXT_BAND + 1].tolist()),
            })

    meta.update({
        "projection_gates": {
            "D25_residual_bands_le24_zero": True,
            "new_columns_zero_below_band26": True,
            "first_occurrence_band26_exactly_declared_ten": True,
            "band26_output_census_exact": True,
            "dual_vs_independent_product_rule": True,
            "ten_unit_finite_differences": finite_difference,
            "mixed_vector_affine_replay": affine_gate,
        },
        "relative_block": {
            "row_eta_labels": NEW_ROWS,
            "column_labels": [[f, r, 32 + r] for f, r in NEW_COORDS],
            "A": A,
            "rhs_minus_residual": rhs,
            "rank_A": rk,
            "rank_augmented": rank_aug,
            "kernel_dimension": len(kbasis),
            "cokernel_dimension": len(left),
            "pivot_row_indices": pivot_rows,
            "pivot_eta_labels": [NEW_ROWS[i] for i in pivot_rows],
            "pivot_column_indices": pivots,
            "pivot_column_labels": [[NEW_COORDS[j][0], NEW_COORDS[j][1],
                                      32 + NEW_COORDS[j][1]]
                                     for j in pivots],
            "canonical_minor_determinant_mod_p": minor_det,
            "right_kernel_free_columns": free,
            "right_kernel_basis": kbasis,
            "left_kernel_basis": left,
            "left_cokernel_obstruction_pairings": pairings,
            "compatible": particular is not None,
            "canonical_particular_solution": particular,
            "actual_lifts_one_per_free_direction": lifts,
            "block_sha256": json_hash({"A": A, "rhs": rhs}),
        },
    })
    return meta


def projection_record():
    return {
        "name": "pi_27_25",
        "direction": "X27 -> X25",
        "source_equation": (
            "E=(theta(Phi)-12Phi)Gamma_eta-"
            "Phi_eta(theta(Gamma)-18Gamma)+42*t^20"),
        "source_constructor": (
            "unreduced cyclic orbit products valuation_e2.build_jets; "
            "no row reduction, Schur complement, D43 source, or D43 claim"),
        "X25_equations": "all pristine residual coefficients at bands <=24",
        "X27_new_equations": ["Row_26[eta^%d]" % a for a in NEW_ROWS],
        "forgotten_coordinates": [
            {"family": f, "source_r": r, "absolute_root_tail_level": 32 + r,
             "name": "%s_%d" % (f, 32 + r)} for f, r in NEW_COORDS],
        "projection_rule": (
            "retain every D25 cell/reconstruction/frontier coordinate and "
            "forget only the ten displayed first-occurrence coordinates"),
        "typing_test": (
            "the ten new source columns vanish on every lower row and "
            "direct finite-difference rebuilds leave X25 byte-identical"),
    }


def decide(results):
    # This is deliberately a signal-level decision.  A positive-dimensional
    # actual relative fiber suffices for FREE-TAIL-SIGNAL, even if other
    # sampled base points are outside the projection image.
    compatible = [r for r in results
                  if r["relative_block"]["compatible"]]
    if (compatible and
            all(r["relative_block"]["kernel_dimension"] > 0
                for r in compatible) and
            all(len(r["relative_block"]
                        ["actual_lifts_one_per_free_direction"]) ==
                r["relative_block"]["kernel_dimension"]
                for r in compatible)):
        return "FREE-TAIL-SIGNAL"
    if (results and
            all(r["relative_block"]["rank_A"] == len(NEW_COORDS)
                for r in results)):
        return "FINITE-TYPE-SIGNAL"
    return "INCONCLUSIVE"


def run(out_path):
    manifest = source_manifest()
    projection = projection_record()
    try:
        results = [audit_sample(p, kind) for p in PRIMES
                   for kind in ("witness", "interior-sequence")]
        verdict = decide(results)
        defect = None
    except TypedMapError as e:
        results = []
        verdict = "NO-TYPED-MAP"
        defect = str(e)
    out = {
        "tool": TOOL,
        "status": "INTERNAL / PRODUCER-CHECKED / MOD-p SIGNAL ONLY",
        "verdict": verdict,
        "type_or_provenance_defect": defect,
        "scope": (
            "mod p only at 105337 and 105673; residue-A, B-frozen, "
            "no-log, PIN42, W1*W2!=0 a00pp chart; four named points on "
            "promoted D25 cells; one new band only"),
        "perimeter": (
            "Relative first-order ranks and pointwise affine lifts are "
            "not component statements, do not decide the projection image, "
            "and do not imply persistence or existence of an inverse limit."),
        "projection": projection,
        "projection_sha256": json_hash(projection),
        "source_manifest": manifest,
        "source_manifest_sha256": json_hash(manifest),
        "samples": results,
        "summary": {
            "n_samples": len(results),
            "samples_per_prime": {str(p): sum(r["prime"] == p
                                              for r in results)
                                  for p in PRIMES},
            "rank_A_distribution": {
                str(k): sum(r["relative_block"]["rank_A"] == k
                            for r in results)
                for k in sorted({r["relative_block"]["rank_A"]
                                 for r in results})},
            "rank_augmented_distribution": {
                str(k): sum(r["relative_block"]["rank_augmented"] == k
                            for r in results)
                for k in sorted({r["relative_block"]["rank_augmented"]
                                 for r in results})},
            "compatible_samples": sum(
                r["relative_block"]["compatible"] for r in results),
            "incompatible_samples": sum(
                not r["relative_block"]["compatible"] for r in results),
            "actual_lifts_replayed": sum(
                len(r["relative_block"]
                    ["actual_lifts_one_per_free_direction"])
                for r in results),
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps(out["summary"], sort_keys=True))
    print("VERDICT:", verdict)
    print("WROTE:", out_path)
    return out


def selftest():
    p = 101
    A = [[1, 2, 3], [2, 4, 6]]
    kb, piv, free = kernel_basis(A, p)
    require(len(piv) == 1 and len(free) == 2 and
            all(not any(matvec(A, v, p)) for v in kb),
            "kernel selftest failed")
    left, _, _ = kernel_basis(transpose(A), p)
    require(len(left) == 1 and
            all(not any(matvec(transpose(A), v, p)) for v in left),
            "cokernel selftest failed")
    require(solve(A, [1, 2], p) is not None and
            solve(A, [1, 3], p) is None,
            "solve selftest failed")
    require(len(NEW_COORDS) == 10 and len(set(NEW_COORDS)) == 10 and
            NEW_ROWS == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
            "X27 registry selftest failed")
    print("PASS selftest: modular RREF/kernel/cokernel/solve and exact "
          "10x10 X27 registry")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--out", default=os.path.join(HERE, "samples.json"))
    args = ap.parse_args()
    if args.selftest:
        selftest()
    if args.run:
        run(args.out)
    if not args.selftest and not args.run:
        ap.print_help()


if __name__ == "__main__":
    main()
