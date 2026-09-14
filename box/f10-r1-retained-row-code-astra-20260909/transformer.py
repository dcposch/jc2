"""UNEXECUTED. Exact retained-row substitution only; no solving or factorization.
argv: transformer.py AUTHORITY ORIGINAL.json RETAINED.json
Mathematical work is inside transform(), called only after unchanged authority.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

SOURCE_SHA = "168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576"
NAMES = ["u", "ell", "d0", "v0", "v1", "k1", "k2", "k3", "s", "S", "t", "v"]
OLD_NAMES = ["u", "ell", "d0", "d1", "v0", "v1", "v2", "k1", "k2", "k3", "k4", "omega"]


def transform(data):
    from fractions import Fraction as Q
    from math import factorial, gcd

    def need(ok, why):
        if not ok:
            raise ValueError(why)

    def no_float(x):
        need(type(x) is not float, "floating point forbidden")
        if isinstance(x, (list, dict)):
            for y in (x.values() if isinstance(x, dict) else x):
                no_float(y)

    no_float(data)
    need(data["schema"] == "F10-L1-EXACT/v1" and data["variables"] == OLD_NAMES, "original schema/variables")
    need(data["gauges"] == {"k0": 0, "beta": 0, "gamma": 0}, "gauges")

    # Dense Q[v] is used ONLY for fixed p and its three named unit inverses.
    def trim(a):
        a = list(a)
        while a and not a[-1]:
            a.pop()
        return a

    def plus(a, b):
        return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                     for i in range(max(len(a), len(b)))])

    def times(a, b):
        c = [Q(0)] * max(0, len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x * y
        return trim(c)

    def scale(a, c):
        return trim([x * c for x in a])

    def divide(a, b):
        need(bool(b), "zero Q[v] divisor")
        a = trim(a); out = [Q(0)] * max(0, len(a) - len(b) + 1)
        while a and len(a) >= len(b):
            k = len(a) - len(b); c = a[-1] / b[-1]; out[k] += c
            a = plus(a, [Q(0)] * k + scale(b, -c))
        return trim(out), a

    E = list(map(Q, [39, -360, 960, -512]))
    L = list(map(Q, [25, -144, 192]))
    R = list(map(Q, [-195, 2016, -6720, 7168]))
    modulus = plus(plus(scale(times(R, R), 24), times([Q(280), Q(-1344)], times(L, R))),
                   scale(times(E, times(L, L)), 49))
    need(len(modulus) == 8, "modulus degree")
    monic = scale(modulus, 1 / modulus[-1])

    def red(a):
        return divide(a, monic)[1]

    def inv(a):
        r0, r1, t0, t1 = monic, red(a), [], [Q(1)]
        while r1:
            q, r2 = divide(r0, r1)
            r0, r1, t0, t1 = r1, r2, t1, plus(t0, scale(times(q, t1), -1))
        need(len(r0) == 1 and r0[0] != 0, "named element is not a unit in product algebra")
        answer = red(scale(t0, 1 / r0[0]))
        need(red(times(a, answer)) == [Q(1)], "unit identity")
        return answer

    Linv = inv(L)
    w = red(scale(times(R, Linv), Q(1, 112)))
    winv = inv(w)
    # Literal finite partition formula, exponent7/4; no arbitrary coefficient inversion.
    fall = [Q(1)]
    for i in range(5):
        fall.append(fall[-1] * (Q(7, 4) - i))
    f5 = []
    for l in range(2):
        for j in range(3):
            i = 5 - 2 * j - 3 * l
            if i < 0:
                continue
            term = [Q(0)] * j + [fall[i + j + l] / (factorial(i) * factorial(j) * factorial(l))]
            if l:
                term = times(term, w)
            f5 = red(plus(f5, term))
    f5inv = inv(f5)
    origin = (0,) * 12

    def atom(axis, degree=1):
        e = list(origin); e[axis] = degree
        return {tuple(e): Q(1)}

    def scalar(c):
        return {origin: Q(c)} if c else {}

    def embed(a):
        return {origin[:-1] + (i,): c for i, c in enumerate(a) if c}

    def add(*polys):
        out = {}
        for poly in polys:
            for e, c in poly.items():
                out[e] = out.get(e, Q(0)) + c
        return {e: c for e, c in out.items() if c}

    def mul(a, b):
        groups = {}
        for e, c in a.items():
            for f, d in b.items():
                key = tuple(x + y for x, y in zip(e, f))
                g = groups.setdefault(key[:-1], {})
                g[key[-1]] = g.get(key[-1], Q(0)) + c * d
        out = {}
        for e, group in groups.items():
            values = [group.get(i, Q(0)) for i in range(max(group) + 1)]
            for i, c in enumerate(red(values)):
                if c:
                    out[e + (i,)] = c
        return out

    def power(a, n):
        need(type(n) is int and n >= 0, "power outside polynomial input")
        out = scalar(1)
        while n:
            if n & 1:
                out = mul(out, a)
            n //= 2
            if n:
                a = mul(a, a)
        return out

    low = [atom(i) for i in range(8)]
    F = mul(embed(red(times([Q(0), Q(1)], winv))), atom(8, -1))
    H = mul(embed(winv), atom(8, -2))
    a = mul(embed(winv), atom(8, -3))
    omega = mul(embed(red(times(w, f5))), atom(8, 8))
    mapping = [low[0], low[1], low[2], F, low[3], low[4], H,
               low[5], low[6], low[7], a, omega, atom(9)]

    def read_old(wire, width):
        out = {}; previous = None
        for entry in wire:
            need(type(entry) is list and len(entry) == 3, "input wire entry")
            e, n, d = entry
            need(type(e) is list and len(e) == width and all(type(i) is int and i >= 0 for i in e), "input exponents")
            key = tuple(e)
            need(previous is None or previous < key, "input ordering")
            previous = key
            need(type(n) is str and type(d) is str, "input rational strings")
            num, den = int(n), int(d)
            need(str(num) == n and str(den) == d and num and den > 0 and gcd(abs(num), den) == 1, "input canonical rational")
            out[key] = Q(num, den)
        return out

    cache = {}
    def sub(wire, width):
        answer = {}
        for e, c in read_old(wire, width).items():
            term = scalar(c)
            for axis, degree in enumerate(e):
                if degree:
                    key = (axis, degree)
                    if key not in cache:
                        cache[key] = power(mapping[axis], degree)
                    term = mul(term, cache[key])
            answer = add(answer, term)
        return [[list(e), str(c.numerator), str(c.denominator)] for e, c in sorted(answer.items())]

    def dense(a):
        return [[str(c.numerator), str(c.denominator)] for c in a]

    ids = ["E1/S" + str(i) for i in range(9)] + ["E0/S" + str(i) for i in range(10)] + ["GUARD/omega*a*b-1"]
    need([r["id"] for r in data["rows"]] == ids, "all original slots")
    zeros = {"E1/S8", "E0/S9", "GUARD/omega*a*b-1"}
    rows = [{"id": row["id"], "S_degree": row["S_degree"], "polynomial": sub(row["polynomial"], 12),
             "status": "IDENTICALLY-ZERO" if row["id"] in zeros else "RETAINED"} for row in data["rows"]]
    need(all(not row["polynomial"] for row in rows if row["id"] in zeros), "top/guard did not vanish")
    out = {"schema": "F10-R1-RETAINED/v1", "source_sha256": SOURCE_SHA, "variables": NAMES,
           "coefficient_format": "sorted width12 rational-string monomials; s exponent signed; v exponent0..6",
           "modulus": dense(modulus), "units": {name: dense(value) for name, value in
           (("L", L), ("Linv", Linv), ("w", w), ("winv", winv), ("f5", f5), ("f5inv", f5inv))},
           "mapping": [sub([[list((0,) * i + (1,) + (0,) * (11 - i)), "1", "1"]], 12) for i in range(12)],
           "A": [sub(x, 13) for x in data["A"]], "B": [sub(x, 13) for x in data["B"]],
           "coefficient_slots": {label: [[sub(x, 12) for x in slots] for slots in data["coefficient_slots"][label]] for label in ("A", "B")},
           "forcing": {key: sub(value, 13) for key, value in data["forcing"].items()},
           "residuals": {key: sub(value, 13) for key, value in data["residuals"].items()},
           "restoration": {key: sub(data["restoration"][key], 13) for key in ("a", "b", "guard")},
           "rows": rows, "retained_ids": [row["id"] for row in rows if row["status"] == "RETAINED"],
           "gauges": data["gauges"], "resonances": data["resonances"],
           "jacobian_slot_map": data["jacobian_slot_map"], "pole_slots": data["pole_slots"]}
    return out


def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: transformer.py AUTHORITY ORIGINAL RETAINED; registered AWS only")
    custody = authorize(sys.argv[1], __file__, "build")
    import hashlib
    import json
    spec = json.loads(Path(sys.argv[1]).read_text())
    source = Path(sys.argv[2]).resolve(strict=True)
    if spec["file_sha256"].get(str(source)) != SOURCE_SHA:
        raise RuntimeError("original artifact pin missing")
    raw = source.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SOURCE_SHA:
        raise RuntimeError("original artifact changed")
    result = transform(json.loads(raw))
    result["execution"] = custody
    result["implementation_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with open(sys.argv[3], "x", encoding="utf-8") as output:
        json.dump(result, output, sort_keys=True, separators=(",", ":"), allow_nan=False)
        output.write("\n")
    print("EMITTED-REPRESENTATION-ONLY; NO IDEAL DECISION")


if __name__ == "__main__":
    main()
