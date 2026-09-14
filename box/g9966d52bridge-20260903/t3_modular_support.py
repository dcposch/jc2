#!/usr/bin/env python3
"""Emit finite-field support probes for the complete delta=5/2 bridge.

This is deliberately *not* an elimination driver.  It reconstructs the
charged stage-7 endpoint over QQ, checks the exact 869-coordinate quotient,
then deterministically specializes those coordinates and the 4+34 effective
T-coefficients in one of three prime fields.  The emitted Singular programs
have only the bookkeeping variables ``s,pi`` and work in ``s^1179=0``.

Consequently a term of the residual is one sampled nonzero bridge row.  The
programs print term counts and min/max (s,pi) support only; they never compute
a chart rank, affine pivots, or a chart Groebner basis.  The only ``std`` in
an emitted program is the one-generator monomial quotient ``<s^1179>``.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from typing import Iterable

for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_name, "1")

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.IAeCOg/inputs")
RECEIPT = ROOT / "xmodel/g9966-delta52-bridge-sol56-20260903.run.v2"
STAGE7 = FROZEN / "stage7.json"
FREE_LIST = FROZEN / "stage7-free-coefficients.txt"
NEXT = FROZEN / "next-stage8-system.json"
CHARGED_ENGINE = FROZEN / "band_engine.py"

CAP = 1178
T2_CAP = 391
PRIMES = (32003, 104729, 1299709)
SPECIALIZATION_DOMAIN = b"g9966-delta52-bridge-support-v1\0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_charged_module():
    spec = importlib.util.spec_from_file_location("charged_band_engine_modular_support", CHARGED_ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load charged band engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_frozen() -> dict:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    if count != 21 or Path(fields["lane_inputs_dir"]) != FROZEN:
        raise RuntimeError("unexpected charged receipt shape")
    checked = []
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        actual = sha256(FROZEN / name)
        if actual != expected:
            raise RuntimeError(f"charged input mismatch: {name}")
        checked.append((name, actual))
    return {"count": count, "all_match": True, "checked": checked}


def load_endpoint(band):
    stage = json.loads(STAGE7.read_text(encoding="utf-8"))
    nxt = json.loads(NEXT.read_text(encoding="utf-8"))
    free_names = FREE_LIST.read_text(encoding="utf-8").splitlines()
    if not (
        stage["branch"] == "delta52"
        and stage["stage_spec"]["stage"] == 7
        and stage["counts"]["exact_Krull_dimension_localized"] == 869
        and stage["joint_elimination"]["residual_count"] == 0
        and stage["joint_elimination"]["Qstar_pivots"] == 59
        and free_names == stage["unresolved_quotient_generators"]
        and free_names == nxt["unresolved_quotient_generators"]
        and len(free_names) == len(set(free_names)) == 869
    ):
        raise RuntimeError("charged endpoint assertions failed")

    # max_t=33 is the complete normalized H block; outer_state(7) is exactly
    # the charged stage-7 endpoint, not a replay of the parallel stage-8 lane.
    k2, inner_free, major_meta = band.build_major_h2("delta52", 33)
    outer, outer_free, outer_meta = band.outer_state(7)

    symbol_table = {name: sp.Symbol(name) for name in free_names}
    for item in stage["joint_elimination"]["pivot_ledger"]:
        symbol_table.setdefault(item["variable"], sp.Symbol(item["variable"]))
        parsed = sp.sympify(item["rhs"])
        for symbol in parsed.free_symbols:
            symbol_table.setdefault(str(symbol), sp.Symbol(str(symbol)))
    raw_map = {
        sp.Symbol(item["variable"]): sp.sympify(item["rhs"], locals=symbol_table)
        for item in stage["joint_elimination"]["pivot_ledger"]
    }
    joint_map = band.resolve_map(raw_map)
    if len(joint_map) != 59 or any(value != 0 for value in joint_map.values()):
        raise RuntimeError("the charged 59-pivot quotient did not resolve to zero")

    reconstructed = (set(inner_free) | set(outer_free)) - set(joint_map)
    if sorted(map(str, reconstructed)) != free_names:
        raise RuntimeError("reconstructed coordinate list differs from charged list")
    if not (
        outer_meta["D1_cumulative_pivots"] == 176
        and outer_meta["outer_free_count"] == 826
        and major_meta["major_output_free_count"] == 99
    ):
        raise RuntimeError("charged stage-7 block counts changed")

    pieces = {"H": k2}
    for name in ("A2", "A3", "B1", "B2"):
        pieces[name] = band.outer_effective_tz(outer, name, 200)
    allowed = set(map(sp.Symbol, free_names))
    for name, item in pieces.items():
        symbols = set()
        for raw in item.values():
            symbols.update(sp.sympify(raw).xreplace(joint_map).free_symbols)
        unexpected = symbols - allowed
        if unexpected:
            raise RuntimeError(f"{name} has non-quotient symbols: {sorted(map(str, unexpected))}")

    endpoint = {
        "stage7_sha256": sha256(STAGE7),
        "free_list_sha256": sha256(FREE_LIST),
        "next_manifest_sha256": sha256(NEXT),
        "charged_engine_sha256": sha256(CHARGED_ENGINE),
        "free_count": len(free_names),
        "inner_free": major_meta["major_output_free_count"],
        "outer_free_before_joint": outer_meta["outer_free_count"],
        "outer_D1_pivots": outer_meta["D1_cumulative_pivots"],
        "joint_pivots": len(joint_map),
        "joint_all_zero": True,
    }
    return free_names, joint_map, pieces, endpoint


def t3_coefficient_names() -> list[str]:
    names = []
    for i in range(2, 10):
        for m in range((2 * i) // 3 + 1):
            if (i, m) != (9, 6):
                names.append(f"T3_a{i}_m{m}")
    if len(names) != 34:
        raise AssertionError("T3 coefficient family must have 34 members")
    return names


def deterministic_value(name: str, prime: int) -> int:
    """A stable nonzero value; independent of Python's randomized hash."""
    payload = SPECIALIZATION_DOMAIN + str(prime).encode() + b"\0" + name.encode()
    integer = int.from_bytes(hashlib.sha256(payload).digest(), "big")
    return 1 + integer % (prime - 1)


