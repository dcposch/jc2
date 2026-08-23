#!/usr/bin/env python3
"""D43 NF/certificate route on the 52+34 parked-fiber verdict system.

INTERNAL / UNREVIEWED.  This tool deliberately never invokes msolve on the
full D43 verdict file.  It uses the verified D25 parked-cell triangular
structure to form exact normal forms of the 52 D43 compatibility rows.

The first gate, ``--selftest``, independently rebuilds the triangular map on
each of the 16 components of the a00pp parked fiber and checks all 34 pristine
rows as polynomial identities in the fourteen free cell coordinates.
"""

import argparse
import hashlib
import itertools
import json
import os
import pickle
import random
import sys


PRIMES = (105337, 105673)
FREE_BASE = ("x57", "x59", "x60", "x62", "x63", "x65", "x66", "x68",
             "x72", "x73")
FREE_LIFT = ("x16", "x19", "x24", "x27")
FREE = FREE_BASE + FREE_LIFT
DEP_BASE = ("x70", "x53", "x58", "x55", "x71", "x52", "x47", "x54")
DEP_LIFT = ("x33", "x38")
DEP = DEP_BASE + DEP_LIFT
FIXED = ("W1", "W2", "uW1", "uW2")


def parse_ms(path):
    """Strict parser for the campaign's expanded, plus-only .ms format."""
    with open(path) as fh:
        lines = fh.read().splitlines()
    names = tuple(x.strip() for x in lines[0].split(","))
    p = int(lines[1])
    body = "\n".join(lines[2:])
    rows_text = [x.strip().rstrip(",") for x in body.split(",\n") if x.strip()]
    pos = {x: i for i, x in enumerate(names)}
    rows = []
    for text in rows_text:
        poly = {}
        for term in text.split("+"):
            factors = term.strip().split("*")
            try:
                coeff = int(factors[0]) % p
                factors = factors[1:]
            except ValueError:
                coeff = 1
            exps = [0] * len(names)
            for factor in factors:
                if "^" in factor:
                    name, power = factor.split("^", 1)
                    power = int(power)
                else:
                    name, power = factor, 1
                if name not in pos:
                    raise ValueError("unknown variable %r in %s" % (name, path))
                exps[pos[name]] += power
            key = tuple(exps)
            poly[key] = (poly.get(key, 0) + coeff) % p
            if not poly[key]:
                del poly[key]
        rows.append(poly)
    return names, p, rows


def poly_add_scaled(dst, src, scale, p):
    scale %= p
    if not scale:
        return dst
    for mono, coeff in src.items():
        value = (dst.get(mono, 0) + scale * coeff) % p
        if value:
            dst[mono] = value
        else:
            dst.pop(mono, None)
    return dst


def poly_mul(a, b, p):
    if not a or not b:
        return {}
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mono = tuple(x + y for x, y in zip(ma, mb))
            value = (out.get(mono, 0) + ca * cb) % p
            if value:
                out[mono] = value
            else:
                out.pop(mono, None)
    return out


def poly_pow(poly, power, p, nvars):
    out = {(0,) * nvars: 1}
    base = poly
    while power:
        if power & 1:
            out = poly_mul(out, base, p)
        power >>= 1
        if power:
            base = poly_mul(base, base, p)
    return out


def substitute(poly, var_index, replacement, p):
    """Substitute one variable by ``replacement`` in the same sparse ring."""
    if not poly:
        return {}
    nvars = len(next(iter(poly)))
    powers = {0: {(0,) * nvars: 1}, 1: replacement}
    out = {}
    for mono, coeff in poly.items():
        power = mono[var_index]
        if power not in powers:
            powers[power] = poly_pow(replacement, power, p, nvars)
        rest = list(mono)
        rest[var_index] = 0
        rest = tuple(rest)
        shifted = {tuple(x + y for x, y in zip(rest, mr)): cr
                   for mr, cr in powers[power].items()}
        poly_add_scaled(out, shifted, coeff, p)
    return out


def rref_left_kernel(matrix, p):
    """Return a canonical basis of the left kernel of a numeric matrix."""
    nr = len(matrix)
    nc = len(matrix[0]) if nr else 0
    aug = [list(row) + [1 if i == j else 0 for j in range(nr)]
           for i, row in enumerate(matrix)]
    rank = 0
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if aug[i][col] % p), None)
        if pivot is None:
            continue
        aug[rank], aug[pivot] = aug[pivot], aug[rank]
        inv = pow(aug[rank][col] % p, p - 2, p)
        aug[rank] = [x * inv % p for x in aug[rank]]
        for i in range(nr):
            if i != rank and aug[i][col] % p:
                scale = aug[i][col] % p
                aug[i] = [(x - scale * y) % p
                          for x, y in zip(aug[i], aug[rank])]
        rank += 1
    return [row[nc:] for row in aug[rank:]], rank


