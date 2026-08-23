#!/usr/bin/env python3
"""Exact toric/Macaulay pilots for the pinned D21 direction-b window.

The default ``pilot`` phase performs the complete degree-one Macaulay
closure at (h1,h2,w1,w2)=(+,+,1,1).  It proves the reported rank on at
least one characteristic-zero factor of E by a deterministic good-prime
minor and twelve exact E-syzygies.  ``internal`` is the cheaper sub-tier;
``census`` counts occurrence-wide quadratic toric binomials without
materialising them.  No phase mutates the banked state.

Reproduction (from the repository root):

  DIRECTIONB_STATE="$PWD/directionb_tails_D21.pkl" \
    python3 cases/directionb_toric.py pilot

The pilot needs python-flint.  ``internal`` uses only the repository
engine, but is much slower because it eliminates over E directly.
"""
import os
import random
import resource
import sys
import time
from array import array
from collections import Counter, defaultdict
from itertools import combinations_with_replacement

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
os.environ.setdefault("DIRECTIONB_STATE",
                      os.path.join(REPO, "directionb_tails_D21.pkl"))
sys.path.insert(0, HERE)
import directionb_window as W

P = 105337
R3, A1, A2, MU = 795, 50630, 10114, 50267
SEED = 7210821
PIN_NAMES = ("tf1_42", "tf2_42", "tg1_42", "tg2_42",
             "tg01_42", "tg02_42")

# Global row numbers in the 56*(1+68) ordering: first the unshifted
# rows, then blocks x_j*basis_i for active variables j=0,...,67.
SYZYGY_SUPPORTS = (
    (1, 2, 3, 4, 168),
    (5, 6, 7, 8, 9, 169, 170, 171, 172),
    (1, 2, 3, 4, 280),
    (5, 6, 7, 8, 9, 169, 170, 171, 224, 281, 282),
    (5, 6, 7, 8, 9, 169, 170, 171, 224, 281, 283),
    (5, 6, 7, 8, 9, 169, 170, 171, 224, 281, 284),
    (5, 6, 7, 8, 9, 169, 170, 171, 224, 281, 336),
    (10, 11, 12, 13, 14, 15, 16, 173, 174, 175, 176, 177,
     225, 226, 227, 228, 285, 286, 287, 288, 289, 337, 338, 339),
    (10, 11, 12, 13, 14, 15, 16, 173, 174, 175, 176, 177,
     225, 226, 227, 228, 285, 286, 287, 288, 289, 337, 338, 340),
    (393, 394, 395, 396, 504, 1065, 1066, 1067, 1068,
     1737, 1738, 1739, 1740, 1848, 2409, 2410, 2411, 2412,
     3081, 3082, 3083, 3084, 3136, 3473, 3474, 3475, 3476),
    (393, 394, 395, 396, 504, 1065, 1066, 1067, 1176,
     1737, 1738, 1739, 1740, 1848, 2409, 2410, 2411, 2520,
     3081, 3082, 3083, 3084, 3136, 3473, 3474, 3475, 3528),
    (428, 896, 1100, 1568, 1772, 2240, 2444, 2912, 3116,
     3304, 3508, 3696),
)


def qmod(q):
    return (q.numerator % P) * pow(q.denominator, -1, P) % P


def emod(c):
    """The certified E -> F_105337 component homomorphism."""
    return sum((qmod(k[0]) + qmod(k[1]) * R3)
               * pow(A1, i, P) * pow(A2, j, P) * pow(MU, e, P)
               for (i, j, e), k in c.items()) % P


def build():
    """Hard-substitute the six pins and return 76 affine E-polynomials."""
    byk, names, depth = W.load()
    assert depth == 21, "this script is deliberately the D21 pilot"
    pins = {names.index(x) for x in PIN_NAMES}
    polys, labels = [], []
    for k in sorted(byk):
        for n, value in sorted(byk[k].items()):
            poly = {}
            for mon, ring_coeff in value.items():
                if pins.intersection(mon):
                    continue
                coeff = W.ring_to_E(ring_coeff, 1, 1, W.K1, W.K1)
                if coeff:
                    poly[mon] = W.eadd(poly.get(mon, {}), coeff)
                    if not poly[mon]:
                        del poly[mon]
            if k == 20 and n == 0:
                poly[()] = W.eadd(poly.get((), {}),
                                  {(0, 0, 0): W.RHS42})
            if poly:
                polys.append(poly)
                labels.append((k, n))
    active = sorted({v for poly in polys for mon in poly for v in mon})
    mons = {mon for poly in polys for mon in poly}
    full_nnz = sum(map(len, polys))
    nonconst_nnz = sum(sum(bool(mon) for mon in poly) for poly in polys)
    scalar_nnz = sum(() in poly for poly in polys)
    assert labels.count((10, 28)) == 0
    assert (len(polys), len(mons) - 1, len(active)) == (76, 4351, 68)
    assert (nonconst_nnz, scalar_nnz, full_nnz) == (36519, 9, 36528)
    return names, polys, labels, active


