#!/usr/bin/env python3
"""Exact-Q audit of the cyclic bottom-node constant-Wronskian system.

For a bottom node with z=pi^A, g=pi*G(z), f=F(z), put

    deg G=N=(e*V-1)/A,  deg F=M=d*V/A.

Moh's r=1 equation (in the convention of the frozen bottomode.py) is

    d*f*g' - e*g*f' = kappa,  kappa != 0,

NOT the r>=2 Appendix-I equation with right side c*p.  If

    P(w)=w^M F(1/w), H(w)=w^N G(1/w),

then H is the degree-N truncation of P^(e/d).  Write
P=1+a1*w+...+aM*w^M and P^(e/d)=sum h_j*w^j.  The exact system is

    h_(N+1)=...=h_(N+M-1)=0,  h_(N+M) != 0.

The inequation is implemented by Rabinowitsch, never by a sat() wrapper.
The finite --first stratification is exhaustive over an algebraic closure:
--first r means a1=...=a_(r-1)=0, ar!=0, followed by the root-dilation
normalization ar=1.  The all-zero stratum has h_(N+M)=0 and is excluded.

Cases installed for this lane:
  D108: (d,e,A,M,N)=(2,3,2,7,10), tails h11..h16, invert h17.
  D90 : (d,e,A,M,N)=(3,5,3,8,13), tails h14..h20, invert h21.
"""
import argparse
import resource
import subprocess
import time

import sympy as sp


CASES = {
    "108": (2, 3, 2, 7, 10),
    "90": (3, 5, 3, 8, 13),
}


def power_series_coefficients(d, e, coefficients, upto):
    """Return h_0,...,h_upto of P^(e/d), exactly over Q[a_i]."""
    M = len(coefficients)
    h = [sp.Integer(1)]
    # Coefficients of d*P*H' - e*H*P'=0 give this linear recurrence.
    for n in range(1, upto + 1):
        value = sp.Integer(0)
        for i in range(1, min(M, n) + 1):
            value += (d * (n - i) - e * i) * coefficients[i - 1] * h[n - i]
        h.append(sp.cancel(-value / (d * n)))
    return h


def singular_polynomial(expr, variables):
    polynomial = sp.Poly(sp.cancel(expr), *variables, domain=sp.QQ)
    denominator, integral = polynomial.clear_denoms(convert=True)
    assert denominator != 0
    return str(integral.as_expr()).replace("**", "^")


def make_system(case, first):
    d, e, A, M, N = CASES[case]
    if not 1 <= first <= M:
        raise ValueError("--first must lie in 1..%d" % M)
    aa = list(sp.symbols("a1:%d" % (M + 1)))
    specialized = [sp.Integer(0)] * (first - 1) + [sp.Integer(1)] + aa[first:]
    variables = aa[first:]
    h = power_series_coefficients(d, e, specialized, M + N)
    tails = h[N + 1:N + M]
    kappa_factor = h[N + M]
    return (d, e, A, M, N), variables, tails, kappa_factor


def dp_script(variables, tails, kappa_factor):
    """Fast open-locus unit/dimension computation in the extended ring."""
    T = sp.Symbol("T")
    ring_variables = [T] + variables
    generators = tails + [T * kappa_factor - 1]
    names = ",".join(map(str, ring_variables))
    encoded = ",".join(singular_polynomial(g, ring_variables) for g in generators)
    return (
        "ring RE=0,(%s),dp; option(redSB); ideal IE=%s; "
        "timer=1; ideal GE=slimgb(IE); timer=0; "
        "print(\"EXTENDED_RING Q[%s], ORDER dp\"); "
        "print(\"UNIT_REMAINDER\"); reduce(1,GE); "
        "print(\"GB_SIZE\"); size(GE); print(\"OPEN_DIM\"); dim(GE); "
        "print(\"GB\"); GE; quit;\n"
    ) % (names, encoded, names)


def lex_component_script(variables, tails, kappa_factor):
    """Extract (I:h^infinity) into an explicitly declared base ring.

    This mode is intended for the small leader branches and controls.  It may
    be substantially more expensive than the dp emptiness test.
    """
    if not variables:
        raise ValueError("component extraction needs a nonempty base variable list")
    T = sp.Symbol("T")
    base_names = ",".join(map(str, variables))
    base_generators = ",".join(singular_polynomial(g, variables) for g in tails)
    base_kappa = singular_polynomial(kappa_factor, variables)
    ext_names = "T," + base_names
    return (
        "ring R0=0,(%s),lp; ideal I0=%s; poly K0=%s; "
        "ring RE=0,(%s),lp; "
        "ideal IE=imap(R0,I0),T*imap(R0,K0)-1; ideal GE=std(IE); "
        "ideal EE=eliminate(GE,T); "
        "ring RS=0,(%s),lp; ideal JSAT=imap(RE,EE); ideal GSAT=std(JSAT); "
        "print(\"BASE_RING Q[%s], ORDER lp\"); "
        "print(\"SATURATED_COMPONENT (I:K^infinity)\"); GSAT; "
        "print(\"SAT_DIM\"); dim(GSAT); quit;\n"
    ) % (base_names, base_generators, base_kappa, ext_names,
         base_names, base_names)


def run(args):
    generated_at = time.time()
    data, variables, tails, kappa_factor = make_system(args.case, args.first)
    d, e, A, M, N = data
    if args.extract_component:
        script = lex_component_script(variables, tails, kappa_factor)
        mode = "LEX_COMPONENT"
    else:
        script = dp_script(variables, tails, kappa_factor)
        mode = "DP_OPEN_TEST"
    generation_seconds = time.time() - generated_at

    started = time.time()
    try:
        result = subprocess.run(
            ["Singular", "-q"], input=script, text=True,
            capture_output=True, timeout=args.timeout, check=False)
        status, returncode = "DONE", result.returncode
        stdout, stderr = result.stdout, result.stderr
    except subprocess.TimeoutExpired as exc:
        status, returncode = "TIMEOUT", 124
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
    elapsed = time.time() - started
    maxrss = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss

    print("CASE=%s d=%d e=%d A=%d M=%d N=%d FIRST=%d" %
          (args.case, d, e, A, M, N, args.first))
    print("BASE_RING=Q[%s]" % ",".join(map(str, variables)))
    print("EXTENDED_RING=Q[T%s]" %
          (("," + ",".join(map(str, variables))) if variables else ""))
    print("MODE=%s TAIL_GENERATORS=%d RABINOWITSCH=T*h%d-1" %
          (mode, len(tails), M + N))
    print("GEN_SECONDS=%.3f STATUS=%s RC=%d RUN_SECONDS=%.3f MAXRSS_KB=%d" %
          (generation_seconds, status, returncode, elapsed, maxrss))
    print(stdout)
    if stderr:
        print("STDERR")
        print(stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", choices=sorted(CASES))
    parser.add_argument("--first", type=int, required=True)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--extract-component", action="store_true")
    run(parser.parse_args())


if __name__ == "__main__":
    main()
