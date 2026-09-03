#!/usr/bin/env python3
"""Sparse finite-field audit of the D108/D90 cyclic bottom systems.

This is a reproducible screen, not a characteristic-zero lift.  It uses the
constant-Wronskian coefficients directly, eliminates the denominator
polynomial triangularly, and quotients root dilation by setting the
next-to-leading numerator coefficient to one.  The remaining constant term
is 1/T; the two unit tests detect artifacts from clearing T and points where
the Wronskian constant vanishes.
"""

import argparse
import resource
import subprocess
import time

import sympy as sp


# (numerator exponent, denominator exponent, numerator degree, denominator degree)
CASES = {"108": (3, 2, 7, 10), "90": (5, 3, 8, 13)}


def encode(expr, variables):
    _, integral = sp.Poly(expr, *variables, domain=sp.QQ).clear_denoms()
    return str(integral.as_expr()).replace("**", "^")


def make(case):
    numerator_power, denominator_power, m, n = CASES[case]
    fc = list(sp.symbols("x0:%d" % (m + 1)))
    gc = list(sp.symbols("y0:%d" % (n + 1)))
    T = sp.Symbol("T")
    values = {fc[m]: sp.Integer(1), gc[n]: sp.Integer(1),
              fc[m-1]: sp.Integer(1), fc[0]: 1/T}

    def coefficient(k):
        return sp.expand(sum(
            (numerator_power*i - denominator_power*j - 1) * fc[i] * gc[j]
            for i in range(m + 1) for j in range(n + 1) if i + j == k
        ).subs(values))

    # Coefficients m+n-1,...,m determine g_(n-1),...,g_0 linearly.
    for k in range(m + n - 1, m - 1, -1):
        target = gc[k-m]
        equation = coefficient(k)
        leader = equation.coeff(target)
        values[target] = sp.cancel(-(equation - leader*target) / leader)

    tails = [sp.together(sp.cancel(coefficient(k))).as_numer_denom()[0]
             for k in range(1, m)]
    g0_numerator = sp.together(values[gc[0]]).as_numer_denom()[0]
    variables = [T] + fc[1:m-1]
    return variables, tails, g0_numerator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", choices=sorted(CASES))
    parser.add_argument("--prime", type=int, default=1009)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    generated = time.time()
    variables, tails, g0 = make(args.case)
    names = ",".join(map(str, variables))
    generators = ",".join(encode(expr, variables) for expr in tails)
    g0_encoded = encode(g0, variables)
    script = f"""
ring r={args.prime},({names}),dp;
option(redSB);
ideal I={generators};
timer=1; ideal G=slimgb(I); timer=0;
print("MAIN_DIM"); dim(G);
print("MAIN_VDIM"); vdim(G);
print("MAIN_SIZE"); size(G);
timer=1; ideal GT=slimgb(I+ideal(T)); timer=0;
print("T_ZERO_UNIT_REMAINDER"); reduce(1,GT);
poly g0={g0_encoded};
timer=1; ideal GK=slimgb(I+ideal(g0)); timer=0;
print("G0_ZERO_UNIT_REMAINDER"); reduce(1,GK);
print("G0_ZERO_DIM"); dim(GK);
quit;
"""
    generation_seconds = time.time() - generated
    started = time.time()
    try:
        result = subprocess.run(["Singular", "-q"], input=script, text=True,
                                capture_output=True, timeout=args.timeout,
                                check=False)
        status, output = "DONE", result.stdout + result.stderr
    except subprocess.TimeoutExpired as exc:
        status = "TIMEOUT"
        output = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
    print("CASE=%s PRIME=%d RING=F_p[%s]" % (args.case, args.prime, names))
    print("GEN_SECONDS=%.3f STATUS=%s RUN_SECONDS=%.3f MAXRSS_KB=%d" %
          (generation_seconds, status, time.time() - started,
           resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss))
    print(output)


if __name__ == "__main__":
    main()