def choose_basis(polys):
    """A nonzero F_p minor selects 56 independent original rows."""
    pivots, basis = {}, []
    for ri, poly in enumerate(polys):
        row = {m: emod(c) for m, c in poly.items() if emod(c)}
        while row:
            col = min(row, key=lambda m: (len(m), m))
            if col not in pivots:
                inv = pow(row[col], -1, P)
                pivots[col] = {m: x * inv % P for m, x in row.items()}
                basis.append(ri)
                break
            factor = row[col]
            for m, x in pivots[col].items():
                z = (row.get(m, 0) - factor * x) % P
                if z:
                    row[m] = z
                else:
                    row.pop(m, None)
    assert len(basis) == 56
    return basis


def exact_global_row(z, polys, basis, active):
    """Coefficient row; omit the unshifted constant (the affine RHS)."""
    if z < 56:
        return {m: c for m, c in polys[basis[z]].items() if m}
    j, i = divmod(z - 56, 56)
    v = active[j]
    return {tuple(sorted(m + (v,))): c
            for m, c in polys[basis[i]].items()}


def modular_pivot_columns(rows):
    pivots, cols = {}, []
    for exact_row in rows:
        row = {m: emod(c) for m, c in exact_row.items() if emod(c)}
        while row:
            col = min(row, key=lambda m: (len(m), m))
            if col not in pivots:
                inv = pow(row[col], -1, P)
                pivots[col] = {m: x * inv % P for m, x in row.items()}
                cols.append(col)
                break
            factor = row[col]
            for m, x in pivots[col].items():
                z = (row.get(m, 0) - factor * x) % P
                if z:
                    row[m] = z
                else:
                    row.pop(m, None)
        else:
            raise AssertionError("syzygy prefix unexpectedly dependent")
    return cols


def verify_exact_syzygies(polys, basis, active):
    """Lift twelve sparse relations and verify all E coefficients."""
    terminal = []
    t0 = time.time()
    for qi, support in enumerate(SYZYGY_SUPPORTS):
        # Hence a relation among coefficient rows is also a relation among
        # the augmented polynomial rows.  Shifted constants are retained as
        # degree-one monomials by exact_global_row().
        assert all(z >= 56 or () not in polys[basis[z]] for z in support)
        rows = [exact_global_row(z, polys, basis, active) for z in support]
        n = len(rows) - 1
        cols = modular_pivot_columns(rows[:n])
        equations, rhs = [], []
        for mon in cols:
            equations.append({i: rows[i][mon] for i in range(n)
                              if mon in rows[i]})
            rhs.append(W.eneg(rows[-1].get(mon, {})))
        rank, _, solution, free, inconsistent, undecided = W.esolve(
            equations, rhs, n)
        assert rank == n and not free and not inconsistent and not undecided
        factors = [solution[i] for i in range(n)] + [W.EONE]
        residual = {}
        for factor, row in zip(factors, rows):
            for mon, coeff in row.items():
                residual[mon] = W.eadd(residual.get(mon, {}),
                                       W.emul(factor, coeff))
                if not residual[mon]:
                    del residual[mon]
        assert not residual
        terminal.append(support[-1])
        print("PASS exact syzygy %d: support %d, zero residual"
              % (qi + 1, len(support)), flush=True)
    assert len(terminal) == len(set(terminal)) == 12
    assert all(sum(t in support for support in SYZYGY_SUPPORTS) == 1
               for t in terminal)
    print("PASS 12 independent exact E-syzygies (%.2fs)"
          % (time.time() - t0))


