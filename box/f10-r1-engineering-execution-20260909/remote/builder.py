"""UNEXECUTED exact L_1 builder. No solver, CAS, primes, or source powers.

Run only through registered CAPRUN on the specific authorized AWS instance.
Example argv shape: builder.py AUTHORITY.json OUTPUT.json
All mathematical imports/work occur after the metadata launch gate.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize


def build():
    from fractions import Fraction
    names = ["u", "ell", "d0", "d1", "v0", "v1", "v2", "k1", "k2", "k3", "k4", "omega"]
    width = 13                         # twelve parameters, then S
    zero = (0,) * width

    def scalar(value):
        return {zero: Fraction(value)} if value else {}

    def var(index):
        e = list(zero); e[index] = 1
        return {tuple(e): Fraction(1)}

    def add(*polys):
        out = {}
        for poly in polys:
            for e, c in poly.items():
                out[e] = out.get(e, Fraction(0)) + c
                if not out[e]:
                    del out[e]
        return out

    def scale(poly, c):
        return {e: v * c for e, v in poly.items() if v * c}

    def mul(a, b):
        out = {}
        for e, c in a.items():
            for f, d in b.items():
                key = tuple(x + y for x, y in zip(e, f))
                out[key] = out.get(key, Fraction(0)) + c * d
                if not out[key]:
                    del out[key]
        return out

    def ds(poly):
        out = {}
        for e, c in poly.items():
            if e[-1]:
                f = list(e); f[-1] -= 1
                out[tuple(f)] = c * e[-1]
        return out

    def coeff(poly, degree):
        return {e[:-1]: c for e, c in poly.items() if e[-1] == degree}

    def wire(poly):
        return [[list(e), str(c.numerator), str(c.denominator)] for e, c in sorted(poly.items())]

    u, ell, d0, d1, v0, v1, v2, k1, k2, k3, k4, omega, S = [var(i) for i in range(width)]
    S2 = mul(S, S); S3 = mul(S2, S); S4 = mul(S3, S)
    d = add(d0, mul(d1, S))
    v = add(v0, mul(v1, S), mul(v2, S2))
    k = add(mul(k1, S), mul(k2, S2), mul(k3, S3), mul(k4, S4))
    f = add(mul(S, d), scale(u, -1))
    h = add(scalar(1), scale(mul(u, d), -1), mul(S, v))
    A = [k, h, f, S]
    delta = [scalar(1), u, scale(ell, -1), add(mul(ell, u), scalar(-1)),
             add(scale(u, 2), scale(mul(ell, S), -1)),
             add(scale(mul(u, u), -1), scale(S, -2)), scale(mul(u, S), 2), scale(S2, -1)]
    B = [{}, {}, {}, {}, {}, S2, {}, {}]
    forcing = {}
    resonance = {}
    for j in (4, 3, 2, 1, 0):
        Q = add(delta[j + 2], scale(mul(ds(f), B[j + 1]), -(j + 1)),
                scale(mul(f, ds(B[j + 1])), 2),
                scale(mul(ds(h), B[j + 2]), -(j + 2)), mul(h, ds(B[j + 2])),
                scale(mul(ds(k), B[j + 3]), -(j + 3)))
        forcing[str(j)] = wire(Q)
        out = {}
        for e, c in Q.items():
            divisor = j - 3 * e[-1]
            if divisor == 0:
                raise RuntimeError("nonzero resonance forcing; refuse incomplete presentation")
            if e[-1] > 7 - j:
                raise RuntimeError("forcing escaped source envelope")
            out[e] = c / divisor
        B[j] = out                  # beta=gamma=0, including absent resonant slots
        if j in (3, 0):
            resonance[str(j)] = {"S_degree": 1 if j == 3 else 0, "forcing": [], "gauge": []}
    E1 = add(scale(mul(ds(k), B[2]), 2), mul(ds(h), B[1]),
             scale(mul(h, ds(B[1])), -1), scale(mul(f, ds(B[0])), -2), scale(u, -1))
    E0 = add(mul(ds(k), B[1]), scale(mul(h, ds(B[0])), -1), scalar(-1))
    a = k4
    b = {e[:-1] + (0,): c for e, c in B[0].items() if e[-1] == 7}
    guard = add(mul(omega, mul(a, b)), scalar(-1))
    rows = []
    for label, poly, bound in (("E1", E1, 8), ("E0", E0, 9)):
        if any(e[-1] > bound for e in poly):
            raise RuntimeError("residual escaped fixed row envelope")
        for i in range(bound + 1):
            rows.append({"id": label + "/S" + str(i), "S_degree": i, "polynomial": wire(coeff(poly, i))})
    rows.append({"id": "GUARD/omega*a*b-1", "S_degree": None, "polynomial": wire(coeff(guard, 0))})
    return {"schema": "F10-L1-EXACT/v1", "variables": names, "coefficient_coordinate": "S",
            "r": 1, "m": 4, "n": 7, "gauges": {"k0": 0, "beta": 0, "gamma": 0},
            "coefficient_format": "sorted [nonnegative exponent vector, numerator-string, positive denominator-string]; zero=[]",
            "A": [wire(p) for p in A], "B": [wire(p) for p in B[:6]],
            "coefficient_slots": {
                "A": [[wire(coeff(poly, i)) for i in range(5 - j)] for j, poly in enumerate(A)],
                "B": [[wire(coeff(poly, i)) for i in range(8 - j)] for j, poly in enumerate(B[:6])]},
            "jacobian_slot_map": [
                {"t_degree": h, "S_degree": i,
                 "row": ("E" + str(h) + "/S" + str(i)) if h < 2 else "ELIMINATED-ZERO"}
                for h in range(8) for i in range(10 - h)],
            "forcing": forcing, "resonances": resonance,
            "residuals": {"E1": wire(E1), "E0": wire(E0)}, "rows": rows,
            "restoration": {"a": wire(a), "b": wire(b), "guard": wire(guard),
                            "A_original": "A/a", "B_original": "B/b", "c_original": "1/(a*b)",
                            "eta_original": "a*b", "inverse_a_mod_guard": "omega*b", "inverse_b_mod_guard": "omega*a"},
            "pole_slots": {"A": [[-3, 0], [-2, 0], [-1, 0]],
                           "B": [[-5, 0], [-4, 0], [-3, 0], [-2, 0], [-2, 1], [-1, 0], [-1, 1]]}}


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: builder.py AUTHORITY.json OUTPUT.json (registered AWS only)")
    custody = authorize(sys.argv[1], __file__, "build")
    import json
    result = build()
    result["execution"] = custody
    # Direct Python integer/string JSON bytes; never JS-number round trips.
    with open(sys.argv[2], "x", encoding="utf-8") as stream:
        json.dump(result, stream, sort_keys=True, separators=(",", ":"), allow_nan=False)
        stream.write("\n")
    print("BUILT exact artifact; NOT a decision or point")


if __name__ == "__main__":
    main()