def specialization(names: Iterable[str], prime: int) -> dict[str, int]:
    if prime not in PRIMES:
        raise ValueError(f"unsupported prime {prime}")
    name_list = list(names)
    values = {name: deterministic_value(name, prime) for name in name_list}
    if len(values) != len(name_list):
        raise RuntimeError("duplicate specialization names")
    return values


def specialization_hash(values: dict[str, int]) -> str:
    canonical = "".join(f"{name}={values[name]}\n" for name in sorted(values))
    return hashlib.sha256(canonical.encode()).hexdigest()


def modular_evaluator(prime: int, values: dict[str, int]):
    @lru_cache(maxsize=None)
    def evaluate(raw: sp.Expr) -> int:
        expr = sp.sympify(raw)
        if expr.is_Integer:
            return int(expr) % prime
        if expr.is_Rational:
            denominator = int(expr.q) % prime
            if denominator == 0:
                raise ZeroDivisionError(f"denominator {expr.q} vanishes modulo {prime}")
            return (int(expr.p) % prime) * pow(denominator, -1, prime) % prime
        if expr.is_Symbol:
            try:
                return values[str(expr)]
            except KeyError as exc:
                raise KeyError(f"unspecialized symbol {expr}") from exc
        if expr.is_Add:
            return sum(evaluate(arg) for arg in expr.args) % prime
        if expr.is_Mul:
            product = 1
            for arg in expr.args:
                product = product * evaluate(arg) % prime
            return product
        if expr.is_Pow and expr.exp.is_Integer:
            exponent = int(expr.exp)
            base = evaluate(expr.base)
            if exponent < 0:
                if base == 0:
                    raise ZeroDivisionError("negative power of zero in modular evaluation")
                return pow(pow(base, -1, prime), -exponent, prime)
            return pow(base, exponent, prime)
        raise TypeError(f"unsupported SymPy coefficient node: {type(expr).__name__}: {expr}")

    return evaluate