def evaluation_ranks(polys, basis, active):
    """Deterministic nonzero 3852-minors after specialization/evaluation."""
    try:
        from flint import nmod_mat
    except ImportError as exc:
        raise SystemExit("pilot requires python-flint: %s" % exc)
    mons = sorted({m for ri in basis for m in polys[ri]},
                  key=lambda m: (len(m), m))
    mon_index = {m: i for i, m in enumerate(mons)}
    terms = [[(mon_index[m], emod(c)) for m, c in polys[ri].items()]
             for ri in basis]
    constants = [emod(polys[ri].get((), {})) for ri in basis]
    n = 56 * 69
    rng = random.Random(SEED)
    fvals = [array('L', [0]) * n for _ in basis]
    xvals = [array('L', [0]) * n for _ in active]
    t0 = time.time()
    for t in range(n):
        xs = [rng.randrange(1, P) for _ in active]
        values = dict(zip(active, xs))
        for j, x in enumerate(xs):
            xvals[j][t] = x
        mon_values = array('L', [0]) * len(mons)
        for h, mon in enumerate(mons):
            value = 1
            for v in mon:
                value = value * values[v] % P
            mon_values[h] = value
        for i, row_terms in enumerate(terms):
            fvals[i][t] = sum(c * mon_values[h]
                              for h, c in row_terms) % P
        if (t + 1) % 1000 == 0:
            print("evaluation %d/%d" % (t + 1, n), flush=True)
    entries = array('L')
    for i in range(56):
        entries.extend((fvals[i][t] - constants[i]) % P
                       for t in range(n))
    for j in range(68):
        for i in range(56):
            entries.extend(xvals[j][t] * fvals[i][t] % P
                           for t in range(n))
    matrix = nmod_mat(n, n, entries, P)
    coefficient_rank = matrix.rank()
    for i, constant in enumerate(constants):
        if constant:
            for t in range(n):
                matrix[i, t] = (int(matrix[i, t]) + constant) % P
    augmented_rank = matrix.rank()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
    print("certificate ranks: coefficient=%d augmented=%d (%.1fs, %.1f MiB)"
          % (coefficient_rank, augmented_rank, time.time() - t0, peak))
    assert (coefficient_rank, augmented_rank) == (3852, 3852)


def pilot():
    assert pow(R3, 2, P) == 3
    assert pow(A1, 3, P) == (3 + R3) % P
    assert pow(A2, 3, P) == (3 - R3) % P
    assert pow(MU, 2, P) == 3 * pow(2, -1, P) % P
    _, polys, _, active = build()
    basis = choose_basis(polys)
    assert sorted({v for ri in basis for m in polys[ri] for v in m}) == active
    basis_full_nnz = sum(len(polys[ri]) for ri in basis)
    basis_const = sum(() in polys[ri] for ri in basis)
    print("base: 76 rows x 4351 nonconstant cols; accepted exact rank 56")
    print("base nnz: 36519 nonconstant + 9 scalar = 36528")
    print("Macaulay-1 raw: %d rows x 241110 nonconstant cols; %d nnz"
          % (76 * 69, 36528 * 69))
    print("Macaulay-1 basis: %d rows; %d full / %d coefficient nnz"
          % (56 * 69, basis_full_nnz * 69,
             basis_full_nnz * 69 - basis_const))
    verify_exact_syzygies(polys, basis, active)
    evaluation_ranks(polys, basis, active)
    print("EXACT on at least one characteristic-zero E-factor:")
    print("  coefficient rank = augmented rank = 3852")
    print("VERDICT: NO-KILL-AT-TIER-1")


def census():
    """Stream the full pair-sum census; memory stays well below 8 GiB."""
    _, polys, _, active = build()
    coordinates = sorted({m for p in polys for m in p})  # includes ()
    fibers = defaultdict(int)
    t0 = time.time()
    for i, a in enumerate(coordinates):
        for b in coordinates[i:]:
            fibers[tuple(sorted(a + b))] += 1
    hist = Counter(fibers.values())
    pairs = len(coordinates) * (len(coordinates) + 1) // 2
    collision_fibers = sum(n for size, n in hist.items() if size > 1)
    star = sum((size - 1) * n for size, n in hist.items())
    all_pairwise = sum(size * (size - 1) // 2 * n
                       for size, n in hist.items())
    nonconstant = set(coordinates) - {()}
    factor_targets = sum(fibers[m] > 1 for m in nonconstant)
    factor_binomials = sum(fibers[m] - 1 for m in nonconstant)
    print("coordinates=%d unordered-pairs=%d sum-fibers=%d"
          % (len(coordinates), pairs, len(fibers)))
    print("collision-fibers=%d star-binomials=%d all-pairwise=%d max-fiber=%d"
          % (collision_fibers, star, all_pairwise, max(hist)))
    assert (len(coordinates), pairs, len(fibers), collision_fibers,
            star, all_pairwise, max(hist)) == (
                4352, 9472128, 1652985, 1363363,
                7819143, 50778314, 63)
    assert (factor_targets, factor_binomials) == (2207, 6783)
    print("factor-to-target sub-tier: %d binomials on %d targets"
          % (factor_binomials, factor_targets))
    print("PASS full occurrence-pair census (%.1fs)" % (time.time() - t0))


