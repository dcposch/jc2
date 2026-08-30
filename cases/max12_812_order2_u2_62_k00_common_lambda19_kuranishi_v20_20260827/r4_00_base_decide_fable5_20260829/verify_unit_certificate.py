#!/usr/bin/env python3
"""Independent exact verifier for R4-00 base-decide lift certificates.

Reads the packet generator file and a Singular-produced certificate file
(written by R4_00_R*_BASE_DECIDE*.sing on the EMPTY branch), reparses both
with a self-contained recursive-descent parser, and checks the identity

    sum_k C_k * gen_k  ==  (open_product)^a * chart^N

exactly over Q (CELL-R2) or Q(i) (CELL-R1), where open_product is D*kappa
resp. q*kappa and chart is s or t.  This check is engine-independent: only
the *strings* come from Singular; every arithmetic step here is stdlib
Fraction arithmetic.

Usage:
  verify_unit_certificate.py --ring r2 --gens R2_GENS.txt --cert R2_CERT_S.txt
  verify_unit_certificate.py --ring r1 --gens R1_epsP_GENS.txt \
      --cert R1_epsP_CERT_T.txt
The chart variable (s or t) is read from the certificate header line.
"""

from __future__ import annotations

import argparse
import re
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

F0, F1 = F(0), F(1)
RING_VARS = {"r2": ["s", "t", "uz", "vz", "kappa"],
             "r1": ["s", "t", "kappa", "q", "A8", "B8"]}

TOKEN = re.compile(r"\s*(\d+|[A-Za-z_][A-Za-z_0-9]*|\*\*|[()+\-*/^])")


class Parser:
    """Parses a polynomial over Q(i)[vars]; 'ii' is the imaginary unit."""

    def __init__(self, text: str, varnames: list[str]):
        self.toks: list[str] = []
        pos = 0
        while pos < len(text):
            m = TOKEN.match(text, pos)
            if not m:
                if text[pos:].strip():
                    raise ValueError(f"tokenize error at {text[pos:pos+30]!r}")
                break
            self.toks.append(m.group(1))
            pos = m.end()
        self.i = 0
        self.vidx = {n: k for k, n in enumerate(varnames)}

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else None

    def take(self):
        t = self.peek()
        self.i += 1
        return t

    def parse(self):
        p = self.expr()
        if self.peek() is not None:
            raise ValueError(f"trailing tokens {self.toks[self.i:self.i+5]}")
        return p

    def expr(self):
        sign = 1
        while self.peek() in ("+", "-"):
            if self.take() == "-":
                sign = -sign
        acc = pscale(self.term(), (F(sign), F0))
        while self.peek() in ("+", "-"):
            sign = 1
            while self.peek() in ("+", "-"):
                if self.take() == "-":
                    sign = -sign
            acc = padd(acc, pscale(self.term(), (F(sign), F0)))
        return acc

    def term(self):
        acc = self.factor()
        while True:
            t = self.peek()
            if t == "*":
                self.take()
                acc = pmul(acc, self.factor())
            elif t == "/":
                self.take()
                d = self.factor()
                if list(d) != [()] or d[()][1] != 0:
                    raise ValueError("nonconstant or complex denominator")
                dr = d[()][0]
                acc = pscale(acc, (1 / dr, F0))
            else:
                return acc

    def factor(self):
        t = self.take()
        if t == "(":
            inner = self.expr()
            if self.take() != ")":
                raise ValueError("missing )")
            base = inner
        elif t == "-":
            return pscale(self.factor(), (F(-1), F0))
        elif t is not None and t.isdigit():
            base = {(): (F(int(t)), F0)}
        elif t == "ii":
            base = {(): (F0, F1)}
        elif t is not None and t in self.vidx:
            base = {((self.vidx[t], 1),): (F1, F0)}
        else:
            raise ValueError(f"unexpected token {t!r}")
        if self.peek() in ("^", "**"):
            self.take()
            e = self.take()
            if e is None or not e.isdigit():
                raise ValueError("bad exponent")
            out = {(): (F1, F0)}
            for _ in range(int(e)):
                out = pmul(out, base)
            return out
        return base