def source_summary(item) -> dict:
    retained = [(r, q) for r, q in item if 2 * r <= CAP]
    return {
        "tz_terms_total": len(item),
        "tz_terms_retained": len(retained),
        "r_min": min((r for r, _q in retained), default=None),
        "r_max": max((r for r, _q in retained), default=None),
        "q_min": min((q for _r, q in retained), default=None),
        "q_max": max((q for _r, q in retained), default=None),
    }


def component_statements(name: str, item, joint_map, evaluate, chunk: int = 128) -> list[str]:
    terms = []
    for (r, q), raw in sorted(item.items()):
        if 2 * r > CAP:
            continue
        coefficient = evaluate(sp.sympify(raw).xreplace(joint_map))
        if coefficient:
            terms.append(f"{coefficient}*s^{2*r}*zp{q}")
    statements = [f"poly {name}=0;"]
    for start in range(0, len(terms), chunk):
        statements.append(f"{name}=trunc({name}+" + "+".join(terms[start : start + chunk]) + ");")
    statements.append(f'supportMarker("{name}",{name});')
    return statements


def support_procedure() -> str:
    return r'''
proc supportMarker(string tag, poly f)
{
  int count=size(f);
  if(f==0)
  {
    print("SUPPORT tag="+tag+" terms=0 s_min=NA s_max=NA pi_min=NA pi_max=NA");
  }
  else
  {
    poly cursor=f;
    int smin=CAPPLUSONE;
    int smax=-1;
    int pimin=CAPPLUSONE;
    int pimax=-1;
    intvec exponent;
    while(cursor!=0)
    {
      exponent=leadexp(cursor);
      if(exponent[1]<smin) { smin=exponent[1]; }
      if(exponent[1]>smax) { smax=exponent[1]; }
      if(exponent[2]<pimin) { pimin=exponent[2]; }
      if(exponent[2]>pimax) { pimax=exponent[2]; }
      cursor=cursor-lead(cursor);
    }
    print("SUPPORT tag="+tag+" terms="+string(count)+" s_min="+string(smin)+" s_max="+string(smax)+" pi_min="+string(pimin)+" pi_max="+string(pimax));
  }
}

proc sJet(poly f, int bound)
{
  poly answer=0;
  poly cursor=f;
  intvec exponent;
  while(cursor!=0)
  {
    exponent=leadexp(cursor);
    if(exponent[1]<=bound) { answer=answer+lead(cursor); }
    cursor=cursor-lead(cursor);
  }
  return(answer);
}
'''.replace("CAPPLUSONE", str(CAP + 1))