def fourth_roots(p, value, hint):
    assert pow(hint, 4, p) == value % p
    root4 = None
    candidate = 2
    while root4 is None:
        z = pow(candidate, (p - 1) // 4, p)
        if z != 1 and pow(z, 2, p) == p - 1:
            root4 = z
        candidate += 1
    roots = sorted({hint * pow(root4, j, p) % p for j in range(4)})
    assert len(roots) == 4
    assert all(pow(x, 4, p) == value % p for x in roots)
    return roots


def specialize_fixed(rows, names, fixed, p):
    """Substitute W/uW constants but retain the original exponent width."""
    pos = {x: i for i, x in enumerate(names)}
    out = []
    for poly in rows:
        result = {}
        for mono, coeff in poly.items():
            key = list(mono)
            value = coeff
            for name, scalar in fixed.items():
                i = pos[name]
                value = value * pow(scalar, key[i], p) % p
                key[i] = 0
            key = tuple(key)
            result[key] = (result.get(key, 0) + value) % p
            if not result[key]:
                del result[key]
        out.append(result)
    return out


def numeric_linear_coeff(poly, index, p):
    """Coefficient of a variable known to occur as a bare linear term."""
    value = 0
    for mono, coeff in poly.items():
        if mono[index]:
            assert mono[index] == 1
            assert sum(mono) == 1, (index, mono)
            value = (value + coeff) % p
    return value


def only_unknowns(poly, positions):
    return {i for i in positions if any(mono[i] for mono in poly)}


def solve_single(poly, index, p):
    """Solve a constant-unit affine pivot row for one variable."""
    coeff = 0
    const = {}
    for mono, value in poly.items():
        power = mono[index]
        if power:
            assert power == 1
            rest = list(mono)
            rest[index] = 0
            assert not any(rest), (index, mono, "nonconstant pivot")
            coeff = (coeff + value) % p
        else:
            const[mono] = value
    assert coeff
    scale = -pow(coeff, p - 2, p)
    return {mono: value * scale % p for mono, value in const.items()}


def split_constant_affine(poly, indices, p):
    """Split a row as sum(coeff[j]*x_j)+const with scalar coeffs."""
    coeffs = [0] * len(indices)
    const = {}
    iset = set(indices)
    for mono, value in poly.items():
        hit = [j for j, index in enumerate(indices) if mono[index]]
        if not hit:
            const[mono] = value
            continue
        if len(hit) != 1 or mono[indices[hit[0]]] != 1 or sum(mono) != 1:
            return None
        coeffs[hit[0]] = (coeffs[hit[0]] + value) % p
    return coeffs, const


def build_cell_map(parked_path, replay_path, W1, W2):
    """Rebuild one A^14 component's ten triangular substitutions."""
    names, p, raw_rows = parse_ms(parked_path)
    assert len(raw_rows) == 34
    assert set(names) == set(FREE + DEP + FIXED)
    pos = {x: i for i, x in enumerate(names)}
    fixed = {"W1": W1 % p, "W2": W2 % p,
             "uW1": pow(W1, p - 2, p), "uW2": pow(W2, p - 2, p)}
    rows = specialize_fixed(raw_rows, names, fixed, p)

    # The last five pristine rows are affine in the two lift pivots.
    residual = rows[29:34]
    lift_matrix = [[numeric_linear_coeff(row, pos[x], p)
                    for x in DEP_LIFT] for row in residual]
    left_kernel, rank = rref_left_kernel(lift_matrix, p)
    assert rank == 2 and len(left_kernel) == 3
    compat = []
    for vector in left_kernel:
        row = {}
        for scale, source in zip(vector, residual):
            poly_add_scaled(row, source, scale, p)
        assert not only_unknowns(row, (pos["x33"], pos["x38"]))
        compat.append(row)

    work = list(rows) + compat
    unknown = {pos[x] for x in DEP}
    maps = {}
    transcript = []

    # Unit-linear single pivots solve the eight base variables.  The order is
    # discovered from the pristine rows plus exact Schur compatibilities.
    while len(unknown) > 2:
        choice = None
        for ri, row in enumerate(work):
            live = only_unknowns(row, unknown)
            if len(live) != 1:
                continue
            index = next(iter(live))
            try:
                replacement = solve_single(row, index, p)
            except AssertionError:
                continue
            choice = ri, index, replacement
            break
        if choice is not None:
            ri, index, replacement = choice
            maps[names[index]] = replacement
            transcript.append({"var": names[index], "row": ri,
                               "terms": len(replacement)})
            work = [substitute(row, index, replacement, p) for row in work]
            unknown.remove(index)
            continue

        # The sparse parked presentation has one genuine 2x2 base pivot
        # (x47,x52 on the current a00pp files).  Accept it only when both
        # rows are scalar-affine in exactly the selected pair.
        base_unknown = [i for i in unknown if names[i] in DEP_BASE]
        pair_choice = None
        for ia, ib in itertools.combinations(base_unknown, 2):
            candidates = []
            for ri, row in enumerate(work):
                if not only_unknowns(row, unknown) <= {ia, ib}:
                    continue
                split = split_constant_affine(row, (ia, ib), p)
                if split is not None and any(split[0]):
                    candidates.append((ri, split[0], split[1]))
            for left, right in itertools.combinations(candidates, 2):
                a, b = left[1]
                d, e = right[1]
                det = (a * e - b * d) % p
                if det:
                    pair_choice = ia, ib, left, right, det
                    break
            if pair_choice:
                break
        assert pair_choice is not None, ("triangular base pass stuck",
                                         [names[i] for i in sorted(unknown)],
                                         transcript)
        ia, ib, left, right, det = pair_choice
        invdet = pow(det, p - 2, p)
        a, b = left[1]
        d, e = right[1]
        sola, solb = {}, {}
        poly_add_scaled(sola, right[2], b * invdet, p)
        poly_add_scaled(sola, left[2], -e * invdet, p)
        poly_add_scaled(solb, left[2], d * invdet, p)
        poly_add_scaled(solb, right[2], -a * invdet, p)
        maps[names[ia]], maps[names[ib]] = sola, solb
        transcript.extend([
            {"var": names[ia], "rows": [left[0], right[0]],
             "terms": len(sola)},
            {"var": names[ib], "rows": [left[0], right[0]],
             "terms": len(solb)}])
        work = [substitute(row, ia, sola, p) for row in work]
        work = [substitute(row, ib, solb, p) for row in work]
        unknown.remove(ia)
        unknown.remove(ib)

    assert {names[i] for i in unknown} == set(DEP_LIFT)
    ia, ib = pos["x33"], pos["x38"]
    affine = []
    for ri, row in enumerate(work[:34]):
        a = numeric_linear_coeff(row, ia, p)
        b = numeric_linear_coeff(row, ib, p)
        if a or b:
            const = {m: c for m, c in row.items() if not m[ia] and not m[ib]}
            affine.append((ri, a, b, const))
    pair = None
    for left, right in itertools.combinations(affine, 2):
        det = (left[1] * right[2] - left[2] * right[1]) % p
        if det:
            pair = left, right, det
            break
    assert pair is not None
    left, right, det = pair
    invdet = pow(det, p - 2, p)
    # a*x33+b*x38+r = d*x33+e*x38+s = 0
    sol33 = {}
    poly_add_scaled(sol33, right[3], left[2] * invdet, p)
    poly_add_scaled(sol33, left[3], -right[2] * invdet, p)
    sol38 = {}
    poly_add_scaled(sol38, left[3], right[1] * invdet, p)
    poly_add_scaled(sol38, right[3], -left[1] * invdet, p)
    maps["x33"] = sol33
    maps["x38"] = sol38
    transcript.extend([{"var": "x33", "rows": [left[0], right[0]],
                        "terms": len(sol33)},
                       {"var": "x38", "rows": [left[0], right[0]],
                        "terms": len(sol38)}])
    work = [substitute(row, ia, sol33, p) for row in work]
    work = [substitute(row, ib, sol38, p) for row in work]

    # Fixed W roots put us on one factor of the certified product; all 34
    # pristine generators must vanish identically in F_p[free_14].
    failures = [(i, len(row)) for i, row in enumerate(work[:34]) if row]
    assert not failures, failures

    # Convert maps from the original 28-wide ring to the canonical free ring.
    free_pos = {name: i for i, name in enumerate(FREE)}
    compact = {}
    for name, poly in maps.items():
        result = {}
        for mono, coeff in poly.items():
            assert not any(mono[pos[x]] for x in DEP + FIXED)
            exps = [0] * len(FREE)
            for free_name, j in free_pos.items():
                exps[j] = mono[pos[free_name]]
            key = tuple(exps)
            result[key] = (result.get(key, 0) + coeff) % p
            if not result[key]:
                del result[key]
        compact[name] = result

    replay = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    assert pow(W1, 4, p) == int(replay["W1^4"])
    assert pow(W2, 4, p) == int(replay["W2^4"])
    return {"prime": p, "W1": W1, "W2": W2, "fixed": fixed,
            "maps": compact, "transcript": transcript,
            "lift_matrix": lift_matrix, "left_kernel": left_kernel,
            "raw_names": names}


def eval_free_poly(poly, values, p):
    total = 0
    for mono, coeff in poly.items():
        term = coeff
        for value, power in zip(values, mono):
            term = term * pow(value, power, p) % p
        total = (total + term) % p
    return total


def eval_named_poly(poly, names, values, p):
    total = 0
    for mono, coeff in poly.items():
        term = coeff
        for name, power in zip(names, mono):
            if power:
                term = term * pow(values[name], power, p) % p
        total = (total + term) % p
    return total


def matrix_rank(matrix, p):
    if not matrix:
        return 0
    work = [list(map(lambda x: x % p, row)) for row in matrix]
    nr, nc = len(work), len(work[0])
    rank = 0
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], p - 2, p)
        work[rank] = [x * inv % p for x in work[rank]]
        for i in range(nr):
            if i != rank and work[i][col]:
                scale = work[i][col]
                work[i] = [(x - scale * y) % p
                           for x, y in zip(work[i], work[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def deep_level(name, x2tail):
    semantic = x2tail.get(name, name)
    if semantic in ("Xf_alpha", "Xg_beta"):
        return 42
    if "_" not in semantic:
        return None
    suffix = semantic.rsplit("_", 1)[1]
    return int(suffix) if suffix.isdigit() else None


def eval_external(poly, assignment, p):
    total = 0
    for mono, coeff in poly.items():
        value = coeff
        for name in mono:
            value = value * assignment[name] % p
        total = (total + value) % p
    return total


def affine_numeric(rows, selected, lower_assignment, p):
    """Evaluate lower variables and split rows as A*selected+b."""
    selected = tuple(sorted(selected))
    col = {name: i for i, name in enumerate(selected)}
    A = [[0] * len(selected) for _ in rows]
    b = [0] * len(rows)
    for ri, row in enumerate(rows):
        for mono, coeff in row.items():
            hits = [name for name in mono if name in col]
            if len(hits) > 1:
                return None
            value = coeff
            skipped = False
            for name in mono:
                if name in col:
                    if skipped:
                        return None
                    skipped = True
                else:
                    value = value * lower_assignment[name] % p
            if hits:
                A[ri][col[hits[0]]] = (A[ri][col[hits[0]]] + value) % p
            else:
                b[ri] = (b[ri] + value) % p
    return A, b


def affine_split_rows(rows, selected):
    """Exact split rows = A(selected)+b over the lower-variable ring."""
    selected = tuple(sorted(selected))
    selected_set = set(selected)
    columns = {name: [{} for _ in rows] for name in selected}
    constants = [{} for _ in rows]
    for ri, row in enumerate(rows):
        for mono, coeff in row.items():
            hits = [name for name in mono if name in selected_set]
            assert len(hits) <= 1, (ri, mono, hits)
            if not hits:
                constants[ri][mono] = coeff
                continue
            name = hits[0]
            rest = list(mono)
            rest.remove(name)
            rest = tuple(rest)
            target = columns[name][ri]
            target[rest] = coeff
    return selected, columns, constants


def cdiag_factor(columns, p):
    """Test every polynomial column as C_col times one scalar polynomial."""
    Ccols = []
    factors = []
    for name in sorted(columns):
        column = columns[name]
        first = next((i for i, value in enumerate(column) if value), None)
        assert first is not None, ("zero affine column", name)
        scales = []
        for value in column:
            scale = proportional_dict(column[first], value, p)
            if scale is None:
                return None, {"variable": name, "row": len(scales),
                              "reason": "not scalar-proportional"}
            scales.append(scale)
        Ccols.append(scales)
        factors.append(column[first])
    C = [[Ccols[j][i] for j in range(len(Ccols))]
         for i in range(len(Ccols[0]))]
    return (C, factors), None


def emit_external_ms(path, variables, rows, p):
    """Emit a small expanded .ms system from tuple-of-name monomials."""
    with open(path, "w") as fh:
        fh.write(", ".join(variables) + "\n%d\n" % p)
        lines = []
        for row in rows:
            terms = []
            for mono, coeff in sorted(row.items(), key=lambda x: (len(x[0]), x[0])):
                powers = []
                for name, group in itertools.groupby(mono):
                    power = sum(1 for _ in group)
                    powers.append(name if power == 1 else "%s^%d" % (name, power))
                terms.append(str(coeff) + ("*" + "*".join(powers) if powers else ""))
            lines.append("+".join(terms) if terms else "0")
        fh.write(",\n".join(lines) + "\n")


def split_affine_groups(groups, selected):
    """Grouped checkpoint analogue of d43_family2.split_affine."""
    selected = set(selected)
    coeffs = {name: {} for name in selected}
    for deep, basepoly in groups.items():
        hits = [name for name in deep if name in selected]
        if not hits:
            continue
        assert len(hits) == 1 and deep.count(hits[0]) == 1, \
            ("nonaffine rung occurrence", hits, deep)
        name = hits[0]
        rest = list(deep)
        rest.remove(name)
        rest = tuple(rest)
        target = coeffs[name]
        for pk, coeff in basepoly.items():
            key = (pk, rest)
            target[key] = coeff
    return coeffs


def proportional_dict(left, right, p):
    if not right:
        return 0
    if not left or set(left) != set(right):
        return None
    key = next(iter(left))
    scale = right[key] * pow(left[key], p - 2, p) % p
    if any(right[k] != value * scale % p for k, value in left.items()):
        return None
    return scale


def rung_kernel(group_rows, k, p):
    """Recompute the exact constant C and left kernel for one rung."""
    import d43_family2 as F
    import d25_reduce as DR
    hs = F.rung_rows_idx(k)
    ynames = F.rung_tails(k) + (["Xf_alpha", "Xg_beta"] if k == 42 else [])
    rows = []
    zero_pk = DR.pack([0] * DR.NV)
    SM = pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p
    GM = (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p
    for h in hs:
        groups = {deep: dict(base) for deep, base in group_rows.get(h, {}).items()}
        if k == 42 and h in F.P4P1:
            base = 42 * SM * GM % p * (F.P4P1[h] % p) % p
            groups[("Xf_alpha",)] = {zero_pk: 3 * base % p}
            groups[("Xg_beta",)] = {zero_pk: -2 * base % p}
        rows.append(groups)
    matrices = [split_affine_groups(row, ynames) for row in rows]
    columns = []
    for name in ynames:
        column = [matrix[name] for matrix in matrices]
        first = next((i for i, value in enumerate(column) if value), None)
        if first is None:
            columns.append([0] * len(rows))
            continue
        scales = []
        for value in column:
            scale = proportional_dict(column[first], value, p)
            assert scale is not None, ("C-diag failure", k, name)
            scales.append(scale)
        columns.append(scales)
    C = [[columns[j][i] for j in range(len(columns))]
         for i in range(len(rows))]
    L, rank = rref_left_kernel(C, p)
    return hs, ynames, rows, C, L, rank


def eval_group_row(groups, base_values, cell_values, p, t2x, unpack):
    """Specialize one checkpoint row to a D25 cell point exactly."""
    base_cache = {}
    out = {}
    for deep, basepoly in groups.items():
        base_value = 0
        for pk, coeff in basepoly.items():
            if pk not in base_cache:
                value = 1
                for name, power in zip(base_values, unpack(pk)):
                    if power:
                        value = value * pow(name, power, p) % p
                base_cache[pk] = value
            base_value = (base_value + coeff * base_cache[pk]) % p
        if not base_value or "uf30" in deep:
            continue
        external = []
        value = base_value
        for semantic in deep:
            name = t2x.get(semantic, semantic)
            if name in cell_values:
                value = value * cell_values[name] % p
            else:
                external.append(name)
        key = tuple(sorted(external))
        out[key] = (out.get(key, 0) + value) % p
        if not out[key]:
            del out[key]
    return out


def monomial_times(poly, mono, coeff, p):
    out = {}
    for key, value in poly.items():
        shifted = tuple(x + y for x, y in zip(key, mono))
        scalar = value * coeff % p
        if scalar:
            out[shifted] = scalar
    return out


class CellReducer:
    """Exact substitution normal form on one certified D25 A^14 cell."""

    def __init__(self, cell, gbvars, unpack, p):
        self.cell = cell
        self.gbvars = tuple(gbvars)
        self.unpack = unpack
        self.p = p
        self.free_pos = {name: i for i, name in enumerate(FREE)}
        self.base_cache = {}
        self.pattern_cache = {}
        self.power_cache = {}

    def power(self, name, exponent):
        key = name, exponent
        if key not in self.power_cache:
            self.power_cache[key] = poly_pow(
                self.cell["maps"][name], exponent, self.p, len(FREE))
        return self.power_cache[key]

    def base_monomial(self, packed):
        if packed in self.base_cache:
            return self.base_cache[packed]
        exps = self.unpack(packed)
        free_exp = [0] * len(FREE)
        coeff = 1
        dependencies = []
        for name, exponent in zip(self.gbvars, exps):
            if not exponent:
                continue
            if name in self.cell["fixed"]:
                coeff = coeff * pow(self.cell["fixed"][name], exponent,
                                    self.p) % self.p
            elif name in self.free_pos:
                free_exp[self.free_pos[name]] += exponent
            else:
                assert name in DEP_BASE, (name, packed)
                dependencies.append((name, exponent))
        result = {tuple(free_exp): coeff}
        for name, exponent in dependencies:
            result = poly_mul(result, self.power(name, exponent), self.p)
        self.base_cache[packed] = result
        return result

    def cell_pattern(self, names):
        names = tuple(sorted(names))
        if names in self.pattern_cache:
            return self.pattern_cache[names]
        counts = {name: names.count(name) for name in set(names)}
        free_exp = [0] * len(FREE)
        result = {(0,) * len(FREE): 1}
        for name, exponent in counts.items():
            if name in self.free_pos:
                free_exp[self.free_pos[name]] += exponent
            elif name in DEP_LIFT:
                result = poly_mul(result, self.power(name, exponent), self.p)
            else:
                raise AssertionError(("not a D25 cell variable", name))
        result = monomial_times(result, tuple(free_exp), 1, self.p)
        self.pattern_cache[names] = result
        return result

    def base_polynomial(self, poly):
        result = {}
        for packed, coeff in poly.items():
            poly_add_scaled(result, self.base_monomial(packed), coeff, self.p)
        return result


def zero_tail_group_row(groups, reducer, t2x):
    """Exact row NF after setting every non-D25 deep coordinate to zero."""
    result = {}
    cell_names = set(FREE + DEP)
    for deep, basepoly in groups.items():
        if "uf30" in deep:
            continue
        mapped = tuple(t2x.get(name, name) for name in deep)
        if any(name not in cell_names for name in mapped):
            continue
        base_nf = reducer.base_polynomial(basepoly)
        if not base_nf:
            continue
        pattern_nf = reducer.cell_pattern(mapped)
        poly_add_scaled(result, poly_mul(base_nf, pattern_nf, reducer.p),
                        1, reducer.p)
    return result


def emit_free_ms(path, rows, p):
    with open(path, "w") as fh:
        fh.write(", ".join(FREE) + "\n%d\n" % p)
        lines = []
        for row in rows:
            terms = []
            for mono, coeff in sorted(row.items(), key=lambda x: (sum(x[0]), x[0])):
                factors = []
                for name, exponent in zip(FREE, mono):
                    if exponent:
                        factors.append(name if exponent == 1 else
                                       "%s^%d" % (name, exponent))
                terms.append(str(coeff) + ("*" + "*".join(factors)
                                           if factors else ""))
            lines.append("+".join(terms) if terms else "0")
        fh.write(",\n".join(lines) + "\n")


def zero_tail(root, ckdir, p, out_prefix):
    """Build the exact all-new-tails-zero D43 slice on all 16 D25 cells."""
    sys.path.insert(0, root)
    import d25_reduce as DR
    import d43_family2 as F
    replay_path = os.path.join(root, "d25_certificate_replay.json")
    replay = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    hint = replay["derived_witness"]
    roots1 = fourth_roots(p, int(replay["W1^4"]), int(hint["W1"]))
    roots2 = fourth_roots(p, int(replay["W2^4"]), int(hint["W2"]))
    parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
    reports = []
    for ci, (W1, W2) in enumerate(itertools.product(roots1, roots2)):
        cell = build_cell_map(parked, replay_path, W1, W2)
        reducer = CellReducer(cell, DR.GBVARS, DR.unpack, p)
        compat = []
        for k in range(26, 43, 2):
            path = os.path.join(ckdir,
                                "d43red_p%d_a00pp_band%d.pkl" % (p, k))
            with open(path, "rb") as fh:
                bank = pickle.load(fh)
            grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
            _hs, _ynames, rows, _C, L, _rank = rung_kernel(grouped, k, p)
            reduced = [zero_tail_group_row(row, reducer, F.T2X)
                       for row in rows]
            for vector in L:
                result = {}
                for scale, row in zip(vector, reduced):
                    poly_add_scaled(result, row, scale, p)
                compat.append(result)
        assert len(compat) == 52
        nonzero = [row for row in compat if row]
        ms_path = "%s_cell%02d.ms" % (out_prefix, ci)
        emit_free_ms(ms_path, nonzero, p)
        reports.append({
            "cell": ci, "W1": W1, "W2": W2,
            "n_rows": len(compat), "n_nonzero_rows": len(nonzero),
            "terms": [len(row) for row in nonzero],
            "degrees": [max((sum(m) for m in row), default=0)
                        for row in nonzero],
            "ms": ms_path, "base_monomial_cache": len(reducer.base_cache)
        })
        print("zero-tail p=%d cell=%02d W=(%d,%d): %d/%d nonzero -> %s"
              % (p, ci, W1, W2, len(nonzero), len(compat), ms_path),
              flush=True)
    report_path = out_prefix + "_report.json"
    with open(report_path, "w") as fh:
        json.dump({"status": "INTERNAL / UNREVIEWED", "prime": p,
                   "slice": "all 144 non-D25 D43 coordinates = 0",
                   "cells": reports}, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 ZERO-TAIL EXACT NF p=%d: PASS 16/16 -> %s" %
          (p, report_path))
    return reports


def quickshot(root, ckdir, p, free_values, out_path):
    """Point-specialized NF quickshot used to locate the exact affine tail."""
    sys.path.insert(0, root)
    import d25_reduce as DR
    import d43_family2 as F
    replay_path = os.path.join(root, "d25_certificate_replay.json")
    record = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    W1 = int(record["derived_witness"]["W1"])
    W2 = int(record["derived_witness"]["W2"])
    parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
    cell = build_cell_map(parked, replay_path, W1, W2)
    free_values = tuple(x % p for x in free_values)
    cell_values = {name: value for name, value in zip(FREE, free_values)}
    cell_values.update(cell["fixed"])
    for name, poly in cell["maps"].items():
        cell_values[name] = eval_free_poly(poly, free_values, p)
    assert set(DR.GBVARS) <= set(cell_values)
    base_values = [cell_values[name] for name in DR.GBVARS]

    compat = []
    rung_reports = {}
    for k in range(26, 43, 2):
        path = os.path.join(ckdir, "d43red_p%d_a00pp_band%d.pkl" % (p, k))
        with open(path, "rb") as fh:
            bank = pickle.load(fh)
        grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
        hs, ynames, rows, C, L, rank = rung_kernel(grouped, k, p)
        evaluated = [eval_group_row(row, base_values, cell_values, p,
                                    F.T2X, DR.unpack) for row in rows]
        rung_compat = []
        for vector in L:
            result = {}
            for scale, row in zip(vector, evaluated):
                poly_add_scaled(result, row, scale, p)
            # The rung variables were killed symbolically by L; make that a
            # second, representation-independent gate after specialization.
            mapped_y = {F.T2X.get(x, x) for x in ynames}
            assert not any(any(name in mapped_y for name in mono)
                           for mono in result)
            rung_compat.append(result)
        compat.extend(rung_compat)
        rung_reports[str(k)] = {
            "rows": len(rows), "rank_C": rank, "n_compat": len(L),
            "terms_after_cell_specialization": [len(x) for x in rung_compat],
            "max_external_degree": [max(map(len, x), default=0)
                                    for x in rung_compat]
        }

    assert len(compat) == 52
    variables = sorted({name for row in compat for mono in row for name in mono})
    x2tail = dict(F.X2T)
    affine_profiles = []
    exact_factorization = None
    rng = random.Random((p << 17) ^ sum(free_values) ^ 0xD43)
    for threshold in range(43, 75):
        selected = {name for name in variables
                    if (deep_level(name, x2tail) or -1) >= threshold}
        if not selected:
            continue
        affine = all(sum(name in selected for name in mono) <= 1
                     for row in compat for mono in row)
        profile = {"threshold": threshold, "n_selected": len(selected),
                   "affine": affine}
        if affine:
            lower = [name for name in variables if name not in selected]
            ranks, augmented = [], []
            for trial in range(4):
                assignment = {name: (0 if trial == 0 else rng.randrange(p))
                              for name in lower}
                A, b = affine_numeric(compat, selected, assignment, p)
                ranks.append(matrix_rank(A, p))
                augmented.append(matrix_rank([row + [rhs]
                                              for row, rhs in zip(A, b)], p))
            profile.update({"rank_A": ranks, "rank_augmented": augmented,
                            "selected": sorted(selected)})
            if threshold == 53:
                selected_order, columns, constants = affine_split_rows(
                    compat, selected)
                factored, failure = cdiag_factor(columns, p)
                factor_report = {"threshold": 53,
                                 "n_selected": len(selected_order),
                                 "factorization": "FAIL" if failure else "PASS"}
                if failure:
                    factor_report["failure"] = failure
                else:
                    C, factors = factored
                    L, rank_C = rref_left_kernel(C, p)
                    residuals = []
                    for vector in L:
                        residual = {}
                        for scale, const in zip(vector, constants):
                            poly_add_scaled(residual, const, scale, p)
                        residuals.append(residual)
                    # Direct replay against the original rows, not merely b.
                    for vector, residual in zip(L, residuals):
                        replay_row = {}
                        for scale, row in zip(vector, compat):
                            poly_add_scaled(replay_row, row, scale, p)
                        assert replay_row == residual
                    lower_variables = sorted({name for row in residuals
                                              for mono in row for name in mono})
                    residual_path = os.path.splitext(out_path)[0] + \
                        "_residual.ms"
                    emit_external_ms(residual_path, lower_variables,
                                     residuals, p)
                    # Negative control: inject a fresh monomial into a
                    # non-pivot row of a nontrivial column; C-diag must fail.
                    neg_columns = {name: [dict(x) for x in col]
                                   for name, col in columns.items()}
                    neg_name = next(name for name, col in neg_columns.items()
                                    if sum(bool(x) for x in col) >= 2)
                    nz = [i for i, x in enumerate(neg_columns[neg_name]) if x]
                    neg_columns[neg_name][nz[1]][("__NEGATIVE_CONTROL__",)] = 1
                    neg_factored, _neg_failure = cdiag_factor(neg_columns, p)
                    assert neg_factored is None
                    factor_report.update({
                        "rank_C": rank_C, "left_kernel_dimension": len(L),
                        "factor_terms": [len(x) for x in factors],
                        "residual_terms": [len(x) for x in residuals],
                        "residual_degrees": [max(map(len, x), default=0)
                                             for x in residuals],
                        "n_lower_variables": len(lower_variables),
                        "lower_variables": lower_variables,
                        "residual_ms": residual_path,
                        "negative_control": "injected monomial rejected"
                    })
                exact_factorization = factor_report
            affine_profiles.append(profile)

    structure_hash = hashlib.sha256()
    for row in compat:
        for mono in sorted(row):
            structure_hash.update(("*".join(mono) + "\n").encode())
        structure_hash.update(b",\n")
    rows_path = os.path.splitext(out_path)[0] + "_rows.pkl"
    with open(rows_path, "wb") as fh:
        pickle.dump({"prime": p, "fiber": "a00pp", "W1": W1, "W2": W2,
                     "free": dict(zip(FREE, free_values)), "rows": compat,
                     "rung_sizes": [6, 6, 5, 6, 6, 6, 6, 6, 5]},
                    fh, protocol=4)
    report = {
        "status": "INTERNAL / UNREVIEWED", "prime": p, "fiber": "a00pp",
        "method": "D43 rows already NF mod G23; exact D25 cell substitution",
        "cell": {"W1": W1, "W2": W2,
                 "free_values": dict(zip(FREE, free_values))},
        "gates": {"parked_34_symbolic": "PASS", "rung_C_diag": "PASS",
                  "rung_tail_cancellation": "PASS", "n_compat": 52},
        "rungs": rung_reports, "external_variables": variables,
        "n_external_variables": len(variables),
        "affine_threshold_profiles": affine_profiles,
        "exact_threshold53_factorization": exact_factorization,
        "specialized_rows_pickle": rows_path,
        "support_sha256": structure_hash.hexdigest()
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 NF QUICKSHOT p=%d: PASS; 52 rows; %d external vars -> %s"
          % (p, len(variables), out_path))
    return report


def selftest(root, out_path=None):
    replay_path = os.path.join(root, "d25_certificate_replay.json")
    replay = json.load(open(replay_path))
    report = {"status": "INTERNAL / UNREVIEWED", "gate": "PASS",
              "components": []}
    for p in PRIMES:
        parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
        parked_names, parked_prime, parked_rows = parse_ms(parked)
        assert parked_prime == p and len(parked_rows) == 34
        record = replay["parked_fibers"][str(p)]["a00pp"]
        hint = record["derived_witness"]
        roots1 = fourth_roots(p, int(record["W1^4"]), int(hint["W1"]))
        roots2 = fourth_roots(p, int(record["W2^4"]), int(hint["W2"]))
        for W1, W2 in itertools.product(roots1, roots2):
            cell = build_cell_map(parked, replay_path, W1, W2)
            # Negative control on the maps themselves: a nonzero perturbation
            # of any solved coordinate must violate its defining graph row.
            rng = random.Random((p << 32) ^ (W1 << 16) ^ W2)
            free_values = [rng.randrange(p) for _ in FREE]
            dep_values = {name: eval_free_poly(poly, free_values, p)
                          for name, poly in cell["maps"].items()}
            point = dict(zip(FREE, free_values))
            point.update(cell["fixed"])
            point.update(dep_values)
            assert all(eval_named_poly(row, parked_names, point, p) == 0
                       for row in parked_rows)
            bad_name = DEP[(W1 + W2) % len(DEP)]
            before = dep_values[bad_name]
            dep_values[bad_name] = (before + 1) % p
            assert dep_values[bad_name] != before
            bad_point = dict(point)
            bad_point[bad_name] = dep_values[bad_name]
            nbad = sum(eval_named_poly(row, parked_names, bad_point, p) != 0
                       for row in parked_rows)
            assert nbad > 0, ("negative control escaped", p, W1, W2,
                              bad_name)
            report["components"].append({
                "prime": p, "W1": W1, "W2": W2,
                "n_maps": len(cell["maps"]),
                "map_terms": {x: len(cell["maps"][x]) for x in DEP},
                "pivot_order": [x["var"] for x in cell["transcript"]],
                "parked_rows_zero_as_polynomials": 34,
                "negative_control": {"perturbed": bad_name,
                                     "nonzero_parked_rows": nbad}
            })
    assert len(report["components"]) == 32
    if out_path:
        with open(out_path, "w") as fh:
            json.dump(report, fh, indent=1, sort_keys=True)
            fh.write("\n")
    print("D43 NF CERTIFICATE SELFTEST: PASS (32/32 prime-cells; "
          "34/34 parked identities each)")
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--quickshot", action="store_true")
    parser.add_argument("--zero-tail", action="store_true")
    parser.add_argument("--prime", type=int, choices=PRIMES)
    parser.add_argument("--ckdir")
    parser.add_argument("--free", choices=("zero", "sequence"), default="sequence")
    parser.add_argument("--out")
    args = parser.parse_args()
    if args.selftest:
        selftest(args.root, args.out)
        return
    if args.quickshot:
        if not args.prime or not args.ckdir or not args.out:
            parser.error("--quickshot requires --prime, --ckdir, and --out")
        values = ([0] * len(FREE) if args.free == "zero"
                  else list(range(1, len(FREE) + 1)))
        quickshot(args.root, args.ckdir, args.prime, values, args.out)
        return
    if args.zero_tail:
        if not args.prime or not args.ckdir or not args.out:
            parser.error("--zero-tail requires --prime, --ckdir, and --out prefix")
        zero_tail(args.root, args.ckdir, args.prime, args.out)
        return
    parser.error("select --selftest, --quickshot, or --zero-tail")


if __name__ == "__main__":
    main()