def rowcensus():
    """Count the much larger, algebraically arbitrary within-row tier."""
    _, polys, labels, _ = build()
    totals, by_band = Counter(), Counter()
    max_fiber = 0
    t0 = time.time()
    for poly, label in zip(polys, labels):
        # Include z_0 in every support, as required by the affine chart.
        support = sorted(set(poly) | {()})
        fibers = Counter()
        for i, a in enumerate(support):
            for b in support[i:]:
                fibers[tuple(sorted(a + b))] += 1
        pairs = len(support) * (len(support) + 1) // 2
        bins = len(fibers)
        star = pairs - bins
        totals.update({
            "pairs": pairs,
            "bins": bins,
            "collision_fibers": sum(v > 1 for v in fibers.values()),
            "star": star,
            "all_pairwise": sum(v * (v - 1) // 2
                                for v in fibers.values()),
        })
        by_band[label[0]] += star
        max_fiber = max(max_fiber, max(fibers.values()))
    expected = {"pairs": 27075938, "bins": 8556205,
                "collision_fibers": 5755181, "star": 18519733,
                "all_pairwise": 65589065}
    assert dict(totals) == expected and max_fiber == 33
    print("within-row summed census: %s" % dict(totals))
    print("star binomials by band: %s; max fiber=%d"
          % (dict(by_band), max_fiber))
    print("PASS within-row census (%.1fs)" % (time.time() - t0))


def internal():
    """Exact occurrence-closed degree-one sub-tier on the same columns."""
    _, polys, labels, active = build()
    monomials = sorted({m for p in polys for m in p if m})
    index = {m: i for i, m in enumerate(monomials)}
    base_rows, base_rhs = [], []
    for poly in polys:
        base_rows.append({index[m]: c for m, c in poly.items() if m})
        base_rhs.append(W.eneg(poly.get((), {})))
    mset = set(monomials)
    shifted, shifted_rhs = [], []
    by_band = Counter()
    for label, poly in zip(labels, polys):
        terms = {m: c for m, c in poly.items() if m}
        const = poly.get((), {})
        for v in active:
            products = {tuple(sorted(m + (v,))): c
                        for m, c in terms.items()}
            if not set(products).issubset(mset):
                continue
            if const and (v,) not in index:
                continue
            row = {index[m]: c for m, c in products.items()}
            if const:
                col = index[(v,)]
                row[col] = W.eadd(row.get(col, {}), const)
                if not row[col]:
                    del row[col]
            shifted.append(row)
            shifted_rhs.append({})
            by_band[label[0]] += 1
    assert len(shifted) == 944
    print("internal tier: 76+944 rows x 4351 cols; by-band %s"
          % dict(by_band), flush=True)
    out = W.esolve(base_rows + shifted, base_rhs + shifted_rhs,
                   len(monomials))
    rank, _, _, free, inconsistent, undecided = out
    print("rank=56->%d free=%d inconsistent=%s undecided=%d"
          % (rank, len(free), inconsistent, undecided))
    assert (rank, len(free), inconsistent, undecided) == (471, 3880,
                                                          False, 0)
    print("VERDICT: NO-KILL-AT-INTERNAL-TIER")


def projection():
    """Materialize supports, but not the 87-million-entry E matrix."""
    _, polys, _, active = build()
    basis = choose_basis(polys)
    monomials = {m for poly in polys for m in poly}
    columns = set(monomials)
    t0 = time.time()
    for v in active:
        for mon in monomials:
            columns.add(tuple(sorted(mon + (v,))))
    for v, w in combinations_with_replacement(active, 2):
        for mon in monomials:
            columns.add(tuple(sorted(mon + (v, w))))
    multipliers = 1 + len(active) + len(active) * (len(active) + 1) // 2
    basis_full_nnz = sum(len(polys[ri]) for ri in basis)
    raw_rows, basis_rows = 76 * multipliers, 56 * multipliers
    basis_nnz = basis_full_nnz * multipliers
    assert (multipliers, raw_rows, basis_rows, len(columns), basis_nnz) == (
        2415, 183540, 135240, 6939164, 87058335)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
    print("Macaulay-2 support census (%.1fs, %.1f MiB):"
          % (time.time() - t0, peak))
    print("  multipliers degree<=2: %d" % multipliers)
    print("  reduced-basis rows: %d (raw %d)" % (basis_rows, raw_rows))
    print("  columns including constant: %d" % len(columns))
    print("  formal reduced-basis nnz: %d" % basis_nnz)
    print("  current exact sparse-E materialization exceeds the 8 GiB cap")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "pilot"
    phases = {"pilot": pilot, "census": census, "rowcensus": rowcensus,
              "internal": internal, "projection": projection}
    if phase not in phases:
        raise SystemExit("usage: %s [%s]" %
                         (sys.argv[0], "|".join(sorted(phases))))
    phases[phase]()