def emit_one(prime: int, free_names, joint_map, pieces, endpoint, output: Path) -> dict:
    t2_names = ["T2_a1", "T2_a0", "T2_b1", "T2_b0"]
    t3_names = t3_coefficient_names()
    all_names = list(free_names) + t2_names + t3_names
    if len(all_names) != 907 or len(set(all_names)) != 907:
        raise RuntimeError("expected 869 chart plus 38 T coordinates")
    values = specialization(all_names, prime)
    evaluate = modular_evaluator(prime, values)
    max_q = max(q for item in pieces.values() for _r, q in item)

    components = []
    for name in ("H", "A2", "A3", "B1", "B2"):
        components.extend(component_statements(name, pieces[name], joint_map, evaluate))

    z_powers = []
    for q in range(1, max_q + 1):
        z_powers.append(f"poly zp{q}=trunc(zp{q-1}*zeta);")

    alpha_terms = []
    for i in range(2, 10):
        for m in range((2 * i) // 3 + 1):
            if (i, m) == (9, 6):
                continue
            shift = 132 * i - 198 * m
            if shift < 0:
                raise AssertionError("negative normalized T3 shift")
            coefficient = values[f"T3_a{i}_m{m}"]
            alpha_terms.append(f"U3=trunc(U3+{coefficient}*s^{shift}*F{m}*G{9-i});")
    if len(alpha_terms) != 34:
        raise AssertionError("wrong number of specialized T3 columns")

    c_value = values["c"]
    u_value = values["u"]
    v_value = values["v"]
    inv2, inv4, inv5 = (pow(number, -1, prime) for number in (2, 4, 5))
    q1_c8 = (3 * c_value * inv4) % prime
    q1_c6 = (-c_value * c_value) % prime
    q1_c4 = (c_value * c_value % prime) * c_value % prime * inv2 % prime
    q1_c10 = (-inv5) % prime

    provenance = "\n".join(
        [
            "// COMPLETE[STAGE7-DETERMINISTIC-SPECIALIZATION]",
            "// probe_kind=support/nonzero-row only; no rank, pivots, or chart Groebner basis",
            f"// generator_sha256={sha256(Path(__file__))}",
            f"// stage7_sha256={endpoint['stage7_sha256']}",
            f"// free_list_sha256={endpoint['free_list_sha256']}",
            f"// next_manifest_sha256={endpoint['next_manifest_sha256']}",
            f"// charged_engine_sha256={endpoint['charged_engine_sha256']}",
            f"// characteristic={prime}",
            f"// specialization_domain={SPECIALIZATION_DOMAIN.rstrip(chr(0).encode()).decode()}",
            f"// specialization_sha256={specialization_hash(values)}",
            "// specialized_coordinates=907 (869 chart + 4 T2 + 34 T3), all nonzero",
            "// normalization=KF=t^99 F, KG=t^66 G, t=s^2",
            "// minor=z=-1+u*s^4+v*s^6+pi*s^7",
            "// target_T2=s^391*(pi*(pi^2-c))^5",
            "// target_T3=s^1178*(pi*(pi^2-c))^10*q1; normalized_J=1",
            "// q1=-pi^10/5+3*c*pi^8/4-c^2*pi^6+c^3*pi^4/2 (zero constant)",
        ]
    )

    script = f'''{provenance}
ring R={prime},(s,pi),dp;
ideal Truncation=s^{CAP + 1};
qring Q=std(Truncation); // only the one-monomial bookkeeping quotient is standardized
proc trunc(poly f) {{ return(reduce(f,std(0))); }}

{support_procedure()}

poly zp0=1;
poly zeta=-1+{u_value}*s^4+{v_value}*s^6+pi*s^7;
{chr(10).join(z_powers)}

{chr(10).join(components)}

poly H2=trunc(H*H);
poly H3=trunc(H2*H);
poly H4=trunc(H2*H2);
poly EF=trunc(A2*H+A3);
poly EG=trunc(B1*H+B2);
poly F0=1;
poly F1=trunc(H3+EF);
poly F2=trunc(F1*F1);
poly F3=trunc(F2*F1);
poly F4=trunc(F3*F1);
poly F5=trunc(F4*F1);
poly G0=1;
poly G1=trunc(H2+EG);
poly G2=trunc(G1*G1);
poly G3=trunc(G2*G1);
poly G4=trunc(G3*G1);
poly G5=trunc(G4*G1);
poly G6=trunc(G5*G1);
poly G7=trunc(G6*G1);
poly EG2=trunc(EG*EG);
poly EG3=trunc(EG2*EG);
poly EF2=trunc(EF*EF);

// Structural cancellation of H^6: D2=G^3-F^2 without forming either face.
poly D2=trunc(3*H4*EG+3*H2*EG2+EG3-2*H3*EF-EF2);
poly U2=trunc(D2+{values['T2_a1']}*s^66*F1*G1+{values['T2_a0']}*s^264*G1+{values['T2_b1']}*s^198*F1+{values['T2_b0']}*s^396);

// Structural cancellation of H^18: G^9-F^6=D2*(G^6+G^3*F^2+F^4).
poly D3=trunc(D2*(G6+G3*F2+F4));
poly U3=D3;
{chr(10).join(alpha_terms)}

poly pbase=pi*(pi^2-{c_value});
poly q1={q1_c10}*pi^10+{q1_c8}*pi^8+{q1_c6}*pi^6+{q1_c4}*pi^4;
if(subst(q1,pi,0)!=0) {{ ERROR("q1 does not have zero constant"); }}
if(diff(q1,pi)+2*pbase^3!=0) {{ ERROR("q1 derivative identity failed"); }}

// E2 and E3 contain precisely the sampled coefficient-by-coefficient rows.
poly E2=sJet(U2,{T2_CAP})-s^{T2_CAP}*pbase^5;
poly E3=sJet(U3,{CAP})-s^{CAP}*pbase^10*q1;

print("BEGIN_MODULAR_SUPPORT prime={prime} cap={CAP} normalized_J=1 chart_rank_or_gb=0");
supportMarker("F",F1);
supportMarker("G",G1);
supportMarker("D2_monic",D2);
supportMarker("U2_full_mod_s1179",U2);
supportMarker("T2_residual_rows_s_le_391",E2);
supportMarker("D3_monic",D3);
supportMarker("U3_full_mod_s1179",U3);
supportMarker("T3_residual_rows_s_le_1178",E3);
print("END_MODULAR_SUPPORT prime={prime}");
quit;
'''
    encoded = script.encode()
    if len(encoded) > 128 * 1024 * 1024:
        raise RuntimeError("refusing unexpectedly large support script (>128 MiB)")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(encoded)
    return {
        "prime": prime,
        "path": str(output),
        "bytes": len(encoded),
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "specialization_sha256": specialization_hash(values),
        "specialized_coordinate_count": len(values),
        "all_specialized_values_nonzero": all(values.values()),
        "c": c_value,
        "u": u_value,
        "v": v_value,
        "max_z_power": max_q,
    }


def self_check() -> dict:
    t3_names = t3_coefficient_names()
    shifts = {
        name: 132 * i - 198 * m
        for i in range(2, 10)
        for m in range((2 * i) // 3 + 1)
        if (i, m) != (9, 6)
        for name in [f"T3_a{i}_m{m}"]
    }
    if min(shifts.values()) < 0 or len(shifts) != 34:
        raise AssertionError("bad T3 shifts")
    samples = {
        str(prime): {
            "name_count_checked": 38,
            "all_nonzero": all(
                deterministic_value(name, prime) != 0
                for name in ["T2_a1", "T2_a0", "T2_b1", "T2_b0"] + t3_names
            ),
        }
        for prime in PRIMES
    }
    return {
        "status": "COMPLETE[LIGHTWEIGHT-SELF-CHECK]",
        "primes": list(PRIMES),
        "cap": CAP,
        "T2_cap": T2_CAP,
        "T2_coefficients": 4,
        "T3_coefficients": len(t3_names),
        "T3_shift_min": min(shifts.values()),
        "T3_shift_max": max(shifts.values()),
        "specialization_samples": samples,
        "note": "does not reconstruct or emit; safe pre-review check only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true", help="cheap combinatorial check; no endpoint reconstruction")
    parser.add_argument("--prime", type=int, choices=PRIMES, action="append",
                        help="prime(s) to emit; default emits all three")
    parser.add_argument("--output-dir", type=Path, default=HERE / "modular-support")
    args = parser.parse_args()
    if args.self_check:
        print(json.dumps(self_check(), indent=2, sort_keys=True))
        return

    custody = verify_frozen()
    band = load_charged_module()
    free_names, joint_map, pieces, endpoint = load_endpoint(band)
    selected = tuple(dict.fromkeys(args.prime or PRIMES))
    emitted = []
    for prime in selected:
        output = args.output_dir / f"t3-support-p{prime}.sing"
        emitted.append(emit_one(prime, free_names, joint_map, pieces, endpoint, output))
    result = {
        "status": "COMPLETE[MODULAR-SUPPORT-SCRIPTS-EMITTED]",
        "probe_kind": "support/nonzero-row only; never rank or chart Groebner basis",
        "custody": {"count": custody["count"], "all_match": custody["all_match"]},
        "endpoint": endpoint,
        "normalization": {
            "KF": "t^99 F",
            "KG": "t^66 G",
            "t": "s^2",
            "minor": "z=-1+u*s^4+v*s^6+pi*s^7",
            "quotient": "s^1179=0",
            "pi_cap": None,
            "T2_target": "s^391*p^5",
            "T3_target": "s^1178*p^10*q1",
            "p": "pi*(pi^2-c)",
            "q1": "-pi^10/5+3*c*pi^8/4-c^2*pi^6+c^3*pi^4/2",
            "q1_constant": 0,
            "jacobian_convention": "literal normalized J=1 (no kappa variable)",
        },
        "source_support": {name: source_summary(item) for name, item in pieces.items()},
        "emitted": emitted,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.output_dir / "manifest.json"
    manifest.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
