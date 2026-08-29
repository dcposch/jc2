#!/usr/bin/env python3
"""Exact D5G raw-global determinant compiler and certificate replay."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent

PINS = {
    "preregistration": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/PREREGISTRATION.md",
        "72e8ba988a0aaeccb86f473bf89b66847481c4e645998f5456e2ad0acb803541",
    ),
    "d5_design_freeze": (
        "cases/ggv_8_28_factor_etale_global_e22_gluing_d5_design_20260827/FREEZE.sha256",
        "9954063b99931a37dc7df2bd56e82570d6a2d0f036d995d2a95e19d109cf47ce",
    ),
    "d3_raw": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json",
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    ),
    "d3_freeze": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256",
        "012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022",
    ),
    "m_cokernel_audit": (
        "xmodel/ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md",
        "2803b705d41b332cabd12249b0a0be17cdd18e8f2f251fe7b242bf55fc9bb289",
    ),
    "d4r1_hold_freeze": (
        "cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827/FREEZE.sha256",
        "6beafdb470ec9c4c88fd8c6e3d2ccaf3b4312c477ddabc4576203f7e9c19c954",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qstr(q: Q) -> str:
    return str(Q(q))


def compact(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2) + "\n").encode()


# Sparse C[X]: key is (sorted raw-variable tuple, X degree).
def pclean(p):
    return {key: Q(value) for key, value in p.items() if Q(value)}


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Q(0)) + value
        if not out[key]:
            del out[key]
    return out


def pscale(a, q):
    return pclean({key: Q(q) * value for key, value in a.items()})


def pmul(a, b):
    out = {}
    for (va, xa), ca in a.items():
        for (vb, xb), cb in b.items():
            key = (tuple(sorted(va + vb)), xa + xb)
            out[key] = out.get(key, Q(0)) + ca * cb
    return pclean(out)


def pder(a):
    return pclean({(vars_, xdeg - 1): Q(xdeg) * coeff for (vars_, xdeg), coeff in a.items() if xdeg})


def encode_poly(p):
    return [[list(vars_), xdeg, qstr(p[vars_, xdeg])] for vars_, xdeg in sorted(p)]


def decode_poly(items):
    return pclean({(tuple(vars_), int(xdeg)): Q(coeff) for vars_, xdeg, coeff in items})


H = {((), 0): Q(-1), ((), 8): Q(1)}
F0 = pmul(H, H)
G0 = pmul(F0, H)


def rows_from_source(source, drop_slot=None):
    rows = {"F": {0: F0}, "G": {0: G0}}
    sources = {"F": {0: {((), x): f"F0:X^{x}:{qstr(c)}" for (v, x), c in F0.items()}},
               "G": {0: {((), x): f"G0:X^{x}:{qstr(c)}" for (v, x), c in G0.items()}}}
    for kind in ("F", "G"):
        for slot in source["raw_slots_through_weight_22"][kind]:
            if slot["weight"] == 0 or slot["slot"] == drop_slot:
                continue
            n = slot["weight"]
            xdeg = slot["raw_exponents"]["x"]
            key = ((slot["slot"],), xdeg)
            rows[kind].setdefault(n, {})[key] = Q(1)
            sources[kind].setdefault(n, {})[key] = slot["slot"]
    return rows, sources


def determinant(source, second_offset=-8, drop_slot=None):
    rows, sources = rows_from_source(source, drop_slot=drop_slot)
    all_D = []
    contribution_digests = []
    d22_contributions = []
    total_contributions = 0
    for n in range(23):
        out = {}
        contributions = []
        for i in range(n + 1):
            j = n - i
            Fi = rows["F"].get(i, {})
            Gj = rows["G"].get(j, {})
            for (fv, fx), fc in Fi.items():
                for (gv, gx), gc in Gj.items():
                    raw_vars = tuple(sorted(fv + gv))
                    fsource = sources["F"][i][fv, fx]
                    gsource = sources["G"][j][gv, gx]
                    if fx and 12 - j:
                        coeff = Q(12 - j) * Q(fx) * fc * gc
                        key = (raw_vars, fx + gx - 1)
                        out[key] = out.get(key, Q(0)) + coeff
                        contributions.append([n, i, j, "FX_G", fsource, gsource, key[1], qstr(coeff)])
                    if gx and i + second_offset:
                        coeff = Q(i + second_offset) * Q(gx) * fc * gc
                        key = (raw_vars, fx + gx - 1)
                        out[key] = out.get(key, Q(0)) + coeff
                        contributions.append([n, i, j, "F_GX", fsource, gsource, key[1], qstr(coeff)])
        out = pclean(out)
        encoded = encode_poly(out)
        contribution_bytes = compact(sorted(contributions))
        all_D.append({
            "weight": n,
            "term_count": len(out),
            "terms": encoded,
            "contribution_count": len(contributions),
            "contribution_sha256": hashlib.sha256(contribution_bytes).hexdigest(),
            "contributions": sorted(contributions),
        })
        contribution_digests.append(hashlib.sha256(contribution_bytes).hexdigest())
        total_contributions += len(contributions)
        if n == 22:
            d22_contributions = sorted(contributions)
    return {
        "schema": "GGV-8_28-D5G-DIRECT-DETERMINANT-v2",
        "ring": "C[X], C=Q[400 positive-weight D3 raw slots]",
        "recurrence": "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')",
        "leading_rows": {"F0": encode_poly(F0), "G0": encode_poly(G0)},
        "D": all_D,
        "total_final_terms": sum(item["term_count"] for item in all_D),
        "total_contributions": total_contributions,
        "all_contribution_digests_sha256": hashlib.sha256(compact(contribution_digests)).hexdigest(),
        "D22_contributions": d22_contributions,
    }


def divide_by_H(p):
    work = dict(p)
    quotient = {}
    while work:
        max_degree = max(xdeg for _, xdeg in work)
        if max_degree < 8:
            break
        keys = sorted(key for key in work if key[1] == max_degree)
        for vars_, degree in keys:
            coeff = work.get((vars_, degree), Q(0))
            if not coeff:
                continue
            qkey = (vars_, degree - 8)
            quotient[qkey] = quotient.get(qkey, Q(0)) + coeff
            work[(vars_, degree)] -= coeff
            if not work[(vars_, degree)]:
                del work[(vars_, degree)]
            low = (vars_, degree - 8)
            work[low] = work.get(low, Q(0)) + coeff
            if not work[low]:
                del work[low]
    quotient, remainder = pclean(quotient), pclean(work)
    assert padd(pmul(H, quotient), remainder) == p
    assert not remainder or max(x for _, x in remainder) < 8
    return quotient, remainder


def M_of(y):
    Hp = pder(H)
    return padd(pscale(pmul(H, pder(y)), 4), pscale(pmul(Hp, y), 6))


def reduce_M(p):
    work = dict(p)
    y = {}
    trace = []
    while work:
        max_degree = max(xdeg for _, xdeg in work)
        if max_degree < 7:
            break
        keys = sorted(key for key in work if key[1] == max_degree)
        for vars_, degree in keys:
            coeff = work.get((vars_, degree), Q(0))
            if not coeff:
                continue
            k = degree - 7
            yc = coeff / Q(4 * (degree + 5))
            ykey = (vars_, k)
            y[ykey] = y.get(ykey, Q(0)) + yc
            subtraction = pscale(M_of({ykey: Q(1)}), yc)
            work = padd(work, pscale(subtraction, -1))
            trace.append([list(vars_), degree, qstr(coeff), k, qstr(yc)])
    y, remainder = pclean(y), pclean(work)
    assert padd(M_of(y), remainder) == p
    assert not remainder or max(x for _, x in remainder) < 7
    return y, remainder, trace


def coordinate_vector(remainder):
    vector = []
    for degree in range(7):
        entries = [[list(vars_), qstr(coeff)] for (vars_, xdeg), coeff in sorted(remainder.items()) if xdeg == degree]
        vector.append(entries)
    return vector


def direct_D(direct, n):
    item = direct["D"][n]
    assert item["weight"] == n
    return decode_poly(item["terms"])


# Independent dense Q[X,t]/(t^23) specialization.  This deliberately does
# not call determinant() or its coefficient recurrence.
def utrim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return tuple(p)


def uadd(a, b):
    return utrim([(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(max(len(a), len(b)))])


def uscale(a, q):
    return utrim([Q(q) * x for x in a])


def umul(a, b):
    if not a or not b:
        return ()
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return utrim(out)


def uder(a):
    return utrim([Q(i) * a[i] for i in range(1, len(a))])


def tadd(a, b):
    return [uadd(x, y) for x, y in zip(a, b)]


def tscale(a, q):
    return [uscale(x, q) for x in a]


def tmul(a, b):
    out = [()] * 23
    for n in range(23):
        acc = ()
        for i in range(n + 1):
            acc = uadd(acc, umul(a[i], b[n - i]))
        out[n] = acc
    return out


def tdx(a):
    return [uder(x) for x in a]


def tdt(a):
    return [uscale(a[n + 1], n + 1) if n < 22 else () for n in range(23)]


def tshift(a):
    return [()] + a[:22]


def independent_dense_control(source, direct):
    slots = sorted(
        slot["slot"]
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
        if slot["weight"] > 0
    )
    assert len(slots) == 400 and len(set(slots)) == 400
    assignment = {slot: Q((index % 13) + 1) * (-1 if index % 2 else 1) for index, slot in enumerate(slots)}

    F = [()] * 23
    G = [()] * 23
    for target, fixed in ((F, F0), (G, G0)):
        top = max(x for _, x in fixed)
        dense = [Q(0)] * (top + 1)
        for (_, xdeg), coeff in fixed.items():
            dense[xdeg] += coeff
        target[0] = utrim(dense)
    for kind, target in (("F", F), ("G", G)):
        for slot in source["raw_slots_through_weight_22"][kind]:
            n = slot["weight"]
            if n == 0:
                continue
            xdeg = slot["raw_exponents"]["x"]
            dense = list(target[n]) + [Q(0)] * max(0, xdeg + 1 - len(target[n]))
            dense[xdeg] += assignment[slot["slot"]]
            target[n] = utrim(dense)

    FX, GX, Ft, Gt = tdx(F), tdx(G), tdt(F), tdt(G)
    E = tadd(
        tadd(tscale(tmul(FX, G), 12), tscale(tmul(F, GX), -8)),
        tscale(tshift(tadd(tmul(FX, Gt), tscale(tmul(Ft, GX), -1))), -1),
    )

    direct_numeric = []
    for n in range(23):
        sparse = direct_D(direct, n)
        top = max((xdeg for _, xdeg in sparse), default=-1)
        dense = [Q(0)] * (top + 1)
        for (vars_, xdeg), coeff in sparse.items():
            value = coeff
            for slot in vars_:
                value *= assignment[slot]
            dense[xdeg] += value
        direct_numeric.append(utrim(dense))
    assert E == direct_numeric
    encoded = [[qstr(x) for x in poly] for poly in E]
    return {
        "status": "PASS-INDEPENDENT-DENSE-QXT-SPECIALIZATION",
        "assignment_sha256": hashlib.sha256(compact({slot: qstr(value) for slot, value in assignment.items()})).hexdigest(),
        "E0_through_E22_sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        "nonzero_weight_count": sum(bool(poly) for poly in E),
    }


def build_certificate(direct):
    D22 = direct_D(direct, 22)
    Q22, R22 = divide_by_H(D22)
    Y22, rM22, mtrace = reduce_M(D22)

    mutated = padd(D22, H)
    Qmut, Rmut = divide_by_H(mutated)
    Ymut, rMmut, _ = reduce_M(mutated)
    expected_qmut = padd(Q22, {((), 0): Q(1)})
    assert Qmut == expected_qmut
    assert Rmut == R22
    assert rMmut != rM22

    cert = {
        "schema": "GGV-8_28-D5G-D22-CERTIFICATE-v1",
        "D22": encode_poly(D22),
        "H_division": {"Q22": encode_poly(Q22), "R22": encode_poly(R22), "replay": "D22=H*Q22+R22", "R22_degree_lt": 8},
        "M_reduction": {
            "Y22": encode_poly(Y22),
            "rM22": encode_poly(rM22),
            "seven_vector": coordinate_vector(rM22),
            "trace": mtrace,
            "replay": "D22=M(Y22)+rM22",
            "rM22_degree_lt": 7,
        },
        "H_mutation": {
            "mutated_D22": encode_poly(mutated),
            "Q22_mutated": encode_poly(Qmut),
            "R22_mutated": encode_poly(Rmut),
            "M_preimage_mutated": encode_poly(Ymut),
            "M_remainder_mutated": encode_poly(rMmut),
            "seven_vector_mutated": coordinate_vector(rMmut),
            "R_unchanged": True,
            "Q_increment": "1",
            "M_vector_changed": True,
        },
        "D22_contributions": direct["D22_contributions"],
    }
    return cert


def build_result(source_bytes, direct_bytes, direct, cert_bytes, cert, source):
    observed = {}
    for key, (rel, expected) in PINS.items():
        got = sha256(ROOT / rel)
        assert got == expected, (key, got, expected)
        observed[key] = {"path": rel, "sha256": got}
    assert hashlib.sha256(source_bytes).hexdigest() == PINS["d3_raw"][1]
    expected_direct = determinant(source)
    assert direct_bytes == compact(expected_direct)
    expected_cert = build_certificate(direct)
    assert cert_bytes == compact(expected_cert)
    assert direct_D(direct, 0) == {}

    sign_mutated = determinant(source, second_offset=-7)
    sign_digest = hashlib.sha256(compact(sign_mutated)).hexdigest()
    direct_digest = hashlib.sha256(direct_bytes).hexdigest()
    assert sign_digest != direct_digest

    D22 = direct_D(direct, 22)
    slots = sorted({slot for vars_, _ in D22 for slot in vars_})
    assert slots
    dropped_slot = slots[0]
    dropped = determinant(source, drop_slot=dropped_slot)
    dropped_digest = hashlib.sha256(compact(dropped)).hexdigest()
    assert dropped_digest != direct_digest

    Q22 = decode_poly(cert["H_division"]["Q22"])
    R22 = decode_poly(cert["H_division"]["R22"])
    Y22 = decode_poly(cert["M_reduction"]["Y22"])
    rM22 = decode_poly(cert["M_reduction"]["rM22"])
    assert padd(pmul(H, Q22), R22) == D22
    assert padd(M_of(Y22), rM22) == D22

    return {
        "status": "PASS-D5G-REVIEW-INDEPENDENT-RAW-GLOBAL-DETERMINANT",
        "scope": "literal generic raw determinant D0..D22, exact H division and M reduction; no equations or face verdict",
        "pins": observed,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "direct_artifact_sha256": direct_digest,
        "certificate_artifact_sha256": hashlib.sha256(cert_bytes).hexdigest(),
        "census": {
            "raw_positive_slots": 400,
            "weights": 23,
            "total_final_terms": direct["total_final_terms"],
            "total_contributions": direct["total_contributions"],
            "D22_terms": len(D22),
            "D22_contributions": len(direct["D22_contributions"]),
            "Q22_terms": len(Q22),
            "R22_terms": len(R22),
            "Y22_terms": len(Y22),
            "rM22_terms": len(rM22),
        },
        "exact_replays": {
            "D0": "ZERO",
            "H_division": "PASS: D22=H*Q22+R22, deg R22<8",
            "M_reduction": "PASS: D22=M(Y22)+rM22, deg rM22<7",
            "independent_dense_specialization": independent_dense_control(source, direct),
        },
        "mutations": {
            "add_H": "PASS: R22 unchanged, Q22 increments by 1, M seven-vector changes",
            "drop_raw_slot": {"slot": dropped_slot, "status": "DETERMINANT_DIGEST_CHANGED", "mutated_sha256": dropped_digest},
            "change_i_minus_8_to_i_minus_7": {"status": "DETERMINANT_DIGEST_CHANGED", "mutated_sha256": sign_digest},
        },
        "local_naturality_dependency": {
            "status": "LOCKED_PENDING_D4R1_FRESH_HOSTILE_REVIEW",
            "d4r1_bytes_pinned_as_hold_only": PINS["d4r1_hold_freeze"][1],
            "consumed": False,
        },
        "target_status": "NO_TARGET_VERDICT; D0..D21 are generic expressions and are not assumed zero",
        "claims_not_made": ["Keller specialization", "R22=1", "Q22=0", "local/global naturality PASS", "8_28 face/family exclusion", "G2-PSC", "G2-BD", "JC2"],
    }


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--write-direct":
        source_path, out_path = Path(sys.argv[2]), Path(sys.argv[3])
        source_bytes = source_path.read_bytes()
        assert hashlib.sha256(source_bytes).hexdigest() == PINS["d3_raw"][1]
        out_path.write_bytes(compact(determinant(json.loads(source_bytes))))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 4 and sys.argv[1] == "--write-certificate":
        direct_path, out_path = Path(sys.argv[2]), Path(sys.argv[3])
        direct = json.loads(direct_path.read_bytes())
        out_path.write_bytes(compact(build_certificate(direct)))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 5 and sys.argv[1] == "--print-result":
        source_path, direct_path, cert_path = map(Path, sys.argv[2:])
        source_bytes, direct_bytes, cert_bytes = source_path.read_bytes(), direct_path.read_bytes(), cert_path.read_bytes()
        result = build_result(source_bytes, direct_bytes, json.loads(direct_bytes), cert_bytes, json.loads(cert_bytes), json.loads(source_bytes))
        print(pretty(result).decode(), end="")
        return
    if len(sys.argv) == 6 and sys.argv[1] == "--write-result":
        source_path, direct_path, cert_path, out_path = map(Path, sys.argv[2:])
        source_bytes, direct_bytes, cert_bytes = source_path.read_bytes(), direct_path.read_bytes(), cert_path.read_bytes()
        result = build_result(source_bytes, direct_bytes, json.loads(direct_bytes), cert_bytes, json.loads(cert_bytes), json.loads(source_bytes))
        out_path.write_bytes(pretty(result))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 6 and sys.argv[1] == "--check":
        source_path, direct_path, cert_path, result_path = map(Path, sys.argv[2:])
        source_bytes = source_path.read_bytes()
        source = json.loads(source_bytes)
        direct_bytes = direct_path.read_bytes()
        direct = json.loads(direct_bytes)
        cert_bytes = cert_path.read_bytes()
        cert = json.loads(cert_bytes)
        assert direct_bytes == compact(determinant(source))
        assert cert_bytes == compact(build_certificate(direct))
        expected = pretty(build_result(source_bytes, direct_bytes, direct, cert_bytes, cert, source))
        assert result_path.read_bytes() == expected
        print("PASS D5G exact raw-global replay")
        return
    raise SystemExit("usage: --write-direct SOURCE OUT | --write-certificate DIRECT OUT | --print-result SOURCE DIRECT CERT | --write-result SOURCE DIRECT CERT OUT | --check SOURCE DIRECT CERT RESULT")


if __name__ == "__main__":
    main()
