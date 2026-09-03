#!/usr/bin/env python3
"""Coefficient-array form of the symbolic-t Laurent/Euler terminal family.

This is a finite-field evaluator, intended for formula controls rather than a
characteristic-zero ideal certificate.  All polynomial operations are written
as indexed convolutions.  In particular, the code contains no fixed-t CAS
elimination order hidden inside the definition of T_{t,k}.
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import random

def inv(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        raise ZeroDivisionError("zero finite-field denominator")
    return pow(value, -1, prime)


def divide(numerator: int, denominator: int, prime: int) -> int:
    return numerator % prime * inv(denominator, prime) % prime


def convolution(left: list[int], right: list[int], degree: int,
                prime: int) -> int:
    return sum(left[index] * right[degree-index]
               for index in range(degree + 1)
               if index < len(left) and degree-index < len(right)) % prime


def derivative(array: list[int], prime: int) -> list[int]:
    return [(index + 1) * array[index + 1] % prime
            for index in range(len(array) - 1)]


def shift_to_l(coefficients: dict[int, int], b4: int, maximum: int,
               prime: int) -> list[int]:
    answer = [0] * (maximum + 1)
    for exponent, coefficient in coefficients.items():
        for degree in range(exponent + 1):
            answer[degree] += (coefficient * math.comb(exponent, degree)
                               * pow(b4, exponent-degree, prime))
            answer[degree] %= prime
    return answer


def closed_pivot(t: int, weight: int, y: int, prime: int) -> int:
    q, e = 2*t + 1, 3*t + 1
    d = (2*q*y-(t+1)) % prime
    if weight < t:
        j = weight
        aa = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j
              +72*t**3+144*t*t+88*t+16)
        bb = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j
              -12*t**3-20*t*t-8*t)
        return divide(3*t*e*(aa*d+bb),
                      (t+1)*(3*t+2)**3*(4*t-2*j+1), prime)
    if weight <= 2*t:
        j = weight
        aa = 12*t*t+16*t+4-j*(3*t+4)
        bb = 2*(t+1)*(j-t)
        return divide(-3*t*e*(q-j)*(aa*d+bb),
                      (t+1)*q*(3*t+2)**2*(4*t-2*j+1), prime)
    g = (divide(e*t*y, q*q, prime)
         - divide(e*t*(t+1), 6*q**3, prime)) % prime
    return divide(g*d, 2*y, prime)


def l_arrays(t: int, prime: int, y: int, b3: int, b4: int,
             residual: dict[int, int], solved_c: dict[int, int],
             solved_u: dict[int, int], b2: int) -> tuple[list[int], list[int]]:
    """Return R=-E in the L and X bases for the current high variables."""
    q, e, top = 2*t + 1, 3*t + 1, 4*t + 1
    g = (divide(e*t*y, q*q, prime)
         - divide(e*t*(t+1), 6*q**3, prime)) % prime
    ux = {q: 1}
    for index in range(2, 2*t + 1):
        ux[q-index] = (residual.get(index, 0)
                       if index < t else solved_u.get(index, 0)) % prime
    cx = {t-1: 1}
    for index in range(1, t):
        cx[t-1-index] = solved_c.get(index, 0) % prime
    uu = shift_to_l(ux, b4, q, prime)
    cc = shift_to_l(cx, b4, t-1, prime)

    bb = [0] * (t + 1)  # the integration constant is immaterial; choose B_0=0
    for degree in range(t):
        bb[degree+1] = divide(g*(3*degree+5)*cc[degree],
                              2*y*(degree+1), prime)

    ss = [0] * (2*t + 1)
    for degree in range(2*t + 1):
        value = 3*g*(degree+1)*(uu[degree+1] if degree+1 < len(uu) else 0)
        for aa in range(t):
            bb_index = degree-1-aa
            if 0 <= bb_index < len(bb):
                value += (3+2*aa-bb_index)*cc[aa]*bb[bb_index]
        if degree < len(cc):
            value += divide(g*b3*(5*degree+7)*cc[degree], 2, prime)
        ss[degree] = divide(value, y*(2*degree+1), prime)

    vv = [0] * (t + 2)
    vv[0] = -y*b3 % prime
    for degree in range(2, t + 2):
        vv[degree] = cc[degree-2]
    yy = [0] * (2*t + 2)
    yy[0] = -g*b2 % prime
    for degree in range(1, len(yy)):
        yy[degree] = ss[degree-1]
    for degree in range(min(len(yy), len(bb))):
        yy[degree] = (yy[degree]-b3*bb[degree]) % prime
    zz = [0] * (t + 2)
    zz[0] = -g*b3 % prime
    for degree in range(1, len(zz)):
        zz[degree] = bb[degree-1] if degree-1 < len(bb) else 0

    vp, yp, up = derivative(vv, prime), derivative(yy, prime), derivative(uu, prime)
    nn = [0] * (e + 1)
    for degree in range(e + 1):
        nn[degree] = (-convolution(vv, yp, degree, prime)
                      + convolution(vp, yy, degree, prime)
                      + 2*convolution(up, zz, degree, prime)) % prime
    pp = [divide(nn[degree+1], 2*y, prime) for degree in range(e)]
    rr = [0] * (top + 1)
    for degree in range(top + 1):
        rr[degree] = (convolution(vv, pp, degree, prime)
                      - convolution(up, yy, degree, prime)) % prime
    rr[0] = (rr[0]-y*g) % prime

    rx = [0] * (top + 1)
    for degree in range(top + 1):
        rx[degree] = sum(
            math.comb(higher, degree) * pow(-b4, higher-degree, prime)
            * rr[higher]
            for higher in range(degree, top + 1)
        ) % prime
    return rr, rx


def terminal_values(t: int, prime: int, y: int, b3: int, b4: int,
                    residual: dict[int, int]) -> tuple[list[int], list[dict[str, int]]]:
    q, top = 2*t + 1, 4*t + 1
    h_value = (12*q*q*y*y-12*q*(t+1)*y+(t+1)*(3*t+2)) % prime
    if h_value:
        raise ValueError("y is not on H_t")
    solved_c: dict[int, int] = {}
    solved_u: dict[int, int] = {}
    b2 = 0
    pivots: list[dict[str, int]] = []
    for weight in range(1, 2*t + 2):
        def band_at(value: int) -> int:
            trial_c, trial_u, trial_b2 = dict(solved_c), dict(solved_u), b2
            if weight < t:
                trial_c[weight] = value
            elif weight <= 2*t:
                trial_u[weight] = value
            else:
                trial_b2 = value
            return l_arrays(t, prime, y, b3, b4, residual, trial_c,
                            trial_u, trial_b2)[1][top-weight]

        rho = band_at(0)
        measured = (band_at(1)-rho) % prime
        expected = closed_pivot(t, weight, y, prime)
        if measured != expected:
            raise AssertionError(("pivot mismatch", t, weight, measured, expected))
        value = -rho*inv(measured, prime) % prime
        if weight < t:
            solved_c[weight] = value
            variable = f"C{weight}"
        elif weight <= 2*t:
            solved_u[weight] = value
            variable = f"q{weight}_0"
        else:
            b2 = value
            variable = "b2"
        pivots.append({"weight": weight, "variable": variable,
                       "coefficient": measured, "value": value})
    _rl, rx = l_arrays(t, prime, y, b3, b4, residual, solved_c, solved_u, b2)
    if any(rx[degree] for degree in range(2*t, top + 1)):
        raise AssertionError("nonzero high band after recurrence")
    # R=-E; return the sign T=[X^k]E used in the question.
    return [(-rx[degree]) % prime for degree in range(2*t)], pivots


def roots(t: int, prime: int) -> list[int]:
    q = 2*t + 1
    return [value for value in range(prime)
            if (12*q*q*value*value-12*q*(t+1)*value
                +(t+1)*(3*t+2)) % prime == 0]


def evaluate_record(record: dict[str, object], point: dict[str, int],
                    prime: int) -> list[int]:
    answer = []
    for item in record["terminal"]:  # type: ignore[index]
        # The records are receipt/bank authenticated arithmetic expressions
        # containing only integer literals and the declared point variables.
        # Evaluating after substituting Python integers is far cheaper than
        # constructing the million-byte t=6 SymPy expression tree.
        value = eval(str(item["expr"]), {"__builtins__": {}}, dict(point))
        answer.append(int(value) % prime)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, nargs="*", default=list(range(2, 7)))
    parser.add_argument("--prime", type=int, default=1009)
    parser.add_argument("--points", type=int, default=3)
    parser.add_argument("--records", type=pathlib.Path)
    parser.add_argument("--seed", type=int, default=160903)
    args = parser.parse_args()
    randomizer = random.Random(args.seed)
    summary: list[dict[str, object]] = []
    for t in args.t:
        fibre_roots = roots(t, args.prime)
        if len(fibre_roots) != 2:
            raise RuntimeError(f"expected two roots for t={t}: {fibre_roots}")
        for branch, y in enumerate(fibre_roots):
            record = None
            if args.records is not None:
                path = args.records / f"terminal_mod_t{t}_p{args.prime}_branch{branch}.json"
                if path.exists():
                    record = json.loads(path.read_text(encoding="utf-8"))
                    if int(record["y"]) != y:
                        raise RuntimeError(f"record/root mismatch: {path}")
            digests = []
            for _point_index in range(args.points):
                b3, b4 = randomizer.randrange(args.prime), randomizer.randrange(args.prime)
                residual = {index: randomizer.randrange(args.prime)
                            for index in range(2, t)}
                values, pivots = terminal_values(t, args.prime, y, b3, b4, residual)
                if record is not None:
                    point = {"b3": b3, "b4": b4,
                             **{f"q{i}_0": residual[i] for i in residual}}
                    stored_r = evaluate_record(record, point, args.prime)
                    if values != [(-value) % args.prime for value in stored_r]:
                        raise AssertionError(("terminal mismatch", t, branch))
                digests.append(sum((index+1)*value for index, value in enumerate(values))
                               % args.prime)
                if any(pivot["coefficient"] == 0 for pivot in pivots):
                    raise AssertionError("zero pivot")
            status = "PASS_RECORD" if record is not None else "PASS_FORMULA"
            item = {"t": t, "prime": args.prime, "branch": branch, "y": y,
                    "points": args.points, "status": status, "value_digests": digests}
            summary.append(item)
            print(json.dumps(item, sort_keys=True))
    print(json.dumps({"status": "ALL_PASS", "checks": len(summary)}, sort_keys=True))


if __name__ == "__main__":
    main()
