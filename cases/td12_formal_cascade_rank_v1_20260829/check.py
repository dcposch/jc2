#!/usr/bin/env python3
"""Exact stdlib controls for TD12-FORMAL-CASCADE-RANK/v1.

No CAS and no floating point.  Polynomials are coefficient lists over Q,
low degree first.  `require` is deliberately a real function so `python -O`
executes the same checks.
"""

from fractions import Fraction as Q
from hashlib import sha256
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [Q(0)]


def zero():
    return [Q(0)]


def is_zero(a):
    return len(trim(a)) == 1 and trim(a)[0] == 0


def add(a, b):
    n = max(len(a), len(b))
    out = [Q(0)] * n
    for j in range(n):
        out[j] = (a[j] if j < len(a) else 0) + (b[j] if j < len(b) else 0)
    return trim(out)


def neg(a):
    return trim([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def scale(c, a):
    return trim([Q(c) * x for x in a])


def mul(a, b):
    if is_zero(a) or is_zero(b):
        return zero()
    out = [Q(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return trim(out)


def power(a, n):
    require(n >= 0, "negative polynomial power")
    out = [Q(1)]
    base = trim(a)
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def deriv(a):
    if len(a) <= 1:
        return zero()
    return trim([Q(j) * a[j] for j in range(1, len(a))])


def monomial(n, c=1):
    require(n >= 0, "negative monomial degree")
    return [Q(0)] * n + [Q(c)]


def degree(a):
    a = trim(a)
    return -1 if is_zero(a) else len(a) - 1


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    require(not is_zero(b), "division by zero polynomial")
    if degree(a) < degree(b):
        return zero(), a
    q = [Q(0)] * (degree(a) - degree(b) + 1)
    r = list(a)
    db = degree(b)
    lb = b[-1]
    while not is_zero(r) and degree(r) >= db:
        d = degree(r) - db
        c = r[-1] / lb
        q[d] += c
        r = sub(r, mul(monomial(d, c), b))
    return trim(q), trim(r)


def exact_div(a, b, label):
    q, r = divmod_poly(a, b)
    require(is_zero(r), "nonexact division: " + label)
    return q


def linear(root):
    return [Q(-root), Q(1)]


def poly_from_roots(roots, mults):
    out = [Q(1)]
    for root, mult in zip(roots, mults):
        out = mul(out, power(linear(root), mult))
    return out


def rank_q(rows):
    a = [list(map(Q, row)) for row in rows]
    if not a:
        return 0
    nr = len(a)
    nc = len(a[0])
    pivot_row = 0
    for col in range(nc):
        pivot = next((r for r in range(pivot_row, nr) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        z = a[pivot_row][col]
        a[pivot_row] = [x / z for x in a[pivot_row]]
        for r in range(nr):
            if r != pivot_row and a[r][col] != 0:
                z = a[r][col]
                a[r] = [x - z * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nr:
            break
    return pivot_row


def route_data(name, roots, mults, nu):
    p = poly_from_roots(roots, mults)
    radical = poly_from_roots(roots, [1] * len(roots))
    repeated = exact_div(p, radical, name + ": p/rad")
    jac = exact_div(deriv(p), repeated, name + ": p'/gcd")
    return {
        "name": name,
        "roots": list(map(Q, roots)),
        "mults": list(mults),
        "nu": nu,
        "M": sum(mults),
        "q": len(roots),
        "p": p,
        "rad": radical,
        "rep": repeated,
        "jac": jac,
    }


def floor_poly(route, i, s):
    require(i >= s >= 1, "floor theorem requires 1 <= s <= i")
    return poly_from_roots(route["roots"], [m * i - s for m in route["mults"]])


def quotient_operator(route, i, s, rpoly):
    nu = route["nu"]
    M = route["M"]
    e = (-M * s) % nu
    require(0 < e < nu, "weight residue must be nonzero in the gate window")
    floor = floor_poly(route, i, s)
    u = zero()
    for root, mult in zip(route["roots"], route["mults"]):
        h = mult * i - s
        rad_over = exact_div(route["rad"], linear(root), route["name"] + ": rad/linear")
        u = add(u, scale(h, rad_over))
    c = add(
        add(scale(e, route["rad"]), scale(nu, mul(monomial(1), u))),
        scale(-(nu * i - s), mul(monomial(1), route["jac"])),
    )
    return add(scale(nu, mul(mul(monomial(1), route["rad"]), deriv(rpoly))), mul(c, rpoly))


def raw_operator_factor_check(route, i, s, rpoly):
    nu = route["nu"]
    M = route["M"]
    e = (-M * s) % nu
    floor = floor_poly(route, i, s)
    inside = add(
        scale(e, mul(floor, rpoly)),
        scale(nu, mul(monomial(1), add(mul(deriv(floor), rpoly), mul(floor, deriv(rpoly))))),
    )
    raw = sub(
        mul(route["p"], inside),
        scale(nu * i - s, mul(monomial(1), mul(deriv(route["p"]), mul(floor, rpoly)))),
    )
    factored = mul(mul(floor, route["rep"]), quotient_operator(route, i, s, rpoly))
    require(raw == factored, route["name"] + ": root-floor factorization failed")


def matrix_case(route, i, s, cap):
    qroots = route["q"]
    cols = [quotient_operator(route, i, s, monomial(n)) for n in range(cap + 1)]
    nominal_degree = cap + qroots
    matrix = []
    for row in range(nominal_degree + 1):
        matrix.append([col[row] if row < len(col) else Q(0) for col in cols])
    rank = rank_q(matrix)
    sharp_degree = max(degree(col) for col in cols)
    e = (-route["M"] * s) % route["nu"]
    h = (route["M"] * s + e) // route["nu"]
    resonance = qroots * s - h
    require(rank == cap + 1, route["name"] + ": unexpected kernel")
    require(nominal_degree + 1 - rank == qroots, route["name"] + ": nominal cokernel")
    expected_sharp = qroots - 1 if cap == resonance else qroots
    require(sharp_degree + 1 - rank == expected_sharp, route["name"] + ": sharp cokernel")
    expected_degree = cap + qroots - (1 if cap == resonance else 0)
    require(sharp_degree == expected_degree, route["name"] + ": sharp degree")
    raw_operator_factor_check(route, i, s, add(monomial(cap), [Q(1)]))
    return rank, qroots, expected_sharp, resonance


def wscale(c, x):
    return x[0], scale(c, x[1])


def wadd(x, y, label):
    require(x[0] == y[0], label + ": weight mismatch")
    return x[0], add(x[1], y[1])


def wsub(x, y, label):
    return wadd(x, wscale(-1, y), label)


def wmul(x, y, nu):
    total = x[0] + y[0]
    residue = total % nu
    tshift = total // nu
    return residue, mul(monomial(tshift), mul(x[1], y[1]))


def wderiv(x, nu):
    e, h = x
    if e:
        return e - 1, add(scale(e, h), scale(nu, mul(monomial(1), deriv(h))))
    return nu - 1, scale(nu, deriv(h))


def tiny_order_two_control(route, i=6):
    """One exact nonzero level-1 jet and its binomial order-2 response.

    This is a sample/control, not the proof of the general binomial lift.
    Weighted t-polynomials avoid large sparse eta expansions.
    """
    require(i >= 2 and i % 2 == 0, "typed order-two control")
    nu = route["nu"]
    M = route["M"]
    r = 3 * i // 2
    df = nu * i
    dg = nu * r
    e1 = (-M) % nu
    e2 = (-2 * M) % nu
    f1 = floor_poly(route, i, 1)
    f2 = floor_poly(route, i, 2)
    r1 = [Q(2), Q(1)]
    p1 = (e1, mul(f1, r1))
    g1 = (e1, scale(Q(3, 2), mul(power(route["p"], r - i), p1[1])))

    k2 = wsub(
        wscale(df - 1, wmul(p1, wderiv(g1, nu), nu)),
        wscale(dg - 1, wmul(wderiv(p1, nu), g1, nu)),
        route["name"] + ": K2",
    )

    carry = (2 * e1 - e2) // nu
    require(2 * e1 == e2 + carry * nu, route["name"] + ": order-two carry")
    f1sq_over_pi = exact_div(power(f1, 2), power(route["p"], i), route["name"] + ": F1^2/p^i")
    require(f1sq_over_pi == f2, route["name"] + ": order-two floor identity")
    z2 = (e2, scale(Q(3, 8), mul(monomial(carry), mul(f2, power(r1, 2)))))

    p_weight = (0, route["p"])
    pprime_weight = wderiv(p_weight, nu)
    lz = wsub(
        wscale(df, wmul(p_weight, wderiv(z2, nu), nu)),
        wscale(i * (df - 2), wmul(pprime_weight, z2, nu)),
        route["name"] + ": L2",
    )
    full_left = wmul((0, power(route["p"], r - 1)), lz, nu)
    require(full_left[0] == k2[0], route["name"] + ": order-two output residue")
    require(full_left[1] == neg(k2[1]), route["name"] + ": order-two binomial solve")
    return True


def run_route(route):
    i = 30
    windows = list(range(1, route["nu"]))
    matrix_cases = 0
    endpoint_orders = [s for s in windows if route["M"] * s < route["nu"]]
    natural_sharp = [route["q"] - 1 if s in endpoint_orders else route["q"] for s in windows]
    boundary = max(endpoint_orders)
    sample_orders = sorted({1, boundary, boundary + 1, route["nu"] - 1})
    for s in sample_orders:
        e = (-route["M"] * s) % route["nu"]
        h = (route["M"] * s + e) // route["nu"]
        nstar = route["q"] * s - h
        nnat = route["q"] * s - 1
        caps = {nstar, nnat}
        for cap in sorted(caps):
            _, _, _, resonance = matrix_case(route, i, s, cap)
            matrix_cases += 1
            require(resonance == nstar, route["name"] + ": resonance formula")
        require((nnat == nstar) == (s in endpoint_orders), route["name"] + ": endpoint range")
    order_two_control = tiny_order_two_control(route)
    digest_payload = {
        "endpoint_orders": endpoint_orders,
        "natural_sharp": natural_sharp,
    }
    digest = sha256(json.dumps(digest_payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "nu": route["nu"],
        "M": route["M"],
        "distinct_roots": route["q"],
        "nominal_cokernel": route["q"],
        "endpoint_resonance_orders": endpoint_orders,
        "natural_sharp_cokernel": natural_sharp,
        "matrix_cases": matrix_cases,
        "order_two_binomial_control": order_two_control,
        "table_sha256": digest,
    }


def main():
    b = route_data("B", [1, 2], [2, 1], 25)
    sibling = route_data("S", [1, 2, 3], [2, 1, 1], 17)
    result = {
        "B": run_route(b),
        "S": run_route(sibling),
        "status": "TD12_FORMAL_CASCADE_RANK_V1_OK",
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
