"""UNEXECUTED independent full-condition verifier, not an ideal decision.

Does not import builder or use its Euler recursion. Rebuilds the complete
two-coordinate determinant and the inverse Laurent substitution from wires.
checker.py AUTHORITY.json ARTIFACT.json RECEIPT.json MODE
MODE: full, u-zero, dropped-constant, upper-coefficient, guard, leading-top,
      u-zero-dropped-constant. All modes require their own registered argv.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize


class InvalidArtifact(Exception):
    pass


def verify(data, u_zero=False, low=True):
    from fractions import Fraction
    from math import gcd
    N = 14                           # parameters, S (or p), t (or z)
    origin = (0,) * N
    expected_names = ["u", "ell", "d0", "d1", "v0", "v1", "v2", "k1", "k2", "k3", "k4", "omega"]

    def demand(condition, message):
        if not condition:
            raise InvalidArtifact(message)

    def no_floats(obj):
        demand(not isinstance(obj, float), "floating point anywhere in artifact")
        if isinstance(obj, list):
            for item in obj:
                no_floats(item)
        if isinstance(obj, dict):
            for item in obj.values():
                no_floats(item)

    no_floats(data)
    demand(data["schema"] == "F10-L1-EXACT/v1", "schema")
    demand(data["variables"] == expected_names, "variable order")
    demand((data["r"], data["m"], data["n"]) == (1, 4, 7), "r/m/n")
    demand(data["coefficient_coordinate"] == "S", "coordinate")
    demand(data["gauges"] == {"k0": 0, "beta": 0, "gamma": 0}, "gauge declaration")

    def read(wire, width=13):
        demand(isinstance(wire, list), "wire not list")
        answer = {}
        previous = None
        for term in wire:
            demand(isinstance(term, list) and len(term) == 3, "term shape")
            exponents, numerator, denominator = term
            demand(isinstance(exponents, list) and len(exponents) == width, "exponent width")
            demand(all(type(x) is int and x >= 0 for x in exponents), "exponents not nonnegative integers")
            key = tuple(exponents)
            demand(previous is None or previous < key, "unsorted/duplicate monomial")
            previous = key
            demand(type(numerator) is str and type(denominator) is str, "rational not strings")
            num, den = int(numerator), int(denominator)
            demand(str(num) == numerator and str(den) == denominator, "noncanonical integer strings")
            demand(num != 0 and den > 0 and gcd(abs(num), den) == 1, "noncanonical rational")
            if not (u_zero and key[0]):
                answer[key + (0,) * (N - width)] = Fraction(num, den)
        return answer

    def literal(value):
        return {origin: Fraction(value)} if value else {}

    def atom(axis):
        if axis == 0 and u_zero:
            return {}
        e = list(origin); e[axis] = 1
        return {tuple(e): Fraction(1)}

    def combine(*arguments):
        accum = {}
        for poly in arguments:
            for monomial, coefficient in poly.items():
                accum[monomial] = accum.get(monomial, 0) + coefficient
        return {e: c for e, c in accum.items() if c}

    def times(left, right):
        accum = {}
        for a, ca in left.items():
            for b, cb in right.items():
                e = tuple(a[i] + b[i] for i in range(N))
                accum[e] = accum.get(e, 0) + ca * cb
        return {e: c for e, c in accum.items() if c}

    def number(poly, factor):
        return {e: c * factor for e, c in poly.items() if c * factor}

    def power(poly, exponent):
        result = literal(1)
        for unused in range(exponent):
            result = times(result, poly)
        return result

    def derivative(poly, axis):
        result = {}
        for e, c in poly.items():
            if e[axis]:
                target = list(e); target[axis] -= 1
                result[tuple(target)] = c * e[axis]
        return result

    def projection(poly, axis, degree):
        result = {}
        for e, c in poly.items():
            if e[axis] == degree:
                target = list(e); target[axis] = 0
                result[tuple(target)] = c
        return result

    u, ell, d0, d1, v0, v1, v2, k1, k2, k3, k4, omega, S, t = [atom(i) for i in range(N)]
    d = combine(d0, times(d1, S))
    v = combine(v0, times(v1, S), times(v2, power(S, 2)))
    k = combine(times(k1, S), times(k2, power(S, 2)), times(k3, power(S, 3)), times(k4, power(S, 4)))
    expected_A = [k, combine(literal(1), number(times(u, d), -1), times(S, v)),
                  combine(times(S, d), number(u, -1)), S]
    demand(len(data["A"]) == 4 and len(data["B"]) == 6, "coefficient list length")
    A = [read(item) for item in data["A"]]
    B = [read(item) for item in data["B"]]
    demand(A == expected_A, "A parameterization differs from complete cubic module")
    demand(B[5] == power(S, 2), "upper B coefficient")
    for label, coefficients, degree in (("A", A, 4), ("B", B, 7)):
        mapped = data["coefficient_slots"][label]
        demand(len(mapped) == len(coefficients), "coefficient slot-list length")
        for index, poly in enumerate(coefficients):
            demand(all(e[12] <= degree - index and e[13] == 0 for e in poly), label + " envelope")
            demand(len(mapped[index]) == degree - index + 1, "zero coefficient slot omitted")
            for s_degree, saved_slot in enumerate(mapped[index]):
                demand(read(saved_slot, 12) == projection(poly, 12, s_degree), "coefficient slot serialization")
    demand(not projection(A[0], 12, 0), "k0 gauge")
    demand(not projection(B[0], 12, 0), "gamma gauge")
    demand(not projection(B[3], 12, 1), "beta gauge")
    AA = combine(*(times(poly, power(t, i)) for i, poly in enumerate(A)))
    BB = combine(*(times(poly, power(t, i)) for i, poly in enumerate(B)))
    jacobian = combine(times(derivative(AA, 12), derivative(BB, 13)),
                       number(times(derivative(AA, 13), derivative(BB, 12)), -1))
    Pi = combine(t, number(times(u, power(t, 2)), -1), times(S, power(t, 3)))
    Delta = combine(literal(1), times(u, t), number(times(ell, times(t, Pi)), -1),
                    number(times(t, times(Pi, Pi)), -1))
    difference = combine(jacobian, number(Delta, -1))
    expected_jacobian_map = [{"t_degree": h, "S_degree": i,
                              "row": ("E" + str(h) + "/S" + str(i)) if h < 2 else "ELIMINATED-ZERO"}
                             for h in range(8) for i in range(10 - h)]
    demand(data["jacobian_slot_map"] == expected_jacobian_map, "full Jacobian zero-slot mapping")
    demand(all(e[13] <= 7 for e in difference), "unexpected t degree")
    for degree in range(2, 8):
        demand(not projection(difference, 13, degree), "nonzero full upper bracket t" + str(degree))
    # Check saved forcings by removing the diagonal term from the independently
    # computed full determinant, not by reimplementing the producer recurrence.
    demand(set(data["forcing"]) == {"0", "1", "2", "3", "4"}, "forcing IDs")
    for index in range(5):
        diagonal = combine(number(B[index], index), number(times(S, derivative(B[index], 12)), -3))
        rest = combine(projection(jacobian, 13, index + 2), number(diagonal, -1))
        expected_forcing = combine(projection(Delta, 13, index + 2), number(rest, -1))
        demand(read(data["forcing"][str(index)]) == expected_forcing, "forcing serialization")
    demand(data["resonances"] == {"3": {"S_degree": 1, "forcing": [], "gauge": []},
                                   "0": {"S_degree": 0, "forcing": [], "gauge": []}}, "resonance mapping")
    rows = data["rows"]
    expected_ids = ["E1/S" + str(i) for i in range(9)] + ["E0/S" + str(i) for i in range(10)] + ["GUARD/omega*a*b-1"]
    demand([row["id"] for row in rows] == expected_ids, "every row including zero slots must be present")
    position = 0
    for label, t_degree, bound in (("E1", 1, 8), ("E0", 0, 9)):
        actual = projection(difference, 13, t_degree)
        demand(all(e[12] <= bound for e in actual), "low bracket escaped row envelope")
        saved = read(data["residuals"][label])
        if low:
            demand(saved == actual, "full low bracket " + label)
        for degree in range(bound + 1):
            row = rows[position]; position += 1
            demand(row["S_degree"] == degree, "row coordinate mapping")
            demand(read(row["polynomial"], 12) == projection(saved, 12, degree), "residual-to-row serialization")
    # Independent direct negative-power test, no module quotient formulas.
    # For a t^k S^i term, i>=k can never create a negative z power because
    # S=p*z^3-z^2+u*z has z-order at least one, also when u=0.
    p, z = atom(12), atom(13)
    inverse_S = combine(times(p, power(z, 3)), number(power(z, 2), -1), times(u, z))
    expected_slots = {"A": [[-3, 0], [-2, 0], [-1, 0]],
                      "B": [[-5, 0], [-4, 0], [-3, 0], [-2, 0], [-2, 1], [-1, 0], [-1, 1]]}
    demand(data["pole_slots"] == expected_slots, "all ten inverse slots")
    for label, coefficients in (("A", A), ("B", B)):
        negative = {}
        for t_degree, poly in enumerate(coefficients):
            for e, coefficient in poly.items():
                s_degree = e[12]
                if s_degree >= t_degree:
                    continue
                base = list(e); base[12] = 0; base[13] = -t_degree
                contribution = times({tuple(base): coefficient}, power(inverse_S, s_degree))
                negative = combine(negative, {a: b for a, b in contribution.items() if a[13] < 0})
        demand(all([e[13], e[12]] in expected_slots[label] for e in negative), "unmapped inverse pole")
        for z_degree, p_degree in expected_slots[label]:
            slot = projection(projection(negative, 13, z_degree), 12, p_degree)
            demand(not slot, label + " inverse pole " + str([z_degree, p_degree]))
    restored = data["restoration"]
    a = projection(A[0], 12, 4); b = projection(B[0], 12, 7)
    demand(a == k4 and bool(b), "leading coefficient restoration")
    demand(read(restored["a"]) == a and read(restored["b"]) == b, "saved leading coefficient restoration")
    guard = combine(times(omega, times(a, b)), literal(-1))
    demand(read(restored["guard"]) == guard, "guard restoration")
    demand(rows[-1]["S_degree"] is None and read(rows[-1]["polynomial"], 12) == guard, "full guard row")
    descriptions = {"A_original": "A/a", "B_original": "B/b", "c_original": "1/(a*b)",
                    "eta_original": "a*b", "inverse_a_mod_guard": "omega*b", "inverse_b_mod_guard": "omega*a"}
    demand(all(restored[key] == val for key, val in descriptions.items()), "normalization map")
    # [A/a,B/b]-Delta/(ab)=(full difference)/(ab); all coefficients
    # are parameter constants. Monic tops are exactly a/a and b/b.
    # Guard supplies both inverses; no field point or zero residual asserted.
    return {"full_bracket_slots": 8, "inverse_pole_slots": 10, "ideal_slots": len(rows),
            "u_zero": u_zero, "low_rows_checked": low,
            "B_term_counts": [len(poly) for poly in B],
            "row_term_counts": [len(read(row["polynomial"], 12)) for row in rows],
            "row_parameter_degrees": [max((sum(e[:12]) for e in read(row["polynomial"], 12)), default=-1) for row in rows]}


def mutation(data, mode):
    import copy
    changed = copy.deepcopy(data)

    def remove_constant(wire):
        found = [term for term in wire if not any(term[0])]
        if len(found) != 1 or found[0][1:] != ["-1", "1"]:
            raise InvalidArtifact("mutation precondition: exact -1 constant absent")
        wire.remove(found[0])

    if mode in ("dropped-constant", "u-zero-dropped-constant"):
        remove_constant(changed["residuals"]["E0"])
        remove_constant(changed["rows"][9]["polynomial"])
    elif mode == "upper-coefficient":
        # Change the genuine B4 coefficient d0*S^2/2 to 3*d0*S^2/2,
        # with both wires synchronized. Monic B5 remains intact.
        key = [0] * 13; key[2] = 1; key[12] = 2
        terms = [item for item in changed["B"][4] if item[0] == key]
        slots = [item for item in changed["coefficient_slots"]["B"][4][2] if item[0] == key[:12]]
        if len(terms) != 1 or len(slots) != 1 or terms[0][1:] != ["1", "2"] or slots[0][1:] != ["1", "2"]:
            raise InvalidArtifact("upper-coefficient mutation precondition")
        terms[0][1] = "3"; slots[0][1] = "3"
    elif mode == "guard":
        remove_constant(changed["restoration"]["guard"])
        remove_constant(changed["rows"][-1]["polynomial"])
    elif mode == "leading-top":
        changed["restoration"]["a"] = [[[0] * 13, "1", "1"]]
    else:
        raise InvalidArtifact("unknown mutation")
    if changed == data:
        raise InvalidArtifact("mutation changed no payload")
    return changed


def main():
    if len(sys.argv) != 5:
        raise SystemExit("usage: checker.py AUTHORITY ARTIFACT RECEIPT MODE (registered AWS only)")
    custody = authorize(sys.argv[1], __file__, "check")
    import hashlib
    import json
    raw = Path(sys.argv[2]).read_bytes()
    data = json.loads(raw)
    mode = sys.argv[4]
    u_zero = mode in ("u-zero", "u-zero-dropped-constant")
    details = verify(data, u_zero=u_zero)
    result = {"schema": "F10-L1-CHECK/v1", "execution": custody, "mode": mode,
              "artifact_sha256": hashlib.sha256(raw).hexdigest(), "valid_full_artifact": details,
              "verdict": "PASS-REPRESENTATION-NOT-IDEAL-DECISION"}
    if mode not in ("full", "u-zero"):
        changed = mutation(data, mode)
        if mode in ("dropped-constant", "u-zero-dropped-constant"):
            # Actual old-pass/new-fail: upper/J and all poles/guard do not see
            # this deletion, but the complete determinant's constant row does.
            verify(changed, u_zero=u_zero, low=False)
            result["weakened_upper_only_check"] = "PASS"
        try:
            verify(changed, u_zero=u_zero)
        except InvalidArtifact as error:
            result["changed_payload"] = "REJECTED"
            result["rejection"] = str(error)
        else:
            raise InvalidArtifact("changed mathematical payload incorrectly passed")
    with open(sys.argv[3], "x", encoding="utf-8") as output:
        json.dump(result, output, sort_keys=True, separators=(",", ":"), allow_nan=False)
        output.write("\n")
    print(result["verdict"])


if __name__ == "__main__":
    main()
