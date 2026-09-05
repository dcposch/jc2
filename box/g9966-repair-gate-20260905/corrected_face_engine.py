#!/usr/bin/env python3
"""Diagnostic (99,66) repair allowing the two h3 equality-face coefficients.

The source h3 strict-floor restriction is replaced by weight >=32, with
the t4*z5 coefficient fixed to -8/3 by the h2 face and t8*z2 initially free.
The old strict-support basis is retained and these two pure face terms added.
Both branch minor leaders are re-solved exactly with jet0 and Hc_11_0 free.
This diagnostic does not establish necessity of every imported chart block.
In particular the delta2 double-root coordinate remains at zeta=0.
No original input is modified; provenance and exact diff accompany this file.

Leading-row repair 2026-09-05 (cone-vertex gate §6–§7): ``pole_coeff``
subtracts the forced F/G face at the top pole tag (δ=2: 81/54; δ=5/2:
189/126). Every strictly-lower pole row is byte-identical to the old
homogeneous emission. Canonical helper: box/band-leading-fix-20260905/leading_pole.py.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import resource
import subprocess
import tempfile
import time
from typing import Iterable
from functools import lru_cache

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RECEIPT = ROOT / "box/g9966-d2-precise-20260905/receipt.run.v2"
FROZEN = ROOT / "box/g9966-d2-precise-20260905/frozen"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_inputs() -> dict:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    checked = []
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        assert Path(name).name == name
        actual = sha256(FROZEN / name)
        assert actual == expected, f"charged input mismatch: {name}"
        checked.append((name, actual))
    assert count == 8
    return {
        "receipt": str(RECEIPT),
        "lane_inputs_dir": str(FROZEN),
        "count": count,
        "all_hashes_match": True,
        "manifest_sha256": hashlib.sha256(
            "".join(f"{h}  {name}\n" for name, h in checked).encode()
        ).hexdigest(),
    }


def charged_driver_control() -> dict:
    """Pin the pristine engine; endpoint controls run separately before replay."""
    charged = FROZEN / "band_engine.py"
    actual = sha256(charged)
    expected = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
    assert actual == expected
    return {
        "charged_driver_sha256": actual,
        "separate_original_controls_required": True,
    }


def symbol(name: str) -> sp.Symbol:
    return sp.Symbol(name)


def expr_text(expr: sp.Expr) -> str:
    return str(sp.factor(expr))


# A sparse polynomial in (t,z): (t exponent,z exponent) -> coefficient.
TZ = dict[tuple[int, int], sp.Expr]


def tz_add(*items: TZ) -> TZ:
    out: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for item in items:
        for key, value in item.items():
            out[key] += value
    return {key: sp.expand(value) for key, value in out.items() if value != 0}


def tz_scale(item: TZ, scalar: int | sp.Expr) -> TZ:
    return {key: sp.expand(scalar * value) for key, value in item.items() if value != 0}


def tz_mul(left: TZ, right: TZ, max_t: int) -> TZ:
    out: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (r1, q1), a in left.items():
        for (r2, q2), b in right.items():
            if r1 + r2 <= max_t:
                out[(r1 + r2, q1 + q2)] += a * b
    return {key: sp.expand(value) for key, value in out.items() if value != 0}


def tz_dt(item: TZ) -> TZ:
    return {(r - 1, q): r * value for (r, q), value in item.items() if r}


def tz_dz(item: TZ) -> TZ:
    return {(r, q - 1): q * value for (r, q), value in item.items() if q}


def tz_times_t(item: TZ, max_t: int) -> TZ:
    return {(r + 1, q): value for (r, q), value in item.items() if r + 1 <= max_t}


def substitute_map(expr: sp.Expr, substitutions: dict[sp.Symbol, sp.Expr]) -> sp.Expr:
    if not substitutions or not expr.free_symbols.intersection(substitutions):
        return expr
    old = sp.expand(expr)
    for _ in range(20):
        new = sp.expand(old.subs(substitutions, simultaneous=True))
        if new == old:
            return new
        old = new
    raise AssertionError("substitution map did not stabilize")


def resolve_map(substitutions: dict[sp.Symbol, sp.Expr]) -> dict[sp.Symbol, sp.Expr]:
    resolved: dict[sp.Symbol, sp.Expr] = {}
    pending = dict(substitutions)
    for _ in range(len(pending) + 2):
        progress = False
        for variable in list(pending):
            rhs = pending[variable]
            blockers = rhs.free_symbols.intersection(pending)
            if not blockers:
                resolved[variable] = substitute_map(rhs, resolved)
                del pending[variable]
                progress = True
        if not pending:
            return resolved
        if not progress:
            # The elimination maps constructed here are triangular.  A cycle
            # indicates an implementation error, never a license to divide.
            raise AssertionError(f"cyclic substitution map: {sorted(map(str, pending))[:8]}")
    raise AssertionError("failed to resolve substitution map")


@dataclass
class Pivot:
    label: str
    variable: sp.Symbol
    coefficient: sp.Rational
    rhs: sp.Expr


def qstar_reduce(
    rows: list[tuple[str, sp.Expr]],
    eligible: set[sp.Symbol],
) -> tuple[list[tuple[str, sp.Expr]], dict[sp.Symbol, sp.Expr], list[Pivot], int]:
    """Eliminate affine pivots whose coefficient is a nonzero rational."""
    work = [(label, sp.expand(row)) for label, row in rows if row != 0]
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    pivots: list[Pivot] = []
    zero_rows = len(rows) - len(work)
    while True:
        choice = None
        for row_index, (label, row) in enumerate(work):
            candidates = sorted(row.free_symbols.intersection(eligible), key=str)
            for variable in candidates:
                coefficient = sp.diff(row, variable)
                if not coefficient.is_Rational or coefficient == 0:
                    continue
                remainder = sp.expand(row - coefficient * variable)
                if variable in remainder.free_symbols:
                    continue
                choice = (row_index, label, variable, sp.Rational(coefficient), remainder)
                break
            if choice is not None:
                break
        if choice is None:
            break
        row_index, label, variable, coefficient, remainder = choice
        rhs = sp.cancel(-remainder / coefficient)
        substitutions[variable] = rhs
        pivots.append(Pivot(label, variable, coefficient, rhs))
        eligible.remove(variable)
        del work[row_index]
        reduced: list[tuple[str, sp.Expr]] = []
        for old_label, old_row in work:
            image = sp.expand(old_row.subs(variable, rhs))
            if image == 0:
                zero_rows += 1
            else:
                reduced.append((old_label, image))
        work = reduced
    resolved = resolve_map(substitutions)
    residual = []
    for label, row in work:
        image = substitute_map(row, resolved)
        if image == 0:
            zero_rows += 1
        else:
            residual.append((label, image))
    return residual, resolved, pivots, zero_rows


def h3_template() -> tuple[TZ, list[sp.Symbol]]:
    out: TZ = {(0, 8): 1, (0, 9): 3, (0, 10): 3, (0, 11): 1}
    variables: list[sp.Symbol] = []
    for r in range(1, 12):
        cap = 11 - r
        vmin = max(0, (33 - 3 * r + 3) // 4)
        for degree in range(vmin, cap + 1):
            variable = symbol(f"Hc_{r}_{degree}")
            variables.append(variable)
            for j in range(degree - vmin + 1):
                out[(r, vmin + j)] = out.get((r, vmin + j), 0) + variable * comb(degree - vmin, j)
    assert len(variables) == 21
    out[(4,5)] = out.get((4,5),0) - sp.Rational(8,3)
    out[(8,2)] = out.get((8,2),0) + symbol("E82")
    variables.append(symbol("E82"))
    assert len(variables) == 22
    return {key: sp.expand(value) for key, value in out.items()}, variables


def h3_branch_map(branch: str) -> tuple[dict[sp.Symbol, sp.Expr], list[sp.Symbol], dict]:
    """Exact minor-leader solution after correcting the h3 D2 equality face."""
    if branch == 'delta2':
        encoded = {'E82': '-(-3*Hc_7_4*jet0 - 3*Hc_8_3 - 9*jet0**4*u**2 - 18*jet0**3*rho*u + 18*jet0**2*u**3 + 16*jet0**2*u + 27*jet0*rho*u**2 - 8*u**2)/3', 'Hc_1_10': '-3*jet0', 'Hc_1_8': '0', 'Hc_1_9': '0', 'Hc_2_7': '0', 'Hc_2_8': '-3*jet0**2', 'Hc_2_9': '3*(jet0**2 + u)', 'Hc_3_6': '-jet0**3', 'Hc_3_7': '2*jet0*(jet0**2 + 3*u)', 'Hc_3_8': '-jet0**3 - 3*jet0*u + 3*rho', 'Hc_4_6': '-(9*jet0**2*u + 8)/3', 'Hc_4_7': '(-9*jet0**2*u - 18*jet0*rho + 9*u**2 - 8)/3', 'Hc_5_5': '3*jet0*(-jet0**2*u - jet0*rho + u**2)', 'Hc_5_6': '(9*jet0**3*u + 9*jet0**2*rho + 9*jet0*u**2 + 16*jet0 + 18*rho*u)/3', 'Hc_6_4': '-(-18*jet0**2*u**2 - 8*jet0**2 - 18*jet0*rho*u + 3*u**3)/3', 'Hc_6_5': '(-9*jet0**2*u**2 - 8*jet0**2 + 3*u**3 - 16*u)/3', 'Hc_7_3': '-u*(-9*jet0**3*u - 18*jet0**2*rho + 9*jet0*u**2 + 16*jet0 + 9*rho*u)/3', 'Hc_9_2': '-(3*Hc_7_4*jet0**2 - 3*Hc_7_4*u + 3*Hc_8_3*jet0 + 9*jet0**5*u**2 + 18*jet0**4*rho*u - 30*jet0**3*u**3 - 16*jet0**3*u - 54*jet0**2*rho*u**2 + 9*jet0*u**4 + 24*jet0*u**2 + 9*rho*u**3)/3'}
        free_names = ['Hc_10_1', 'Hc_11_0', 'Hc_7_4', 'Hc_8_3', 'jet0', 'rho', 'u']
        localizer = 'rho'
    elif branch == 'delta52':
        encoded = {'E82': '-(-3*Hc_8_3 - 3*c*jet0 + 9*jet0**2*u**3 + 16*jet0**2*u - 18*jet0*u**2*v - 16*jet0*v - 8*u**2 + 9*u*v**2)/3', 'Hc_10_1': '-(-3*Hc_8_3*u - 6*c*jet0*u + 3*c*v + 9*jet0**2*u**4 + 24*jet0**2*u**2 - 18*jet0*u**3*v - 32*jet0*u*v - 8*u**3 + 9*u**2*v**2 + 8*v**2)/3', 'Hc_1_10': '-3*jet0', 'Hc_1_8': '0', 'Hc_1_9': '0', 'Hc_2_7': '0', 'Hc_2_8': '-3*jet0**2', 'Hc_2_9': '3*(jet0**2 + u)', 'Hc_3_6': '-jet0**3', 'Hc_3_7': '2*jet0*(jet0**2 + 3*u)', 'Hc_3_8': '-jet0**3 - 3*jet0*u - 3*v', 'Hc_4_6': '-(9*jet0**2*u + 8)/3', 'Hc_4_7': '(-9*jet0**2*u + 18*jet0*v + 9*u**2 - 8)/3', 'Hc_5_5': '3*jet0*(-jet0**2*u + jet0*v + u**2)', 'Hc_5_6': '(9*jet0**3*u - 9*jet0**2*v + 9*jet0*u**2 + 16*jet0 - 18*u*v)/3', 'Hc_6_4': '-(-18*jet0**2*u**2 - 8*jet0**2 + 18*jet0*u*v + 3*u**3)/3', 'Hc_6_5': '(-9*jet0**2*u**2 - 8*jet0**2 + 3*u**3 - 16*u + 9*v**2)/3', 'Hc_7_3': '-(-9*jet0**3*u**2 + 18*jet0**2*u*v + 9*jet0*u**3 + 16*jet0*u - 9*jet0*v**2 - 9*u**2*v)/3', 'Hc_7_4': '(3*c - 9*jet0**3*u**2 + 18*jet0**2*u*v + 9*jet0*u**3 - 9*jet0*v**2 - 9*u**2*v + 16*v)/3', 'Hc_9_2': '(-3*Hc_8_3*jet0 - 3*c*jet0**2 + 3*c*u + 12*jet0**3*u**3 + 16*jet0**3*u - 27*jet0**2*u**2*v - 16*jet0**2*v - 24*jet0*u**2 + 18*jet0*u*v**2 + 16*u*v - 3*v**3)/3'}
        free_names = ['Hc_11_0', 'Hc_8_3', 'jet0', 'u', 'v', 'c']
        localizer = 'c'
    else:
        raise ValueError(branch)
    substitutions = {symbol(name):sp.sympify(rhs) for name,rhs in encoded.items()}
    free = list(map(symbol,free_names))
    centre = {"parameters":free_names,"localization":localizer+"!=0",
              "minor_constant":"free","Hc_11_0":"free",
              "h3_face":"pi^8-(8/3)*pi^5+E82*pi^2",
              "E82":"solved in terms of retained Hc_8_3 and other free coefficients",
              "scope":"diagnostic corrected h3 equality face, no full necessity assertion"}
    return substitutions,free,centre


def h3_minor_control(branch: str, h3: TZ) -> dict:
    """Check the charged common-h3 leader without expanding a global F/G."""
    rho, u, v, c = map(symbol, ("rho", "u", "v", "c"))
    # Convert each z=w-1 coefficient to w coefficients, then substitute the
    # small minor w-series combinatorially.
    if branch == "delta2":
        rows = local_rows(h3, "delta2", 9, exact_only=False)
        expected = {9: {2: 3*rho, 3: 1}}
        for n in range(10):
            got = {k: row for (power, k), row in rows.items() if power == n and row != 0}
            want = expected.get(n, {})
            assert set(got) == set(want)
            assert all(sp.expand(got[k] - want[k]) == 0 for k in got)
        return {"target":"t^9*zeta^2*(zeta+3*rho)","verified":True,
                "minor_series":"y=jet0+u*t+zeta*t^2","jet0":"free"}
    rows = local_rows(h3, "delta52", 21, exact_only=False)
    expected = {21: {1: -c, 3: 1}}
    for n in range(22):
        got = {k: row for (power, k), row in rows.items() if power == n and row != 0}
        want = expected.get(n, {})
        assert set(got) == set(want)
        assert all(sp.expand(got[k] - want[k]) == 0 for k in got)
    return {"target":"s^21*pi*(pi^2-c)","verified":True,
            "minor_series":"y=jet0+u*t+v*t^2+pi*t^(5/2)","jet0":"free",
            "Hc_11_0":"free; no ODE compatibility imposed"}


def build_major_h2(branch: str, max_t: int) -> tuple[TZ, set[sp.Symbol], dict]:
    h3, hvars = h3_template()
    hmap, hfree, centre = h3_branch_map(branch)
    h3 = {key: substitute_map(value, hmap) for key, value in h3.items()}
    control = h3_minor_control(branch, h3)
    h3cube = tz_mul(tz_mul(h3, h3, max_t), h3, max_t)

    # The low-q major-output coordinates have unit C3 (q<=10) or unit C2
    # (11<=q<=21) leading columns.  There are 106 before the seven D1 rows.
    dvars: dict[tuple[int,int], sp.Symbol] = {}
    for r in range(1, 34):
        for q in range(34-r):
            if 3*r + 4*q >= 97 and q <= 21:
                dvars[(r,q)] = symbol(f"K2c_{r}_{q}")
    assert len(dvars) == 106

    def raw_coefficient(r: int, q: int) -> sp.Expr:
        if (r,q) in dvars:
            return dvars[(r,q)]
        return h3cube.get((r,q), sp.Integer(0))

    # Exact h2 D1 rows: W=97 has k=0..4, W=98 has k=0..1.
    rows: list[tuple[str,sp.Expr]] = []
    for W, kmax in ((97,4),(98,1)):
        positions = [(r,q) for r in range(1,34) for q in range(34-r) if 3*r+4*q == W]
        for k in range(kmax+1):
            row = sum(comb(q,k)*raw_coefficient(r,q) for r,q in positions if q >= k)
            rows.append((f"h2_D1_W{W}_k{k}", sp.expand(row)))
    pivot_order = [
        dvars[(11,16)],dvars[(15,13)],dvars[(19,10)],dvars[(23,7)],dvars[(27,4)],
        dvars[(10,17)],dvars[(14,14)],
    ]
    # Force the charged determinant choice rather than letting symbol names
    # choose a different but equivalent chart.
    work = list(rows)
    h2map: dict[sp.Symbol,sp.Expr] = {}
    pivots = []
    for variable in pivot_order:
        selected = None
        for index,(label,row) in enumerate(work):
            row = substitute_map(row,h2map)
            coefficient = sp.diff(row,variable)
            if coefficient.is_Rational and coefficient != 0:
                selected=(index,label,row,sp.Rational(coefficient)); break
        assert selected is not None
        index,label,row,coefficient=selected
        rhs=sp.cancel(-(row-coefficient*variable)/coefficient)
        h2map[variable]=rhs
        pivots.append((label,str(variable),str(coefficient)))
        del work[index]
        work=[(lab,sp.expand(rr.subs(variable,rhs))) for lab,rr in work]
    h2map=resolve_map(h2map)
    assert all(substitute_map(row,h2map)==0 for _label,row in rows)
    dfree=set(dvars.values())-set(h2map)
    assert len(dfree)==99

    k2: TZ = {}
    # fixed P^3 top
    for j in range(10):
        k2[(0,24+j)] = sp.Integer(comb(9,j))
    equality={(4*k,24-3*k):sp.Integer((-1)**k*comb(8,k)) for k in range(1,9)}
    for r in range(1,max_t+1):
        for q in range(34-r):
            value=sp.Integer(0)
            if (r,q) in equality:
                value=equality[(r,q)]
            elif 3*r+4*q>=97:
                value=raw_coefficient(r,q)
            value=substitute_map(sp.expand(value),h2map)
            if value!=0:
                k2[(r,q)]=value
    inner_free=set(hfree)|dfree
    expected=106 if branch=="delta2" else 105
    assert len(inner_free)==expected
    return k2,inner_free,{
        "h3_control":control,"centre":centre,
        "h3_free":[str(v) for v in hfree],
        "major_output_coordinate_count_before_D1":106,
        "major_h2_D1_pivots":pivots,
        "major_output_free_count":99,
        "inner_dimension_including_centres":len(inner_free),
        "coordinate_change":"K2c low-q coordinates have unit leading C3/C2 columns",
    }


OUTER_SPECS = {
    "A2": (65, 189, 583),
    "A3": (98, 285, 879),
    "B1": (32, 93, 287),
    "B2": (65, 189, 583),
}


def outer_state(max_offset: int) -> tuple[dict[str,dict[tuple[int,int],sp.Expr]],set[sp.Symbol],dict]:
    coordinates: dict[str,dict[tuple[int,int],sp.Symbol]]={}
    preblock_raw=0
    preblock_rank=0
    for block,(degree,W0,threshold) in OUTER_SPECS.items():
        all_positions=[(r,q) for r in range(degree+1) for q in range(min(32,degree-r)+1)]
        kept={(r,q):symbol(f"{block}c_{r}_{q}") for r,q in all_positions if 3*r+4*q>=W0}
        coordinates[block]=kept
        preblock_rank += len(all_positions)-len(kept)
        # Literal nonzero D1 scalar rows supported below W0.
        labels=set()
        for r,q in all_positions:
            if 3*r+4*q>=W0: continue
            for k in range(q+1):
                exponent=9*r+12*q+k
                if exponent<threshold:
                    labels.add((exponent,k))
        preblock_raw += len(labels)
    assert (preblock_raw,preblock_rank)==(15934,5598)

    substitutions: dict[sp.Symbol,sp.Expr]={}
    ledger=[]
    all_boundary_rows=[]
    for offset in range(max_offset+1):
        band_rows=[]
        band_variables=set()
        by_block={}
        for block,(_degree,W0,threshold) in OUTER_SPECS.items():
            W=W0+offset
            positions=[p for p in coordinates[block] if 3*p[0]+4*p[1]==W]
            rows=[]
            for k in range(max(0,threshold-3*W)):
                row=sum(comb(q,k)*coordinates[block][(r,q)] for r,q in positions if q>=k)
                row=substitute_map(sp.expand(row),substitutions)
                if row!=0:
                    rows.append((f"{block}_D1_s{offset}_k{k}",row))
                    band_variables.update(row.free_symbols)
            band_rows.extend(rows)
            by_block[block]={"raw_rows":len(rows),"positions":len(positions)}
        residual,band_map,pivots,zero_rows=qstar_reduce(band_rows,set(band_variables))
        assert not residual
        substitutions.update(band_map)
        substitutions=resolve_map(substitutions)
        all_boundary_rows.extend(band_rows)
        ledger.append({
            "offset":offset,"raw_rows":len(band_rows),"Qstar_pivots":len(pivots),
            "dependent_zero":zero_rows,"by_block":by_block,
            "pivot_variables":[str(p.variable) for p in pivots],
        })
    resolved_coordinates={
        block:{pos:substitute_map(var,substitutions) for pos,var in values.items()}
        for block,values in coordinates.items()
    }
    all_vars=set().union(*(set(values.values()) for values in coordinates.values()))
    free=all_vars-set(substitutions)
    cumulative_pivots=sum(item["Qstar_pivots"] for item in ledger)
    expected_boundary=[41,38,33,25,19,11,6,3]
    assert [item["Qstar_pivots"] for item in ledger]==expected_boundary[:max_offset+1]
    return resolved_coordinates,free,{
        "basis":"K_Q=t^D Q(t^-1,w/t)=sum c_(r,q)t^r(w-1)^q",
        "weight":"W=3*r+4*q",
        "preblock":{
            "imposed_D2_coordinate_rows":preblock_rank,
            "Qstar_pivots":preblock_rank,
            "surviving_coordinates":6600-preblock_rank,
            "redundant_D1_labels_on_deleted_coordinates":preblock_raw,
        },
        "D1_offsets":ledger,
        "D1_cumulative_pivots":cumulative_pivots,
        "outer_free_count":len(free),
    }


def outer_effective_tz(
    coordinates: dict[str,dict[tuple[int,int],sp.Expr]], block: str, max_t: int
) -> TZ:
    # Each coefficient block is one degree below its containing term, so its
    # normalized contribution to KF/KG has one additional factor of t.
    return {
        (r+1,q):value for (r,q),value in coordinates[block].items()
        if r+1<=max_t and value!=0
    }


def build_FG(k2: TZ, outer: dict[str,dict[tuple[int,int],sp.Expr]], max_t: int) -> tuple[TZ,TZ]:
    k2sq=tz_mul(k2,k2,max_t)
    k2cube=tz_mul(k2sq,k2,max_t)
    a2=outer_effective_tz(outer,"A2",max_t)
    a3=outer_effective_tz(outer,"A3",max_t)
    b1=outer_effective_tz(outer,"B1",max_t)
    b2=outer_effective_tz(outer,"B2",max_t)
    KF=tz_add(k2cube,tz_mul(a2,k2,max_t),a3)
    KG=tz_add(k2sq,tz_mul(b1,k2,max_t),b2)
    return KF,KG


def z_band_to_w(item: TZ, t_power: int) -> dict[int,sp.Expr]:
    out: dict[int,sp.Expr]=defaultdict(lambda:sp.Integer(0))
    for (r,q),value in item.items():
        if r!=t_power: continue
        # (w-1)^q=sum_k binom(q,k)(-1)^(q-k)w^k
        for k in range(q+1):
            out[k]+=value*comb(q,k)*((-1)**(q-k))
    return {k:sp.expand(value) for k,value in out.items() if value!=0}


def jacobian_band(KF: TZ,KG: TZ,t_power: int) -> dict[int,sp.Expr]:
    max_t=t_power
    term1=tz_scale(tz_mul(KF,tz_dz(KG),max_t),99)
    term2=tz_scale(tz_mul(tz_times_t(tz_dt(KF),max_t),tz_dz(KG),max_t),-1)
    term3=tz_scale(tz_mul(tz_dz(KF),KG,max_t),-66)
    term4=tz_mul(tz_dz(KF),tz_times_t(tz_dt(KG),max_t),max_t)
    return z_band_to_w(tz_add(term1,term2,term3,term4),t_power)


def jacobian_normalization_control() -> dict:
    """Reproduce the charged first and named-next homogeneous J rows."""
    f=[symbol(f"control_f{j}") for j in range(11)]
    g=[symbol(f"control_g{j}") for j in range(2)]
    k20={(0,24+j):sp.Integer(comb(9,j)) for j in range(10)}
    F0=tz_mul(tz_mul(k20,k20,1),k20,1)
    G0=tz_mul(k20,k20,1)
    F1:TZ={}
    G1:TZ={}
    for j,var in enumerate(f):
        for q in range(j+1):
            F1[(1,q)]=F1.get((1,q),0)+var*comb(j,q)
    for j,var in enumerate(g):
        for q in range(j+1):
            G1[(1,q)]=G1.get((1,q),0)+var*comb(j,q)
    J=jacobian_band(tz_add(F0,F1),tz_add(G0,G1),1)
    assert sp.expand(J[17]-1764*f[0])==0
    named=(17947724418624*f[0]-4326935131200*f[1]+911675169504*f[2]
           -165812670144*f[3]+25622917056*f[4]-3294472896*f[5]
           +342460800*f[6]-27604416*f[7]+1615296*f[8]-60864*f[9]
           +1104*f[10]+131040*g[0]-1656*g[1])
    assert sp.expand(J[27]-named)==0
    return {"x145_y17":"1764*f0","x135_y27":expr_text(named),"verified":True}


def all_w_bands(item: TZ) -> dict[int,dict[int,sp.Expr]]:
    powers=sorted({r for r,_q in item})
    return {r:z_band_to_w(item,r) for r in powers}


def local_rows(item: TZ,branch: str,max_power: int,exact_only: bool=True) -> dict[tuple[int,int],sp.Expr]:
    wbands=all_w_bands(item)
    out: dict[tuple[int,int],sp.Expr]=defaultdict(lambda:sp.Integer(0))
    jet0,u,v=map(symbol,("jet0","u","v"))
    if branch=="delta2":
        for r,poly in wbands.items():
            for j,coefficient in poly.items():
                if r+j>max_power:
                    continue
                for d in range(j+1):
                    for k in range(j-d+1):
                        a=j-d-k
                        n=r+d+2*a+3*k
                        if n<=max_power:
                            multinomial=factorial(j)//(factorial(d)*factorial(a)*factorial(k))
                            out[(n,k)]+=coefficient*multinomial*jet0**d*u**a
    else:
        for r,poly in wbands.items():
            for j,coefficient in poly.items():
                if 2*r+2*j>max_power:
                    continue
                for d in range(j+1):
                    for b in range(j-d+1):
                        for k in range(j-d-b+1):
                            a=j-d-b-k
                            n=2*r+2*d+4*a+6*b+7*k
                            if n<=max_power:
                                multinomial=(factorial(j)//(factorial(d)*factorial(a)
                                             *factorial(b)*factorial(k)))
                                out[(n,k)]+=coefficient*multinomial*jet0**d*u**a*v**b
    return {tag:sp.expand(value) for tag,value in out.items() if value!=0}


@lru_cache(maxsize=None)
def raw_minor_support(branch: str, name: str) -> dict[int, tuple[int, ...]]:
    """Charged lower-support row labels, grouped by normalized local power."""
    degree = 99 if name == "F" else 66
    pole = 18 if name == "F" else 12
    tags: set[tuple[int,int]] = set()
    if branch == "delta2":
        shift = 81 if name == "F" else 54
        for i in range(degree):
            for j in range(degree-i):
                for k in range(j+1):
                    exponent = pole-i+j+k
                    if exponent <= 0:
                        tags.add((exponent+shift,k))
    else:
        pole = 9 if name == "F" else 6
        shift = 189 if name == "F" else 126
        for i in range(degree):
            for j in range(degree-i):
                for b in range(j+1):
                    for k in range(j-b+1):
                        exponent = pole-2*i+2*j+2*b+3*k
                        if exponent <= 0:
                            tags.add((exponent+shift,k))
    grouped: dict[int,list[int]]=defaultdict(list)
    for n,k in sorted(tags):
        grouped[n].append(k)
    return {n:tuple(values) for n,values in grouped.items()}


def raw_minor_tags(branch: str, name: str, local_power: int) -> tuple[int, ...]:
    return raw_minor_support(branch,name).get(local_power,())


# Leading-row repair 2026-09-05. Keep in sync with
# box/band-leading-fix-20260905/leading_pole.py (g9966_*).
def leading_pole_power(branch: str, name: str) -> int:
    if branch == "delta2":
        return 81 if name == "F" else 54
    if branch == "delta52":
        return 189 if name == "F" else 126
    raise ValueError(branch)


@lru_cache(maxsize=None)
def leading_pole_target_table(branch: str, name: str) -> dict[int, sp.Expr]:
    """Forced F/G face: (K3 lead)^9 / (K3 lead)^6. Gate §6."""
    exp = 9 if name == "F" else 6
    if branch == "delta2":
        zeta, rho = sp.symbols("zeta rho")
        face = zeta**2 * (zeta + 3 * rho)
        poly = sp.Poly(sp.expand(face**exp), zeta)
    else:
        pi, c = sp.symbols("pi c")
        face = pi * (pi**2 - c)
        poly = sp.Poly(sp.expand(face**exp), pi)
    return {int(mon[0]): sp.expand(cf) for mon, cf in poly.terms()}


def pole_coeff(table, n, k, branch, name):
    """F/G pole entry: coefficient minus target at the leading local power."""
    value = table.get((n, k), sp.Integer(0))
    if n != leading_pole_power(branch, name):
        return value
    return sp.expand(value - leading_pole_target_table(branch, name).get(k, 0))


def rows_hash(rows: Iterable[tuple[str,sp.Expr]]) -> str:
    payload="".join(f"{label}\t{sp.srepr(sp.expand(row))}\n" for label,row in rows)
    return hashlib.sha256(payload.encode()).hexdigest()


def small_rational_point(
    rows: list[tuple[str,sp.Expr]], residual: list[tuple[str,sp.Expr]],
    linear_map: dict[sp.Symbol,sp.Expr], all_free: set[sp.Symbol],
    localized: sp.Symbol,
) -> dict:
    """Try a bounded QQ section, then verify every cumulative row exactly."""
    remaining=all_free-set(linear_map)
    jet0=symbol("jet0")
    trials=[sp.Rational(1),sp.Rational(-1),sp.Rational(2),sp.Rational(-2),
            sp.Rational(1,2),sp.Rational(-1,2)]
    settings=[]
    if jet0 in remaining:
        settings=[{jet0:value} for value in trials]
    else:
        dependencies=sorted(linear_map[jet0].free_symbols.intersection(remaining)
                            -{localized},key=str)
        for dependency in dependencies:
            settings.extend({dependency:value} for value in trials)
        if dependencies:
            settings.append({dependency:sp.Integer(1) for dependency in dependencies})
        else:
            settings=[{}]
    attempted=0
    for local_value in trials:
        for setting in settings:
            attempted+=1
            point={variable:sp.Integer(0) for variable in remaining}
            point[localized]=local_value
            point.update(setting)
            if any(sp.expand(row.xreplace(point))!=0 for _label,row in residual):
                continue
            full=dict(point)
            for variable,rhs in linear_map.items():
                value=sp.cancel(rhs.xreplace(point))
                if value.free_symbols or not value.is_Rational:
                    break
                full[variable]=value
            else:
                assert set(full)==all_free
                assert full[localized]!=0
                assert all(not value.free_symbols and value.is_Rational for value in full.values())
                assert all(sp.expand(row.xreplace(full))==0 for _label,row in rows)
                if full[jet0]==0:
                    continue
                payload="".join(f"{variable}={full[variable]}\n" for variable in sorted(full,key=str))
                zero_payload="".join(f"{label}\t0\n" for label,_row in rows)
                nonzero={str(variable):str(full[variable]) for variable in sorted(full,key=str)
                         if full[variable]!=0}
                return {
                    "status":"FOUND","field":"Q","localized":str(localized),
                    "localized_value":str(full[localized]),"jet0_value":str(full[jet0]),
                    "jet0_nonzero":full[jet0]!=0,"all_free_count":len(all_free),
                    "nonzero_assignment":nonzero,"omitted_all_free_default":"0",
                    "full_assignment_sha256":hashlib.sha256(payload.encode()).hexdigest(),
                    "resolved_Qstar_back_substitutions":len(linear_map),
                    "raw_rows_verified_zero":len(rows),"residual_rows_verified_zero":len(residual),
                    "raw_rows_hash":rows_hash(rows),
                    "raw_zero_image_sha256":hashlib.sha256(zero_payload.encode()).hexdigest(),
                    "localization_wrapper_value":str(1/full[localized]),
                    "gauge_ledger":{"group_element":"(x,y)->(x,y+a1)",
                                    "minor_jet0_pin_released":True,
                                    "Hc_11_0_free":True},
                    "scope":"rational point of cumulative necessary chart; not a Keller pair",
                    "attempts":attempted,
                }
    return {"status":"NOT_FOUND_BOUNDED_Q","attempts":attempted,
            "trial_values":[str(value) for value in trials],
            "scope":"failure of this bounded search is not nonexistence"}


def singular_dimension(
    residual: list[tuple[str,sp.Expr]], branch: str, emit_path: Path | None=None
) -> dict:
    if not residual:
        if emit_path is not None:
            emit_path.write_text("// zero residual ideal over Q\n",encoding="utf-8")
        return {"unit_ideal":False,"active_variables":0,"dimension":0,"codimension":0,
                "basis":["0"],"wrapper_control":"not_needed"}
    expressions=[sp.expand(row) for _label,row in residual]
    variables=sorted(set().union(*(row.free_symbols for row in expressions)),key=str)
    wrapper=symbol("Zrho" if branch=="delta2" else "Zc")
    localized=symbol("rho" if branch=="delta2" else "c")
    if localized not in variables:
        variables.append(localized)
        variables.sort(key=str)
    ringvars=variables+[wrapper]
    def singular_expr(expr:sp.Expr)->str:
        return str(expr).replace("**","^")
    ideal_entries=[singular_expr(row) for row in expressions]+[f"{wrapper}*{localized}-1"]
    script=(
        f"ring R=0,({','.join(map(str,ringvars))}),dp;\n"
        f"ideal I={','.join(ideal_entries)};\n"
        "ideal S=std(I);\n"
        'print("BEGIN_DIM"); print(dim(S)); print("END_DIM");\n'
        'print("BEGIN_GB"); print(S); print("END_GB");\n'
        f"ideal EmptyControl={localized},{wrapper}*{localized}-1;\n"
        f"ideal PointControl={localized}-1,{wrapper}*{localized}-1;\n"
        f"ideal RawControl={','.join(singular_expr(row) for row in expressions)};\n"
        'print("BEGIN_CONTROLS"); print(reduce(1,std(EmptyControl))); '
        'print(reduce(1,std(PointControl))); print(reduce(1,std(RawControl))); '
        'print("END_CONTROLS");\n'
        "quit;\n"
    )
    if emit_path is not None:
        emit_path.write_text(script,encoding="utf-8")
    run=subprocess.run(["Singular","-q"],input=script,text=True,capture_output=True,check=True)
    output=run.stdout
    def section(name:str)->str:
        return output.split(f"BEGIN_{name}\n",1)[1].split(f"\nEND_{name}",1)[0].strip()
    dimension=int(section("DIM").splitlines()[-1])
    gb=section("GB")
    controls=section("CONTROLS").splitlines()
    unit=dimension < 0
    # wrapper adds one variable and one equation, so dimension is the
    # localized dimension in the original active variables.
    codimension=len(variables)-dimension
    assert controls[-3:-1]==["0","1"]
    raw_unit=controls[-1]=="0"
    gb_lines=gb.splitlines()
    return {"unit_ideal":unit,"active_variables":len(variables),"dimension":dimension,
            "codimension":codimension,"basis_line_count":len(gb_lines),
            "basis_sha256":hashlib.sha256((gb+"\n").encode()).hexdigest(),
            "basis_preview":gb_lines[:20],
            "wrapper":f"{wrapper}*{localized}-1",
            "wrapper_control":"<p,Zp-1> unit; <p-1,Zp-1> nonunit",
            "raw_residue_unit_ideal":raw_unit}


def stage_spec(branch:str,stage:int)->dict:
    if branch=="delta2":
        pole_power=4+stage
        pole_exponents={"F":pole_power-81,"G":pole_power-54}
    else:
        pole_power=8+stage
        pole_exponents={"F":pole_power-189,"G":pole_power-126}
    if stage==0:
        jacobian={"t_power":1,"degree":162,"w_powers":[27]}
    elif stage==1:
        jacobian={"t_power":1,"degree":162,"w_powers":list(range(28,163))}
    else:
        tpower=stage
        jacobian={"t_power":tpower,"degree":163-tpower,"w_powers":list(range(164-tpower))}
    return {"stage":stage,"D1_offset":stage if stage<=7 else None,
            "pole_local_power":pole_power,"pole_exponents":pole_exponents,
            "jacobian":jacobian}


def cumulative_rows(branch:str,stage:int,KF:TZ,KG:TZ) -> tuple[list[tuple[str,sp.Expr]],dict]:
    rows=[]
    accounting={"prior":{},"stages":[]}
    # Charged prefix: exact local bands and ten J162 slots.
    fprior=[1,2,3] if branch=="delta2" else [2,4,6]
    gprior=list(fprior)
    f_local=local_rows(KF,branch,max(stage_spec(branch,stage)["pole_local_power"],max(fprior)))
    g_local=local_rows(KG,branch,max(stage_spec(branch,stage)["pole_local_power"],max(gprior)))
    for name,bands,table in (("F",fprior,f_local),("G",gprior,g_local)):
        count=0
        for n in bands:
            tags=raw_minor_tags(branch,name,n)
            assert tags
            for k in tags:
                rows.append((f"prior_{name}_local{n}_coord{k}",pole_coeff(table,n,k,branch,name)))
                count+=1
        accounting["prior"][name]=count
    J1=jacobian_band(KF,KG,1)
    for k in range(17,27):
        rows.append((f"prior_J_d162_k{k}",J1.get(k,sp.Integer(0))))
    accounting["prior"]["J162"]=10

    # Continuation stages.
    for current in range(stage+1):
        spec=stage_spec(branch,current)
        n=spec["pole_local_power"]
        stage_counts={"stage":current,"F":0,"G":0,"J":0}
        for name,table in (("F",f_local),("G",g_local)):
            tags=raw_minor_tags(branch,name,n)
            for k in tags:
                rows.append((f"stage{current}_{name}_local{n}_coord{k}",pole_coeff(table,n,k,branch,name)))
                stage_counts[name]+=1
        jspec=spec["jacobian"]
        J=jacobian_band(KF,KG,jspec["t_power"])
        for k in jspec["w_powers"]:
            rows.append((f"stage{current}_J_d{jspec['degree']}_k{k}",J.get(k,sp.Integer(0))))
            stage_counts["J"]+=1
        accounting["stages"].append(stage_counts)
    return rows,accounting


def run(branch:str,stage:int,emit_singular:Path|None=None)->dict:
    started=time.perf_counter()
    custody=verify_inputs()
    endpoint=charged_driver_control()
    jac_control=jacobian_normalization_control()
    raw_counts={
        "delta2_F":sum(map(len,raw_minor_support("delta2","F").values())),
        "delta2_G":sum(map(len,raw_minor_support("delta2","G").values())),
        "delta52_F":sum(map(len,raw_minor_support("delta52","F").values())),
        "delta52_G":sum(map(len,raw_minor_support("delta52","G").values())),
    }
    assert raw_counts=={
        "delta2_F":1134,"delta2_G":513,"delta52_F":1316,"delta52_G":594,
    }
    spec=stage_spec(branch,stage)
    max_j=max(stage_spec(branch,i)["jacobian"]["t_power"] for i in range(stage+1))
    max_pole=spec["pole_local_power"] if branch=="delta2" else (spec["pole_local_power"]+1)//2
    max_t=max(max_j,max_pole,4)
    k2,inner_free,major=build_major_h2(branch,max_t)
    outer,outer_free,outer_meta=outer_state(min(stage,7))
    KF,KG=build_FG(k2,outer,max_t)
    rows,accounting=cumulative_rows(branch,stage,KF,KG)
    all_free=set(inner_free)|set(outer_free)
    localized=symbol("rho" if branch=="delta2" else "c")
    residual,linear_map,pivots,zero_rows=qstar_reduce(rows,set(all_free)-{localized})
    remaining=all_free-set(linear_map)
    assert localized in remaining
    residual_symbols=set().union(*(row.free_symbols for _label,row in residual)) if residual else set()
    assert residual_symbols.issubset(remaining)
    rational_point=small_rational_point(rows,residual,linear_map,all_free,localized)
    singular=singular_dimension(residual,branch,emit_singular)
    if rational_point["status"]=="FOUND":
        # An exact point in the localized chart and a unit Gröbner basis are
        # mutually exclusive.  Fail closed if either certificate path drifts.
        assert singular["unit_ideal"] is False
    if singular["unit_ideal"]:
        dimension=None
        verdict="DEAD"
    else:
        dimension=len(remaining)-singular["codimension"]
        verdict="COUNTING-BOUND"
    elapsed=time.perf_counter()-started
    rss_self=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_children=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    rss=max(rss_self,rss_children)
    return {
        "type":"EXACT-Q JOINT GLOBAL BAND / FALLACY-v2",
        "branch":branch,"stage_spec":spec,"filtration_convention":{
            "outer":"D2 preblock, then W-W0 offsets; W=3r+4q",
            "pole":"next occupied local exponent (branch-specific)",
            "Jacobian":"named d162,k27; finish d162; then total degrees downward",
            "warning":"synchronization is a driver convention, not a source theorem",
        },
        "precise_gauge_repair":{
            "sound_D2_floor_retained":True,
            "minor_constant":"jet0 free",
            "released_gauge_pin":"minor jet0=0",
            "delta52_Hc_11_0":"free",
            "h3_equality_face_correction":True,
            "new_free_dimensions_over_pristine":2 if branch=="delta2" else 3,
        },
        "custody":custody,"driver_sha256":sha256(Path(__file__)),
        "charged_endpoint":endpoint,
        "major":major,"outer_major":outer_meta,"row_accounting":accounting,
        "jacobian_normalization_control":jac_control,
        "raw_minor_support_control":raw_counts,
        "joint_elimination":{
            "input_row_labels_excluding_preeliminated_major_rows":len(rows),
            "all_labeled_rows_hash":rows_hash(rows),
            "raw_nonzero_count":sum(row!=0 for _label,row in rows),
            "Qstar_pivots":len(pivots),"dependent_or_zero_rows":zero_rows,
            "pivot_ledger":[{"row":p.label,"variable":str(p.variable),
                             "coefficient":str(p.coefficient),"rhs":expr_text(p.rhs)}
                            for p in pivots],
            "residual_count":len(residual),
            "residual_rows":[{"label":label,"expression":expr_text(row)} for label,row in residual],
            "residual_hash":rows_hash(residual),"singular":singular,
        },
        "counts":{
            "inner_free_before_outer":len(inner_free),
            "outer_free_after_current_major_band":len(outer_free),
            "linear_free_before_residue":len(remaining),
            "exact_Krull_dimension_localized":dimension,
        },
        "necessary_chart_rational_point":rational_point,
        "verdict":verdict,"nonlinear_residue_appears":bool(residual),
        "resources":{"wall_seconds":elapsed,"peak_rss_kib":rss,
                     "self_peak_rss_kib":rss_self,"children_peak_rss_kib":rss_children,
                     "note":"max of process/child lifetime high-water; isolate stages for per-band RSS"},
        "unresolved_quotient_generators":sorted(map(str,remaining)),
        "free_coordinate_list_is_valid":not residual,
        "coordinate_ring_map":{
            "field":"Q",
            "generator_order":"lexicographic symbol name for Q*; Singular dp on active residual generators",
            "K2c_definition":"K2c_r_q=[t^r(w-1)^q](K3^3+(t^22 C2)K3+t^33 C3), low q, after D2",
            "unit_leader":"C3c_r_q for q<=10; C2c_r_(q-11) for 11<=q<=21",
            "structural_certificate_import":{
                "source":"charged major_tower_structure.py/json",
                "facts":"106 low-q coordinates before the seven D1 pivots; unit-triangular C3/C2 leaders",
                "limitation":"the full original C2/C3 inverse map is not serialized; K2c is the declared computation basis",
            },
        },
        "next_stage":stage_spec(branch,stage+1),
    }


def main()->None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--branch",choices=["delta2","delta52"],required=True)
    parser.add_argument("--stage",type=int,required=True)
    parser.add_argument("--emit-singular",type=Path)
    args=parser.parse_args()
    assert args.stage>=0
    print(json.dumps(run(args.branch,args.stage,args.emit_singular),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
