"""UNEXECUTED independent retained representation verifier; not a solver.
argv: checker.py AUTHORITY ORIGINAL.json RETAINED.json RECEIPT.json
No transformer import. Flat rational polynomial arithmetic and long reduction
are separate from producer dense coefficient grouping and Euclidean inversion.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

SOURCE_SHA = "168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576"


def verify(original, data):
    from fractions import Fraction
    from math import gcd
    origin = (0,) * 12
    names = ["u", "ell", "d0", "v0", "v1", "k1", "k2", "k3", "s", "S", "t", "v"]
    old_names = ["u", "ell", "d0", "d1", "v0", "v1", "v2", "k1", "k2", "k3", "k4", "omega"]

    def demand(ok, reason):
        if not ok:
            raise ValueError(reason)

    def exact(num, den):
        demand(type(num) is str and type(den) is str, "rational coefficients must be strings")
        n, d = int(num), int(den)
        demand(str(n) == num and str(d) == den and d > 0 and gcd(abs(n), d) == 1, "noncanonical exact rational")
        return Fraction(n, d)

    def no_float(item):
        demand(type(item) is not float, "floating point forbidden anywhere")
        if isinstance(item, (dict, list)):
            for value in (item.values() if isinstance(item, dict) else item):
                no_float(value)

    no_float(original); no_float(data)
    demand(original["schema"] == "F10-L1-EXACT/v1" and original["variables"] == old_names, "original schema/order")
    demand(data["schema"] == "F10-R1-RETAINED/v1" and data["variables"] == names, "retained schema/order")
    demand(data["source_sha256"] == SOURCE_SHA, "source binding")

    def literal(c):
        return {origin: Fraction(c)} if c else {}

    def atom(axis, degree=1):
        e = list(origin); e[axis] = degree
        return {tuple(e): Fraction(1)}

    def add(*polys):
        out = {}
        for poly in polys:
            for e, c in poly.items():
                out[e] = out.get(e, 0) + c
        return {e: c for e, c in out.items() if c}

    def scale(poly, c):
        return {e: x * c for e, x in poly.items() if x * c}

    def raw_mul(a, b):
        out = {}
        for e, c in a.items():
            for f, d in b.items():
                target = tuple(e[i] + f[i] for i in range(12))
                out[target] = out.get(target, 0) + c * d
        return {e: c for e, c in out.items() if c}

    v = atom(11)
    v2 = raw_mul(v, v); v3 = raw_mul(v2, v)
    E = add(literal(39), scale(v, -360), scale(v2, 960), scale(v3, -512))
    L = add(literal(25), scale(v, -144), scale(v2, 192))
    R = add(literal(-195), scale(v, 2016), scale(v2, -6720), scale(v3, 7168))
    modulus = add(scale(raw_mul(R, R), 24), raw_mul(add(literal(280), scale(v, -1344)), raw_mul(L, R)),
                  scale(raw_mul(E, raw_mul(L, L)), 49))
    lead_key = origin[:-1] + (7,)
    demand(lead_key in modulus and all(e[-1] <= 7 for e in modulus), "exact modulus degree")
    lead = modulus[lead_key]
    lower_modulus = {e[-1]: c / lead for e, c in modulus.items() if e[-1] < 7}

    def normal(poly):
        # Monomial-by-monomial long division by the fixed monic p; no field
        # division inside Q[v]/p, which may be a product of fields.
        out = dict(poly)
        while True:
            bad = [e for e in out if e[-1] >= 7]
            if not bad:
                break
            e = max(bad, key=lambda x: x[-1]); c = out.pop(e)
            for degree, coefficient in lower_modulus.items():
                key = e[:-1] + (e[-1] - 7 + degree,)
                out[key] = out.get(key, 0) - c * coefficient
                if not out[key]:
                    del out[key]
        return {e: c for e, c in out.items() if c}

    def mul(a, b):
        return normal(raw_mul(a, b))

    def power(a, n):
        demand(type(n) is int and n >= 0, "polynomial power domain")
        answer = literal(1)
        for unused in range(n):
            answer = mul(answer, a)
        return answer

    def same(a, b, reason):
        demand(not normal(add(a, scale(b, -1))), reason)

    def dense(wire):
        demand(type(wire) is list, "dense polynomial shape")
        out = {}
        for i, row in enumerate(wire):
            demand(type(row) is list and len(row) == 2, "dense rational shape")
            c = exact(*row)
            if c:
                out[origin[:-1] + (i,)] = c
        demand(not wire or bool(exact(*wire[-1])), "dense trailing zero")
        return out

    def read(wire):
        demand(type(wire) is list, "retained polynomial shape")
        out = {}; previous = None
        for term in wire:
            demand(type(term) is list and len(term) == 3, "term shape")
            e, num, den = term
            demand(type(e) is list and len(e) == 12 and all(type(i) is int for i in e), "exponent type/width")
            demand(all(i >= 0 for axis, i in enumerate(e) if axis != 8) and e[11] < 7, "Laurent/basis exponent domain")
            key = tuple(e)
            demand(previous is None or previous < key, "duplicate/unsorted retained terms")
            previous = key
            c = exact(num, den); demand(bool(c), "explicit zero term")
            out[key] = c
        return out

    # Exact modulus equality, not congruence to an attacker-supplied modulus.
    demand(dense(data["modulus"]) == modulus, "wrong modulus")
    units = {key: dense(value) for key, value in data["units"].items()}
    demand(set(units) == {"L", "Linv", "w", "winv", "f5", "f5inv"}, "named unit inventory")
    demand(all(all(e[-1] < 7 for e in poly) for poly in units.values()), "noncanonical unit basis")
    same(units["L"], L, "L definition")
    same(mul(L, units["Linv"]), literal(1), "L inverse identity")
    same(mul(scale(L, 112), units["w"]), R, "w definition")
    same(mul(units["w"], units["winv"]), literal(1), "w inverse identity")
    w = units["w"]
    # Independent explicit five partitions of [x^5](1+x+v*x^2+w*x^3)^(7/4).
    # (7/4)_5/120 + (7/4)_4*v/6 + (7/4)_3*v^2/2
    #                    + (7/4)_3*w/2 + (7/4)_2*v*w.
    f5 = add(literal(Fraction(-63, 8192)), scale(v, Fraction(35, 512)),
             scale(v2, Fraction(-21, 128)), scale(w, Fraction(-21, 128)),
             scale(mul(v, w), Fraction(21, 16)))
    same(units["f5"], f5, "f5 finite-partition identity")
    same(mul(f5, units["f5inv"]), literal(1), "f5 inverse identity")
    same(add(scale(mul(w, w), 6144), mul(add(literal(640), scale(v, -3072)), w), E), {}, "leading E6 identity")

    low = [atom(i) for i in range(8)]
    F = mul(mul(v, units["winv"]), atom(8, -1))
    H = mul(units["winv"], atom(8, -2)); a = mul(units["winv"], atom(8, -3))
    omega = mul(mul(w, f5), atom(8, 8))
    mapping = [low[0], low[1], low[2], F, low[3], low[4], H,
               low[5], low[6], low[7], a, omega, atom(9)]
    demand(len(data["mapping"]) == 12, "every original parameter mapping")
    for wire, expected in zip(data["mapping"], mapping):
        same(read(wire), expected, "retained scale/parameter mapping")

    def substitute(wire, width):
        accum = {}; previous = None
        for e, num, den in wire:
            demand(type(e) is list and len(e) == width and all(type(i) is int and i >= 0 for i in e), "original exponent domain")
            key = tuple(e)
            demand(previous is None or previous < key, "original ordering")
            previous = key
            c = exact(num, den); demand(bool(c), "original explicit zero")
            term = literal(c)
            for axis in range(width):
                term = mul(term, power(mapping[axis], e[axis]))
            accum = add(accum, term)
        return normal(accum)

    def diff(poly, axis):
        out = {}
        for e, c in poly.items():
            if e[axis]:
                f = list(e); f[axis] -= 1
                out[tuple(f)] = c * e[axis]
        return out

    def coeff(poly, axis, degree):
        out = {}
        for e, c in poly.items():
            if e[axis] == degree:
                f = list(e); f[axis] = 0
                out[tuple(f)] = c
        return out

    u, ell = low[:2]; S, t = atom(9), atom(10)
    d = add(low[2], mul(F, S)); vp = add(low[3], mul(low[4], S), mul(H, power(S, 2)))
    k = add(mul(low[5], S), mul(low[6], power(S, 2)), mul(low[7], power(S, 3)), mul(a, power(S, 4)))
    expected_A = [k, add(literal(1), scale(mul(u, d), -1), mul(S, vp)), add(mul(S, d), scale(u, -1)), S]
    demand(len(data["A"]) == 4 and len(data["B"]) == 6, "coefficient list length")
    A, B = [read(x) for x in data["A"]], [read(x) for x in data["B"]]
    for got, expected in zip(A, expected_A):
        same(got, expected, "full A boundary parameterization")
    same(B[5], power(S, 2), "leading B coefficient")
    for label, polys, degree in (("A", A, 4), ("B", B, 7)):
        slots = data["coefficient_slots"][label]
        demand(len(slots) == len(polys), "coefficient slot-list")
        for i, poly in enumerate(polys):
            same(poly, substitute(original[label][i], 13), "original coefficient substitution")
            demand(all(e[9] <= degree - i and e[10] == 0 for e in poly), "source coefficient envelope")
            demand(len(slots[i]) == degree - i + 1, "zero coefficient slot omitted")
            for j, wire in enumerate(slots[i]):
                same(read(wire), coeff(poly, 9, j), "coefficient slot projection")
                same(read(wire), substitute(original["coefficient_slots"][label][i][j], 12), "original zero-slot substitution")
    demand(data["gauges"] == {"k0": 0, "beta": 0, "gamma": 0}, "gauge declarations")
    demand(not coeff(A[0], 9, 0) and not coeff(B[0], 9, 0) and not coeff(B[3], 9, 1), "actual gauges")
    AA = add(*(mul(poly, power(t, i)) for i, poly in enumerate(A)))
    BB = add(*(mul(poly, power(t, i)) for i, poly in enumerate(B)))
    J = add(mul(diff(AA, 9), diff(BB, 10)), scale(mul(diff(AA, 10), diff(BB, 9)), -1))
    Pi = add(t, scale(mul(u, power(t, 2)), -1), mul(S, power(t, 3)))
    Delta = add(literal(1), mul(u, t), scale(mul(ell, mul(t, Pi)), -1), scale(mul(t, mul(Pi, Pi)), -1))
    residual = normal(add(J, scale(Delta, -1)))
    demand(all(e[10] <= 7 for e in residual), "full bracket degree")
    for h in range(2, 8):
        same(coeff(residual, 10, h), {}, "upper bracket t" + str(h))
    jacmap = [{"t_degree": h, "S_degree": i, "row": ("E" + str(h) + "/S" + str(i)) if h < 2 else "ELIMINATED-ZERO"}
              for h in range(8) for i in range(10 - h)]
    demand(data["jacobian_slot_map"] == jacmap, "entire bracket zero-slot map")
    demand(set(data["forcing"]) == {"0", "1", "2", "3", "4"}, "forcing inventory")
    for j in range(5):
        diag = add(scale(B[j], j), scale(mul(S, diff(B[j], 9)), -3))
        forcing = add(coeff(Delta, 10, j + 2), scale(add(coeff(J, 10, j + 2), scale(diag, -1)), -1))
        same(read(data["forcing"][str(j)]), forcing, "independent full-bracket forcing")
        same(read(data["forcing"][str(j)]), substitute(original["forcing"][str(j)], 13), "original forcing substitution")
    demand(data["resonances"] == {"3": {"S_degree": 1, "forcing": [], "gauge": []}, "0": {"S_degree": 0, "forcing": [], "gauge": []}}, "resonance zero slots")
    ids = ["E1/S" + str(i) for i in range(9)] + ["E0/S" + str(i) for i in range(10)] + ["GUARD/omega*a*b-1"]
    zeros = {"E1/S8", "E0/S9", "GUARD/omega*a*b-1"}
    demand([x["id"] for x in data["rows"]] == ids and [x["id"] for x in original["rows"]] == ids, "all20 original slots")
    demand(data["retained_ids"] == [x for x in ids if x not in zeros], "all17 retained IDs")
    for label, h, bound in (("E1", 1, 8), ("E0", 0, 9)):
        got = coeff(residual, 10, h)
        demand(all(e[9] <= bound for e in got), "full low envelope")
        same(read(data["residuals"][label]), got, "full low bracket " + label)
        same(got, substitute(original["residuals"][label], 13), "original full residual substitution")
    for row, old in zip(data["rows"], original["rows"]):
        demand(row["S_degree"] == old["S_degree"], "row coordinate")
        expected_status = "IDENTICALLY-ZERO" if row["id"] in zeros else "RETAINED"
        demand(row["status"] == expected_status, "row disposition")
        got = read(row["polynomial"])
        same(got, substitute(old["polynomial"], 12), "original row substitution " + row["id"])
        if row["S_degree"] is not None:
            h = 1 if row["id"].startswith("E1/") else 0
            same(got, coeff(coeff(residual, 10, h), 9, row["S_degree"]), "full row coefficient")
        if row["id"] in zeros:
            same(got, {}, "discarded top/guard is not identically zero")
    # Direct inverse substitution; only i<j can contribute a pole.
    poles = {"A": [[-3, 0], [-2, 0], [-1, 0]], "B": [[-5, 0], [-4, 0], [-3, 0], [-2, 0], [-2, 1], [-1, 0], [-1, 1]]}
    demand(data["pole_slots"] == poles, "all ten pole slots")
    pvar, z = atom(9), atom(10)
    inverse_S = add(mul(pvar, power(z, 3)), scale(power(z, 2), -1), mul(u, z))
    for label, polys in (("A", A), ("B", B)):
        negative = {}
        for j, poly in enumerate(polys):
            for e, c in poly.items():
                i = e[9]
                if i >= j:
                    continue
                base = list(e); base[9] = 0; base[10] = -j
                term = mul({tuple(base): c}, power(inverse_S, i))
                negative = add(negative, {key: val for key, val in term.items() if key[10] < 0})
        negative = normal(negative)
        demand(all([e[10], e[9]] in poles[label] for e in negative), "unmapped inverse pole")
        for zdeg, pdeg in poles[label]:
            same(coeff(coeff(negative, 10, zdeg), 9, pdeg), {}, label + " inverse pole")
    atop, btop = coeff(A[0], 9, 4), coeff(B[0], 9, 7)
    binverse = mul(f5, atom(8, 5)); ainverse = mul(w, atom(8, 3))
    same(atop, a, "actual a top")
    same(mul(atop, ainverse), literal(1), "a top restoration")
    same(mul(btop, binverse), literal(1), "b top restoration")
    same(mul(omega, mul(atop, btop)), literal(1), "full guard restoration")
    for key, value in (("a", atop), ("b", btop), ("guard", {})):
        same(read(data["restoration"][key]), value, "saved restoration " + key)
        same(value, substitute(original["restoration"][key], 13), "original restoration substitution")
    # Quantities are measured ONLY when this verifier is subsequently authorized.
    measures = []
    for row, old in zip(data["rows"], original["rows"]):
        poly = read(row["polynomial"])
        measures.append({"id": row["id"], "original_terms": len(old["polynomial"]), "retained_terms": len(poly),
                         "original_max_parameter_degree": max((sum(term[0]) for term in old["polynomial"]), default=-1),
                         "original_max_rational_bits": max((max(abs(int(term[1])).bit_length(), int(term[2]).bit_length()) for term in old["polynomial"]), default=0),
                         "max_lower_degree": max((sum(e[:8]) for e in poly), default=-1),
                         "min_s_exponent": min((e[8] for e in poly), default=None),
                         "max_s_exponent": max((e[8] for e in poly), default=None),
                         "max_v_degree": max((e[11] for e in poly), default=-1),
                         "max_rational_bits": max((max(abs(c.numerator).bit_length(), c.denominator.bit_length()) for c in poly.values()), default=0)})
    return {"verdict": "PASS-REPRESENTATION-NOT-IDEAL-DECISION", "original_slots": 20, "retained_slots": 17,
            "full_bracket_bands": 8, "inverse_pole_slots": 10, "rows": measures}


def main():
    if len(sys.argv) != 5:
        raise SystemExit("usage: checker.py AUTHORITY ORIGINAL RETAINED RECEIPT; registered AWS only")
    custody = authorize(sys.argv[1], __file__, "check")
    import hashlib
    import json
    spec = json.loads(Path(sys.argv[1]).read_text())
    source, retained = Path(sys.argv[2]).resolve(strict=True), Path(sys.argv[3]).resolve(strict=True)
    if spec["file_sha256"].get(str(source)) != SOURCE_SHA or str(retained) not in spec["file_sha256"]:
        raise RuntimeError("both data artifacts must be explicitly registered")
    raw_source, raw_retained = source.read_bytes(), retained.read_bytes()
    if hashlib.sha256(raw_source).hexdigest() != SOURCE_SHA or hashlib.sha256(raw_retained).hexdigest() != spec["file_sha256"][str(retained)]:
        raise RuntimeError("data changed after registration")
    parsed = json.loads(raw_retained)
    producer = str(Path(__file__).with_name("transformer.py").resolve(strict=True))
    if producer not in spec["file_sha256"] or parsed.get("implementation_sha256") != spec["file_sha256"][producer]:
        raise RuntimeError("producer source binding missing or different")
    result = verify(json.loads(raw_source), parsed)
    result.update({"execution": custody, "source_sha256": SOURCE_SHA,
                   "retained_sha256": hashlib.sha256(raw_retained).hexdigest(),
                   "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   "source_bytes": len(raw_source), "retained_bytes": len(raw_retained)})
    with open(sys.argv[4], "x", encoding="utf-8") as output:
        json.dump(result, output, sort_keys=True, separators=(",", ":"), allow_nan=False)
        output.write("\n")
    print(result["verdict"])


if __name__ == "__main__":
    main()