def mono_mul(m1, m2):
    d = dict(m1)
    for v, e in m2:
        d[v] = d.get(v, 0) + e
    return tuple(sorted(d.items()))


def padd(P, Q):
    out = dict(P)
    for m, (x, y) in Q.items():
        ox, oy = out.get(m, (F0, F0))
        rx, ry = ox + x, oy + y
        if rx or ry:
            out[m] = (rx, ry)
        else:
            out.pop(m, None)
    return out


def pmul(P, Q):
    out: dict = {}
    for m1, (a, b) in P.items():
        for m2, (c, d) in Q.items():
            m = mono_mul(m1, m2)
            x, y = a * c - b * d, a * d + b * c
            ox, oy = out.get(m, (F0, F0))
            out[m] = (ox + x, oy + y)
    return {m: v for m, v in out.items() if v[0] or v[1]}


def pscale(P, c):
    a, b = c
    return {m: (a * x - b * y, a * y + b * x) for m, (x, y) in P.items()}


def parse_named(path: Path, varnames):
    """Parse 'name=poly;' lines."""
    out = {}
    text = path.read_text()
    for chunk in text.split(";"):
        chunk = chunk.strip()
        if not chunk or chunk.startswith("#"):
            continue
        name, _, body = chunk.partition("=")
        out[name.strip()] = Parser(body, varnames).parse()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ring", choices=("r2", "r1"), required=True)
    ap.add_argument("--gens", type=Path, required=True)
    ap.add_argument("--cert", type=Path, required=True)
    args = ap.parse_args()
    varnames = RING_VARS[args.ring]
    gens = parse_named(args.gens, varnames)
    order = (["X1", "X2", "X3", "X4", "X5"] if args.ring == "r2" else
             ["c21p14", "row1line14", "conic1_c31at16", "conic2_row4at16",
              "e18a_row6at18", "e18b_D51at18", "e18c_D71at18"])
    if sorted(gens) != sorted(order):
        raise SystemExit(f"FAIL: generator names {sorted(gens)}")
    lines = [ln.strip() for ln in args.cert.read_text().splitlines()
             if ln.strip()]
    header = lines[0]
    chart = "s" if "s^N" in header else ("t" if "t^N" in header else None)
    if chart is None:
        raise SystemExit("FAIL: cannot read chart from certificate header")
    kv = {}
    cof = {}
    for ln in lines[1:]:
        name, _, body = ln.partition("=")
        if name in ("a", "N"):
            kv[name] = int(body)
        else:
            cof[name] = Parser(body, varnames).parse()
    if sorted(cof) != [f"C{k}" for k in range(1, len(order) + 1)]:
        raise SystemExit(f"FAIL: cofactor names {sorted(cof)}")
    a, N = kv["a"], kv["N"]
    total: dict = {}
    for k, name in enumerate(order, 1):
        total = padd(total, pmul(cof[f"C{k}"], gens[name]))
    P = Parser
    if args.ring == "r2":
        open_prod = P("((6*uz+5*kappa*s)^2+64*(-6*vz+5*kappa*t)^2)*kappa",
                      varnames).parse()
    else:
        open_prod = P("q*kappa", varnames).parse()
    target = {(): (F1, F0)}
    for _ in range(a):
        target = pmul(target, open_prod)
    chart_poly = P(chart, varnames).parse()
    for _ in range(N):
        target = pmul(target, chart_poly)
    diff = padd(total, pscale(target, (F(-1), F0)))
    if diff:
        raise SystemExit(f"FAIL: identity does not hold; {len(diff)} "
                         "residual terms")
    print("CERTIFICATE_VERIFIED=1")
    print(f"ring={args.ring} chart={chart} a={a} N={N}")
    print(f"gens_sha256={sha256(args.gens.read_bytes()).hexdigest()}")
    print(f"cert_sha256={sha256(args.cert.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
