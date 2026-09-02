#!/usr/bin/env python3
"""qqideal oracle jobs for the five corrected N=4 suite systems.

Generation target: qqideal 0.1.0. msolve stays the GB engine (via
msolveio). Macaulay2 is not used.

Derivation (tightest statement): kill-review §2, which re-derives
audit r2 §7.1. Codegen is the encoding transcript, not the source of
the equations.

    G86 = p^3-q^4 + a22 p^2 q + a20 p q^2 + a18 q^3
                + a16 p^2 + a14 p q + a12 q^2 + a8 p + a6 q
    g_j = [t^j] G86
    retain auxiliaries of weight strictly greater than c.

    G96 = p^2-q^3 + a15 p q + a12 q^2 + a9 p + a6 q

Correspondence with the old jobs, in short (report §2 has the
line-cited table):

    M2 I0 + (u*g_c - 1)     <->  Ideal(closed).saturate(g_c)
                                 == ideal_verdict(I0, opens=[g_c])
       Exact: qqideal.saturate is Rabinowitsch I+(u*f-1) in ring[u].
       Ideal.colon is a v0.1 alias of saturate.

    M2 colonInf(Iopen, Cover)  with Cover=(B,D,F,gam,e) or
       (P6,P4,P2,Q3,Q1) is I : Cover^∞ for an IDEAL. v0.1 colon/
       saturate inverts one polynomial. Saturating at the product of
       the cover generators would be a strictly larger open
       (complement of a union of hyperplanes, not of the cover
       locus). This file does not fake that step. The c-open already
       excludes common degree-2/3 covers (audit 169-177, 504-505);
       for P1, Iopen is empty before the colon (kill-review §6).

    M2 idpPostcheck(p0,q0,N)  <->  double_point_ideal(p0,q0) plus
       dimdeg, on a CLOSED univariate parametrization. See
       p3_idp_verdict_for_closed_point for what that constructor
       does and does not check.

Coefficient polynomials are expanded over QQ by fractions.Fraction
(sandbox-runnable, no flint/msolve). qqideal consumes the resulting
generator strings as Ideal / saturate / verdict.

Do not treat a qqideal Verdict as a boolean: Verdict.__bool__ raises.
Branch on verdict.kind (Kind.EMPTY / NONEMPTY / TIMEOUT / ERROR).
"""
from __future__ import annotations

import hashlib
import os
import re
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, Union

# ---------------------------------------------------------------------------
# Specs (audit 7.1 / kill-review §2 / codegen §1)
# ---------------------------------------------------------------------------

CHART86: Tuple[str, ...] = (
    "B", "C", "D", "E", "F", "G", "b", "gam", "d", "e", "f",
)
CHART96: Tuple[str, ...] = (
    "A", "P6", "B", "P4", "C", "P2", "D", "a", "Q3", "b", "Q1",
)
AUX_A: Tuple[str, ...] = ("a22", "a20", "a18", "a16", "a14", "a12")
AUX_B: Tuple[str, ...] = AUX_A
AUX_C: Tuple[str, ...] = AUX_A + ("a8",)
AUX_D: Tuple[str, ...] = AUX_C + ("a6",)
AUX_96: Tuple[str, ...] = ("a15", "a12", "a9", "a6")

# in-chart cover loci from the old .m2 files (NOT applied as a v0.1 saturate)
COVER86: Tuple[str, ...] = ("B", "D", "F", "gam", "e")
COVER96: Tuple[str, ...] = ("P6", "P4", "P2", "Q3", "Q1")

BOX_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class JobSpec:
    job_id: str
    delta: Tuple[int, int, int]
    family: str  # "86" or "96"
    aux: Tuple[str, ...]
    closed_hi: int
    closed_lo: int
    open_deg: int
    delta_aff: int
    ms_stem: str
    cover: Tuple[str, ...]


SPECS: Dict[str, JobSpec] = {
    "p1_863": JobSpec(
        "p1_863", (8, 6, 3), "86", AUX_D, 22, 4, 3, 7,
        "corrected_863", COVER86,
    ),
    "p2_869": JobSpec(
        "p2_869", (8, 6, 9), "86", AUX_B, 22, 10, 9, 10,
        "corrected_869", COVER86,
    ),
    "p3_964": JobSpec(
        "p3_964", (9, 6, 4), "96", AUX_96, 16, 5, 4, 6,
        "corrected_964", COVER96,
    ),
    "p4a_8611": JobSpec(
        "p4a_8611", (8, 6, 11), "86", AUX_A, 22, 12, 11, 11,
        "corrected_8611", COVER86,
    ),
    "p4b_867": JobSpec(
        "p4b_867", (8, 6, 7), "86", AUX_C, 22, 8, 7, 9,
        "corrected_867", COVER86,
    ),
}


# ---------------------------------------------------------------------------
# QQ(zeta) with zeta^2 = zeta - 18474  (audit §5 charged A point)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class QZeta:
    a: Fraction
    b: Fraction

    def __add__(self, other: object) -> "QZeta":
        o = _as_zeta(other)
        return QZeta(self.a + o.a, self.b + o.b)

    def __radd__(self, other: object) -> "QZeta":
        return self + other

    def __sub__(self, other: object) -> "QZeta":
        o = _as_zeta(other)
        return QZeta(self.a - o.a, self.b - o.b)

    def __rsub__(self, other: object) -> "QZeta":
        return _as_zeta(other) - self

    def __neg__(self) -> "QZeta":
        return QZeta(-self.a, -self.b)

    def __mul__(self, other: object) -> "QZeta":
        o = _as_zeta(other)
        ac = self.a * o.a
        bd = self.b * o.b
        cross = self.a * o.b + self.b * o.a
        # zeta^2 = zeta - 18474
        return QZeta(ac - Fraction(18474) * bd, cross + bd)

    def __rmul__(self, other: object) -> "QZeta":
        return self * other

    def __truediv__(self, other: object) -> "QZeta":
        if isinstance(other, QZeta):
            raise NotImplementedError("division in QQ(zeta) is not needed here")
        o = Fraction(other)  # type: ignore[arg-type]
        return QZeta(self.a / o, self.b / o)

    def __pow__(self, n: int) -> "QZeta":
        if n < 0:
            raise ValueError("negative power")
        result = QZeta(Fraction(1), Fraction(0))
        base = self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result

    def __eq__(self, other: object) -> bool:
        o = _as_zeta(other)
        return self.a == o.a and self.b == o.b

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def __str__(self) -> str:
        if self.b == 0:
            return _frac_str(self.a)
        bterm = _zeta_term(self.b)
        if self.a == 0:
            return bterm
        if self.b > 0:
            return f"{_frac_str(self.a)} + {bterm}"
        return f"{_frac_str(self.a)} - {_zeta_term(-self.b)}"


def _as_zeta(value: object) -> QZeta:
    if isinstance(value, QZeta):
        return value
    if isinstance(value, bool):
        raise TypeError("bool is not a coefficient")
    if isinstance(value, Fraction):
        return QZeta(value, Fraction(0))
    if isinstance(value, int):
        return QZeta(Fraction(value), Fraction(0))
    raise TypeError(f"cannot promote {type(value).__name__} to QZeta")


def _is_zero(c: object) -> bool:
    if isinstance(c, QZeta):
        return c.is_zero()
    return c == 0


def _frac_str(c: Fraction) -> str:
    if c.denominator == 1:
        return str(c.numerator)
    return f"{c.numerator}/{c.denominator}"


def _zeta_term(b: Fraction) -> str:
    """Render ``b*zeta`` as ``n*zeta/d`` (codegen transcript convention)."""
    if b == 1:
        return "zeta"
    if b == -1:
        return "-zeta"
    n, d = b.numerator, b.denominator
    if d == 1:
        return f"{n}*zeta"
    if n < 0:
        return f"-{-n}*zeta/{d}"
    return f"{n}*zeta/{d}"


# ---------------------------------------------------------------------------
# Sparse multivariate polynomials over Fraction or QZeta
# ---------------------------------------------------------------------------

Exp = Tuple[int, ...]
Coeff = Union[Fraction, QZeta]


class MV:
    """Sparse polynomial in a declared name tuple. Immutable-in-use."""

    __slots__ = ("names", "terms")

    def __init__(
        self,
        names: Tuple[str, ...],
        terms: Optional[Mapping[Exp, Coeff]] = None,
    ) -> None:
        self.names = names
        collected: Dict[Exp, Coeff] = {}
        if terms:
            for exp, coeff in terms.items():
                if len(exp) != len(names):
                    raise ValueError("exponent length != nvars")
                if not _is_zero(coeff):
                    collected[tuple(int(e) for e in exp)] = coeff
        self.terms = collected

    def __add__(self, other: object) -> "MV":
        if not isinstance(other, MV):
            other = _const(self.names, other)  # type: ignore[arg-type]
        if other.names != self.names:
            raise ValueError("name mismatch")
        out: Dict[Exp, Coeff] = dict(self.terms)
        for exp, coeff in other.terms.items():
            out[exp] = out[exp] + coeff if exp in out else coeff  # type: ignore[operator]
        return MV(self.names, out)

    def __radd__(self, other: object) -> "MV":
        return self + other

    def __sub__(self, other: object) -> "MV":
        return self + (-other)  # type: ignore[operator]

    def __neg__(self) -> "MV":
        return MV(self.names, {e: -c for e, c in self.terms.items()})  # type: ignore[operator]

    def __mul__(self, other: object) -> "MV":
        if not isinstance(other, MV):
            out = {e: c * other for e, c in self.terms.items()}  # type: ignore[operator]
            return MV(self.names, out)
        if other.names != self.names:
            raise ValueError("name mismatch")
        out: Dict[Exp, Coeff] = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                exp = tuple(a + b for a, b in zip(e1, e2))
                prod = c1 * c2  # type: ignore[operator]
                out[exp] = out[exp] + prod if exp in out else prod  # type: ignore[operator]
        return MV(self.names, out)

    def __rmul__(self, other: object) -> "MV":
        return self * other

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MV):
            return NotImplemented
        if other.names != self.names:
            return False
        keys = set(self.terms) | set(other.terms)
        for k in keys:
            a = self.terms.get(k, 0)
            b = other.terms.get(k, 0)
            if isinstance(a, QZeta) or isinstance(b, QZeta):
                if _as_zeta(a) != _as_zeta(b):
                    return False
            elif Fraction(a) != Fraction(b):  # type: ignore[arg-type]
                return False
        return True

    def is_zero(self) -> bool:
        return not self.terms

    def as_constant(self) -> Optional[Coeff]:
        if not self.terms:
            return Fraction(0)
        if len(self.terms) == 1:
            exp, coeff = next(iter(self.terms.items()))
            if all(e == 0 for e in exp):
                return coeff
        if all(all(e == 0 for e in exp) for exp in self.terms):
            acc: Coeff = Fraction(0)
            for coeff in self.terms.values():
                acc = acc + coeff  # type: ignore[operator]
            return acc
        return None


def _const(names: Tuple[str, ...], value: object) -> MV:
    if isinstance(value, MV):
        return value
    if _is_zero(value):
        return MV(names, {})
    if isinstance(value, QZeta):
        coeff: Coeff = value
    else:
        coeff = Fraction(value)  # type: ignore[arg-type]
    return MV(names, {(0,) * len(names): coeff})


def _var(names: Tuple[str, ...], name: str) -> MV:
    exp = [0] * len(names)
    exp[names.index(name)] = 1
    return MV(names, {tuple(exp): Fraction(1)})


# Univariate-in-t: degree -> coefficient MV
UPoly = Dict[int, MV]


def _uadd(a: UPoly, b: UPoly) -> UPoly:
    out: UPoly = dict(a)
    for deg, coeff in b.items():
        out[deg] = out[deg] + coeff if deg in out else coeff
    return {d: c for d, c in out.items() if not c.is_zero()}


def _usub(a: UPoly, b: UPoly) -> UPoly:
    return _uadd(a, {d: -c for d, c in b.items()})


def _umul(a: UPoly, b: UPoly) -> UPoly:
    out: UPoly = {}
    for i, ci in a.items():
        for j, cj in b.items():
            deg = i + j
            prod = ci * cj
            out[deg] = out[deg] + prod if deg in out else prod
    return {d: c for d, c in out.items() if not c.is_zero()}


def _upow(a: UPoly, n: int) -> UPoly:
    if n < 0:
        raise ValueError("negative power")
    if not a:
        if n == 0:
            raise ValueError("0^0")
        return {}
    names = next(iter(a.values())).names
    result: UPoly = {0: _const(names, 1)}
    if n == 0:
        return result
    base = a
    exp = n
    while exp:
        if exp & 1:
            result = _umul(result, base)
        base = _umul(base, base)
        exp >>= 1
    return result


def _uscale(a: UPoly, mv: MV) -> UPoly:
    return {d: c * mv for d, c in a.items()}


# ---------------------------------------------------------------------------
# G86 / G96
# ---------------------------------------------------------------------------

def expand_g86(aux: Sequence[str]) -> Tuple[Tuple[str, ...], UPoly]:
    """Kill-review §2 / audit 7.1 G86 in the declared (8,6) chart."""
    names = tuple(aux) + CHART86
    one = _const(names, 1)
    p: UPoly = {
        8: one,
        5: _var(names, "B"),
        4: _var(names, "C"),
        3: _var(names, "D"),
        2: _var(names, "E"),
        1: _var(names, "F"),
        0: _var(names, "G"),
    }
    q: UPoly = {
        6: one,
        4: _var(names, "b"),
        3: _var(names, "gam"),
        2: _var(names, "d"),
        1: _var(names, "e"),
        0: _var(names, "f"),
    }
    g = _usub(_upow(p, 3), _upow(q, 4))
    p2 = _upow(p, 2)
    q2 = _upow(q, 2)
    q3 = _upow(q, 3)
    aux_set = set(aux)
    if "a22" in aux_set:
        g = _uadd(g, _uscale(_umul(p2, q), _var(names, "a22")))
    if "a20" in aux_set:
        g = _uadd(g, _uscale(_umul(p, q2), _var(names, "a20")))
    if "a18" in aux_set:
        g = _uadd(g, _uscale(q3, _var(names, "a18")))
    if "a16" in aux_set:
        g = _uadd(g, _uscale(p2, _var(names, "a16")))
    if "a14" in aux_set:
        g = _uadd(g, _uscale(_umul(p, q), _var(names, "a14")))
    if "a12" in aux_set:
        g = _uadd(g, _uscale(q2, _var(names, "a12")))
    if "a8" in aux_set:
        g = _uadd(g, _uscale(p, _var(names, "a8")))
    if "a6" in aux_set:
        g = _uadd(g, _uscale(q, _var(names, "a6")))
    return names, g


def expand_g96(aux: Sequence[str] = AUX_96) -> Tuple[Tuple[str, ...], UPoly]:
    """Audit 7.1 / codegen §5 G96 in the declared (9,6) chart."""
    names = tuple(aux) + CHART96
    one = _const(names, 1)
    p: UPoly = {
        9: one,
        7: _var(names, "A"),
        6: _var(names, "P6"),
        5: _var(names, "B"),
        4: _var(names, "P4"),
        3: _var(names, "C"),
        2: _var(names, "P2"),
        1: _var(names, "D"),
    }
    q: UPoly = {
        6: one,
        4: _var(names, "a"),
        3: _var(names, "Q3"),
        2: _var(names, "b"),
        1: _var(names, "Q1"),
    }
    g = _usub(_upow(p, 2), _upow(q, 3))
    aux_set = set(aux)
    if "a15" in aux_set:
        g = _uadd(g, _uscale(_umul(p, q), _var(names, "a15")))
    if "a12" in aux_set:
        g = _uadd(g, _uscale(_upow(q, 2), _var(names, "a12")))
    if "a9" in aux_set:
        g = _uadd(g, _uscale(p, _var(names, "a9")))
    if "a6" in aux_set:
        g = _uadd(g, _uscale(q, _var(names, "a6")))
    return names, g


def coeff_t(g: UPoly, j: int, names: Tuple[str, ...]) -> MV:
    return g.get(j, MV(names, {}))


# ---------------------------------------------------------------------------
# msolve text: render and parse (expanded unique-monomial sums)
# ---------------------------------------------------------------------------

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*|[0-9]+|[+\-*/^]")


def render_mv(mv: MV) -> str:
    """Expanded unique-monomial sum. Zero is ``0``. No parentheses."""
    items = [(exp, c) for exp, c in mv.terms.items() if not _is_zero(c)]
    if not items:
        return "0"
    if any(isinstance(c, QZeta) for _, c in items):
        raise TypeError("cannot emit QQ(zeta) coefficients to msolve")

    def grevlex_key(exp: Exp) -> Tuple:
        return (-sum(exp), tuple(-e for e in reversed(exp)))

    items.sort(key=lambda ec: grevlex_key(ec[0]))
    pieces: List[str] = []
    for exp, coeff in items:
        frac = Fraction(coeff)  # type: ignore[arg-type]
        neg, body = _term_body(exp, frac, mv.names)
        if not pieces:
            pieces.append("-" + body if neg else body)
        else:
            pieces.append(("-" if neg else "+") + body)
    return "".join(pieces)


def _term_body(exp: Exp, coeff: Fraction, names: Sequence[str]) -> Tuple[bool, str]:
    neg = coeff < 0
    num, den = abs(coeff.numerator), coeff.denominator
    var_factors = []
    for name, power in zip(names, exp):
        if power == 1:
            var_factors.append(name)
        elif power > 1:
            var_factors.append(f"{name}^{power}")
    if not var_factors:
        body = str(num) if den == 1 else f"{num}/{den}"
    elif num == 1 and den == 1:
        body = "*".join(var_factors)
    elif den == 1:
        body = "*".join([str(num), *var_factors])
    else:
        body = "*".join([f"{num}/{den}", *var_factors])
    return neg, body


def parse_mv(source: str, names: Tuple[str, ...]) -> MV:
    """Parse an expanded monomial sum into an MV of ``names``."""
    text = "".join(source.split())
    if text.endswith(","):
        text = text[:-1]
    if text in ("", "0", "+0", "-0"):
        return MV(names, {})
    tokens = _TOKEN_RE.findall(text)
    if "".join(tokens) != text:
        raise ValueError(f"unparsed residue in {source!r}")
    index = {n: i for i, n in enumerate(names)}
    nvars = len(names)
    terms: Dict[Exp, Coeff] = {}
    pos = 0
    ntok = len(tokens)
    while pos < ntok:
        sign = 1
        if tokens[pos] in ("+", "-"):
            sign = -1 if tokens[pos] == "-" else 1
            pos += 1
            if pos >= ntok:
                raise ValueError(f"trailing sign in {source!r}")
        coeff_num, coeff_den = 1, 1
        exp = [0] * nvars
        leading = True
        while True:
            if pos >= ntok:
                raise ValueError(f"truncated term in {source!r}")
            tok = tokens[pos]
            if tok.isdigit():
                if not leading:
                    raise ValueError(f"mid-term numeral {tok} in {source!r}")
                coeff_num = int(tok)
                pos += 1
                if pos < ntok and tokens[pos] == "/":
                    pos += 1
                    if pos >= ntok or not tokens[pos].isdigit():
                        raise ValueError(f"bad denominator in {source!r}")
                    coeff_den = int(tokens[pos])
                    if coeff_den == 0:
                        raise ValueError("zero denominator")
                    pos += 1
            elif tok[0].isalpha():
                if tok not in index:
                    raise ValueError(f"unknown identifier {tok!r} in {source!r}")
                pos += 1
                power = 1
                if pos < ntok and tokens[pos] == "^":
                    pos += 1
                    if pos >= ntok or not tokens[pos].isdigit():
                        raise ValueError(f"bad exponent of {tok} in {source!r}")
                    power = int(tokens[pos])
                    pos += 1
                exp[index[tok]] += power
            else:
                raise ValueError(f"unexpected {tok!r} in {source!r}")
            leading = False
            if pos >= ntok or tokens[pos] in ("+", "-"):
                break
            if tokens[pos] != "*":
                raise ValueError(f"expected '*', got {tokens[pos]!r} in {source!r}")
            pos += 1
        key = tuple(exp)
        value = Fraction(sign * coeff_num, coeff_den)
        terms[key] = terms.get(key, Fraction(0)) + value
    return MV(names, terms)


def closed_open_generators(spec: JobSpec) -> Tuple[Tuple[str, ...], List[str], str, MV]:
    """Return (var_names, closed msolve strings, open msolve string, open MV)."""
    if spec.family == "86":
        names, g = expand_g86(spec.aux)
    else:
        names, g = expand_g96(spec.aux)
    closed: List[str] = []
    for j in range(spec.closed_hi, spec.closed_lo - 1, -1):
        gj = coeff_t(g, j, names)
        if gj.is_zero():
            raise AssertionError(
                f"{spec.job_id}: g_{j} vanished identically; the closed "
                f"range {spec.closed_hi}..{spec.closed_lo} is a required slot"
            )
        closed.append(render_mv(gj))
    gopen = coeff_t(g, spec.open_deg, names)
    if gopen.is_zero():
        raise AssertionError(f"{spec.job_id}: g_{spec.open_deg} vanished identically")
    return names, closed, render_mv(gopen), gopen


def load_ms_generators(path: Path) -> Tuple[List[str], List[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        raise ValueError(f"{path} is not POSIX text (missing trailing newline)")
    lines = text.splitlines()
    variables = lines[0].split(",")
    if lines[1] != "0":
        raise ValueError(f"{path} characteristic line is {lines[1]!r}, not '0'")
    gens = []
    for line in lines[2:]:
        s = line.strip()
        if s.endswith(","):
            s = s[:-1]
        gens.append(s)
    return variables, gens


def subst_mv(mv: MV, values: Mapping[str, Coeff]) -> MV:
    idx = {n: i for i, n in enumerate(mv.names)}
    pairs = [(idx[n], values[n]) for n in values if n in idx]
    out: Dict[Exp, Coeff] = {}
    for exp, coeff in mv.terms.items():
        new_exp = list(exp)
        c: Coeff = coeff
        for i, val in pairs:
            power = new_exp[i]
            new_exp[i] = 0
            if power:
                c = c * (val ** power)  # type: ignore[operator]
        key = tuple(new_exp)
        out[key] = out[key] + c if key in out else c  # type: ignore[operator]
    return MV(mv.names, out)


# ---------------------------------------------------------------------------
# Self-checks (pure Fraction / QQ(zeta); no msolve, no qqideal)
# ---------------------------------------------------------------------------

def _lines_leading_identities() -> List[str]:
    """Kill-review §2 leading coefficients (independent of the three controls)."""
    names, g = expand_g86(AUX_D)
    expected = {
        22: "a22-4*b",
        21: "3*B-4*gam",
        20: "a22*b+a20+3*C-6*b^2-4*d",
        19: "2*a22*B+a22*gam+3*D-12*b*gam-4*e",
    }
    lines = ["=== leading G86 identities (kill-review §2) ==="]
    ok = True
    for j, src in expected.items():
        got = coeff_t(g, j, names)
        want = parse_mv(src, names)
        match = got == want
        ok = ok and match
        lines.append(
            f"g_{j} == {src}: {'match' if match else 'MISMATCH'}"
        )
        if not match:
            lines.append(f"  got {render_mv(got)}")
    # g_23 identically 0 (chart identity)
    g23 = coeff_t(g, 23, names)
    z = g23.is_zero()
    ok = ok and z
    lines.append(f"g_23 identically 0: {'match' if z else 'MISMATCH'}")
    lines.append(
        "LEADING-IDENTITIES: PASS" if ok else "LEADING-IDENTITIES: FAIL"
    )
    return lines


def _lines_ms_encoding() -> List[str]:
    """Fraction closed/open generators vs hashed reviewed .ms files."""
    lines = ["=== encoding comparison vs reviewed .ms (polynomial equality) ==="]
    all_ok = True
    for spec in SPECS.values():
        path = BOX_DIR / f"{spec.ms_stem}.ms"
        ms_vars, ms_gens = load_ms_generators(path)
        names, closed, open_s, gopen = closed_open_generators(spec)
        # .ms vars = names + (u,)
        if tuple(ms_vars) != names + ("u",):
            all_ok = False
            lines.append(
                f"{spec.ms_stem}: VAR-MISMATCH ms={ms_vars} vs {names + ('u',)}"
            )
            continue
        if len(ms_gens) != len(closed) + 1:
            all_ok = False
            lines.append(
                f"{spec.ms_stem}: GEN-COUNT ms={len(ms_gens)} vs closed+open={len(closed)+1}"
            )
            continue
        ms_names = tuple(ms_vars)
        job_ok = True
        for i, (ours, theirs) in enumerate(zip(closed, ms_gens[:-1])):
            if parse_mv(ours, ms_names) != parse_mv(theirs, ms_names):
                job_ok = False
                lines.append(
                    f"{spec.ms_stem}: closed[{i}] (deg {spec.closed_hi - i}) MISMATCH"
                )
                break
        # last generator is u*gopen - 1
        u_names = ms_names
        u_exp = [0] * len(u_names)
        u_exp[u_names.index("u")] = 1
        u_poly = MV(u_names, {tuple(u_exp): Fraction(1)})
        want_open = parse_mv(open_s, u_names) * u_poly + _const(u_names, -1)
        got_open = parse_mv(ms_gens[-1], u_names)
        if want_open != got_open:
            job_ok = False
            lines.append(f"{spec.ms_stem}: open u*g_{spec.open_deg}-1 MISMATCH")
        all_ok = all_ok and job_ok
        n_closed = spec.closed_hi - spec.closed_lo + 1
        lines.append(
            f"{spec.ms_stem}: {'match' if job_ok else 'MISMATCH'} "
            f"({n_closed} closed + open g_{spec.open_deg}; "
            f"vars {len(names)}+u)"
        )
    lines.append(
        "MS-ENCODING: PASS" if all_ok else "MS-ENCODING: FAIL"
    )
    return lines


def _charged_a_point() -> Dict[str, Coeff]:
    """Audit §5 / codegen §7 (i). Chart order (B,C,D,E,F,G,b,gam,d,e,f)."""
    z = QZeta(Fraction(0), Fraction(1))
    return {
        "B": Fraction(1),
        "C": Fraction(0),
        "D": (Fraction(294) - z) / Fraction(144),
        "E": Fraction(0),
        "F": (Fraction(150) - z) / Fraction(48),
        "G": Fraction(0),
        "b": Fraction(1),
        "gam": Fraction(3, 4),
        "d": Fraction(1),
        "e": -(Fraction(138) + z) / Fraction(192),
        "f": (Fraction(2) * z - Fraction(71)) / Fraction(144),
    }


def _fmt_coeff(c: object) -> str:
    if isinstance(c, QZeta):
        return str(c)
    if isinstance(c, Fraction):
        return _frac_str(c)
    return str(c)


def _eval_const(mv: MV, values: Mapping[str, Coeff]) -> Coeff:
    got = subst_mv(mv, values).as_constant()
    if got is None:
        raise AssertionError("substitution did not yield a constant")
    return got


def _lines_check_i() -> List[str]:
    """Charged A false-positive vs corrected (8,6,11): required FAIL of membership."""
    lines = ["=== (i) charged A false-positive vs corrected (8,6,11) ==="]
    names, g = expand_g86(AUX_A)
    pt = _charged_a_point()
    # g22 = a22 - 4 b; at the point b=1 so a22-4
    g22 = subst_mv(coeff_t(g, 22, names), pt)
    lines.append(f"check(i) g22 at point (in a22): {render_mv(g22)}")
    g21 = _eval_const(coeff_t(g, 21, names), pt)
    lines.append(f"check(i) g21 at point: {_fmt_coeff(g21)}")
    # raw H = G86 with auxiliaries zero
    names_h, h = expand_g86(())
    h19 = _eval_const(coeff_t(h, 19, names_h), pt)
    lines.append(f"check(i) h19 at point: {_fmt_coeff(h19)}")
    # g19 residual at a22 = 4 b = 4
    g19 = subst_mv(coeff_t(g, 19, names), {**pt, "a22": Fraction(4)})
    g19c = g19.as_constant()
    lines.append(f"check(i) g19 residual (a22=4): {_fmt_coeff(g19c)}")
    h11 = _eval_const(coeff_t(h, 11, names_h), pt)
    lines.append(f"check(i) raw h11 at point: {_fmt_coeff(h11)}")
    # membership of the corrected closed system: g19 is a closed equation
    # for (8,6,11) (closed g_22..g_12) and is the constant 11, independent
    # of the remaining auxiliaries. FAIL of membership is the required outcome.
    fail_membership = (g19c == 11) and (g21 == 0) and (h19 == 0)
    # also record the displayed h11
    want_h11 = QZeta(Fraction(59291, 18432), Fraction(-27671, 110592))
    h11_ok = h11 == want_h11
    if fail_membership and h11_ok:
        lines.append(
            "SELF-CHECK (i) charged A false-positive vs corrected (8,6,11): "
            "PASS — old A holds (g21=0, h19=0, "
            "h11=59291/18432 - 27671*zeta/110592 != 0) but corrected residual "
            "g19|a22=4b equals 11 != 0, so the point is not on V(g_22,...,g_12)"
        )
        lines.append("CHECK(i): PASS")
    else:
        lines.append(
            "SELF-CHECK (i) FAIL — "
            f"g21={_fmt_coeff(g21)} h19={_fmt_coeff(h19)} "
            f"g19={_fmt_coeff(g19c)} h11_ok={h11_ok}"
        )
        lines.append("CHECK(i): FAIL")
    return lines


def _lines_check_ii() -> List[str]:
    """(9,6,2) exhibit curve vs corrected (9,6,2) membership: required PASS."""
    lines = ["=== (ii) (9,6,2) exhibit vs corrected membership ==="]
    names, g = expand_g96()
    # q = t^6+8 t^2, p = t^9+12 t^5+24 t
    # chart: B=12, D=24, b=8, rest of mixed/A/C/... zero
    pt: Dict[str, Coeff] = {
        "A": Fraction(0), "P6": Fraction(0), "B": Fraction(12),
        "P4": Fraction(0), "C": Fraction(0), "P2": Fraction(0),
        "D": Fraction(24),
        "a": Fraction(0), "Q3": Fraction(0), "b": Fraction(8),
        "Q1": Fraction(0),
        "a15": Fraction(0), "a12": Fraction(0), "a9": Fraction(0),
        "a6": Fraction(-64),
    }
    closed_vals = []
    for j in range(16, 2, -1):  # 16..3
        closed_vals.append(_eval_const(coeff_t(g, j, names), pt))
    g2 = _eval_const(coeff_t(g, 2, names), pt)
    g1 = _eval_const(coeff_t(g, 1, names), pt)
    g0 = _eval_const(coeff_t(g, 0, names), pt)
    lines.append(
        "check(ii) closed g_16..g_3: ["
        + ", ".join(_fmt_coeff(v) for v in closed_vals)
        + "]"
    )
    lines.append(f"check(ii) g2: {_fmt_coeff(g2)}")
    lines.append(f"check(ii) g0,g1: {_fmt_coeff(g0)} {_fmt_coeff(g1)}")
    ok = all(v == 0 for v in closed_vals) and g2 == 64 and g1 == 0 and g0 == 0
    if ok:
        lines.append(
            "SELF-CHECK (ii) (9,6,2) curve q=t^6+8t^2, p=t^9+12t^5+24t vs "
            "corrected (9,6,2): PASS — aux (a15,a12,a9,a6)=(0,0,0,-64) gives "
            "g_j=0 for 3<=j<=16 and g_2=64 != 0"
        )
        lines.append("CHECK(ii): PASS")
    else:
        lines.append("SELF-CHECK (ii) FAIL")
        lines.append("CHECK(ii): FAIL")
    return lines


def _lines_check_iii() -> List[str]:
    """HF-twin (9,6,4) vs corrected 964 locus (pre-nodal): required PASS."""
    lines = ["=== (iii) HF-twin (9,6,4) vs corrected locus (pre-nodal) ==="]
    names, g = expand_g96()
    # shared constant-zero chart (audit §6 / codegen §7 (iii))
    pt: Dict[str, Coeff] = {
        "A": Fraction(3), "P6": Fraction(0), "B": Fraction(21, 4),
        "P4": Fraction(0), "C": Fraction(35, 8), "P2": Fraction(0),
        "D": Fraction(63, 32),
        "a": Fraction(2), "Q3": Fraction(0), "b": Fraction(5, 2),
        "Q1": Fraction(0),
        "a15": Fraction(0), "a12": Fraction(-9, 4), "a9": Fraction(0),
        "a6": Fraction(-27, 16),
    }
    closed_vals = []
    for j in range(16, 4, -1):  # 16..5
        closed_vals.append(_eval_const(coeff_t(g, j, names), pt))
    g4 = _eval_const(coeff_t(g, 4, names), pt)
    rest = [_eval_const(coeff_t(g, j, names), pt) for j in (3, 2, 1, 0)]
    lines.append(
        "check(iii) closed g_16..g_5: ["
        + ", ".join(_fmt_coeff(v) for v in closed_vals)
        + "]"
    )
    lines.append(f"check(iii) g4: {_fmt_coeff(g4)}")
    lines.append(
        f"check(iii) g3,g2,g1,g0: {_fmt_coeff(rest[0])} {_fmt_coeff(rest[1])} "
        f"{_fmt_coeff(rest[2])} {_fmt_coeff(rest[3])}"
    )
    ok = (
        all(v == 0 for v in closed_vals)
        and g4 == Fraction(-27, 128)
        and rest[0] == 0
        and rest[1] == Fraction(-351, 1024)
        and rest[2] == 0
        and rest[3] == 0
    )
    if ok:
        lines.append(
            "SELF-CHECK (iii) HF-twin (9,6,4) vs corrected (9,6,4) locus: "
            "PASS — aux (a15,a12,a9,a6)=(0,-9/4,0,-27/16) gives g_j=0 for "
            "5<=j<=16 and g_4=-27/128 != 0 (constant term 0 omitted as in "
            "audit 7.1)"
        )
        lines.append("CHECK(iii): PASS")
    else:
        lines.append("SELF-CHECK (iii) FAIL")
        lines.append("CHECK(iii): FAIL")
    return lines


def run_self_checks() -> Tuple[bool, List[str]]:
    """Return (all_pass, transcript lines). No msolve, no qqideal."""
    blocks = [
        _lines_leading_identities(),
        _lines_ms_encoding(),
        _lines_check_i(),
        _lines_check_ii(),
        _lines_check_iii(),
    ]
    lines: List[str] = []
    ok = True
    for block in blocks:
        if lines:
            lines.append("")
        lines.extend(block)
        tail = block[-1]
        if not tail.endswith("PASS"):
            ok = False
    lines.append("")
    lines.append("SELF-CHECKS OVERALL: PASS" if ok else "SELF-CHECKS OVERALL: FAIL")
    return ok, lines


# ---------------------------------------------------------------------------
# qqideal jobs (import is deferred: sandbox has no qqideal)
# ---------------------------------------------------------------------------

def _prepare_msolve_path(binary: Optional[str]) -> Optional[str]:
    """qqideal.Ideal.verdict does not take binary=; put 0.10.1 on PATH."""
    resolved = binary or os.environ.get("MSOLVE_BINARY")
    if not resolved:
        return None
    path = Path(resolved)
    if path.is_file():
        os.environ["PATH"] = str(path.parent) + os.pathsep + os.environ.get("PATH", "")
        return str(path)
    return resolved


def _import_stack():
    try:
        import qqideal
        from qqideal import (
            Certainty,
            Ideal,
            Kind,
            Ring,
            double_point_ideal,
            ideal_verdict,
        )
        import qqideal.dimdeg as dimdeg
        from msolveio import emit_system
    except ImportError as exc:
        raise RuntimeError(
            "qqideal 0.1.0 / msolveio 0.1.0 are not importable here. "
            "The coordinator runs this on the box. Self-checks do not "
            "need them (python3 box/qq_oracle_run.py --self-check)."
        ) from exc
    return {
        "qqideal": qqideal,
        "Ring": Ring,
        "Ideal": Ideal,
        "Kind": Kind,
        "Certainty": Certainty,
        "ideal_verdict": ideal_verdict,
        "double_point_ideal": double_point_ideal,
        "dimdeg": dimdeg,
        "emit_system": emit_system,
    }


def _poly_diff_univariate(poly, var: str = "t"):
    """Differentiate a qqideal Poly with respect to one variable, via terms()."""
    ring = poly.ring
    i = ring.names.index(var)
    acc = ring.constant(0)
    gens = ring.gens()
    for exp, coeff in poly.terms():
        power = exp[i]
        if power == 0:
            continue
        frac = Fraction(int(coeff.numer()), int(coeff.denom())) * power
        new_exp = list(exp)
        new_exp[i] = power - 1
        mon = ring.constant(frac)
        for gen, ee in zip(gens, new_exp):
            if ee:
                mon = mon * (gen ** ee)
        acc = acc + mon
    return acc


def build_incidence(spec: JobSpec):
    """Build I0 and g_c as qqideal objects. Symbolic; no msolve.

    Correspondence, restated at the call site:

        I0      = Ideal([g_j for j=closed_hi..closed_lo], ring=R0)
                  <-> M2 I0 = ideal closedGens  (e.g. corrected_863.m2:35)
        Iopen   = I0.saturate(g_c)
                  <-> M2 Iopen = I0 + (u*g_c-1) (corrected_863.m2:42)
                  <-> .ms last generator u*g_c-1
        Cover   = (B,D,F,gam,e) or (P6,P4,P2,Q3,Q1) is NOT applied.
                  M2 colonInf is I : Cover^∞; v0.1 saturate(product)
                  is the wrong open (see module docstring).
    """
    st = _import_stack()
    Ring, Ideal = st["Ring"], st["Ideal"]
    names, closed, open_s, _gopen = closed_open_generators(spec)
    R0 = Ring(*names)
    I0 = Ideal(closed, ring=R0)
    return st, names, I0, open_s, closed


def _run_incidence(
    spec: JobSpec,
    timeout: float,
    binary: Optional[str] = None,
) -> Tuple[object, dict]:
    _prepare_msolve_path(binary)
    st, names, I0, open_s, closed = build_incidence(spec)
    ideal_verdict = st["ideal_verdict"]
    emit_system = st["emit_system"]

    # Custody SHA-256 is of the saturated (Rabinowitsch) system, which is
    # what msolve actually sees. saturate is symbolic.
    Iopen = I0.saturate(open_s)
    source = Iopen.to_msolve()
    # emit_system is the library primitive named in the charge; to_msolve
    # calls it. Re-emit from generator strings as an independent custody
    # of the closed+open pair (without slack) as well.
    closed_source = emit_system(
        closed,
        variables=list(names),
        characteristic=0,
    )
    started = time.monotonic()
    verdict = ideal_verdict(I0, opens=[open_s], timeout=timeout)
    wall = time.monotonic() - started
    # never `if verdict:`
    kind_name = verdict.kind.value
    certainty_name = verdict.certainty.value
    custody = {
        "job": spec.job_id,
        "delta": spec.delta,
        "family": spec.family,
        "closed_range": (spec.closed_hi, spec.closed_lo),
        "open_deg": spec.open_deg,
        "delta_aff": spec.delta_aff,
        "ring_closed": list(names),
        "ring_open": list(Iopen.ring.names),
        "ngens_closed": len(closed),
        "ngens_open": len(Iopen.gens),
        "input_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "closed_sha256": hashlib.sha256(
            closed_source.encode("utf-8")
        ).hexdigest(),
        "msolve_version": verdict.msolve_version,
        "wall_seconds": wall,
        "kind": kind_name,
        "certainty": certainty_name,
        "dim": verdict.dim,
        "degree": verdict.degree,
        "detail": verdict.detail,
        "cover_not_applied": list(spec.cover),
        "cover_note": (
            "M2 colonInf(Iopen, Cover) is I : Cover^∞ for an ideal; "
            "qqideal v0.1 saturate/colon inverts one polynomial. Not faked. "
            "c-open already excludes common covers (gcd(d,n,c)=1)."
        ),
    }
    return verdict, custody


def job_p1_863(
    timeout: float = 3600, binary: Optional[str] = None
) -> Tuple[object, dict]:
    """P1 (8,6,3): corrected D. Closed g_22..g_4, open g_3 != 0.

    Old Iopen EMPTY is two-engine binding (kill-review). Cover colon is
    downstream and not applied (module docstring).
    """
    return _run_incidence(SPECS["p1_863"], timeout=timeout, binary=binary)


def job_p2_869(
    timeout: float = 3600, binary: Optional[str] = None
) -> Tuple[object, dict]:
    """P2 (8,6,9): corrected B. Closed g_22..g_10 (includes gap g_10), open g_9."""
    return _run_incidence(SPECS["p2_869"], timeout=timeout, binary=binary)


def job_p3_964(
    timeout: float = 3600, binary: Optional[str] = None
) -> Tuple[object, dict]:
    """P3 (9,6,4): corrected 96A incidence, plus I_DP constructor.

    The oracle *row* is Iopen of the characteristic incidence
    (corrected_964.ms). The six-node question is a post-check on a
    closed point: see p3_idp_verdict_for_closed_point.

    double_point_ideal is invoked here symbolically (no Groebner) to
    pin the v0.1.0 contract against our I_DP definition.
    """
    verdict, custody = _run_incidence(
        SPECS["p3_964"], timeout=timeout, binary=binary
    )
    st = _import_stack()
    Ring = st["Ring"]
    double_point_ideal = st["double_point_ideal"]
    # Symbolic construction only. The node (t^2-1, t^3-t) is the library's
    # own example of a nonempty ordered I_DP of degree 2; it is NOT a
    # (9,6,4) curve and is not a six-node witness.
    idp = double_point_ideal("t^2-1", "t^3-t", ring=Ring("t"), names=("s", "t"))
    custody["idp_schema_ring"] = list(idp.ring.names)
    custody["idp_schema_ngens"] = len(idp.gens)
    custody["idp_contract"] = IDP_CONTRACT
    custody["idp_note"] = (
        "P3 six-node: extract a closed point of Iopen, then "
        "p3_idp_verdict_for_closed_point(p0,q0). Ordered degree 12 "
        "would correspond to 6 ordinary unordered nodes; degree==6 "
        "against double_point_ideal is the wrong number. Reduced / "
        "immersive / distinct tangents / no-reused-parameter are NOT "
        "checked by double_point_ideal."
    )
    return verdict, custody


def job_p4a_8611(
    timeout: float = 3600, binary: Optional[str] = None
) -> Tuple[object, dict]:
    """P4a (8,6,11): corrected A. Archival. Record fresh; do not assume."""
    return _run_incidence(SPECS["p4a_8611"], timeout=timeout, binary=binary)


def job_p4b_867(
    timeout: float = 3600, binary: Optional[str] = None
) -> Tuple[object, dict]:
    """P4b (8,6,7): corrected C. Archival. Record fresh; do not assume."""
    return _run_incidence(SPECS["p4b_867"], timeout=timeout, binary=binary)


JOBS = {
    "p1_863": job_p1_863,
    "p2_869": job_p2_869,
    "p3_964": job_p3_964,
    "p4a_8611": job_p4a_8611,
    "p4b_867": job_p4b_867,
}


# ---------------------------------------------------------------------------
# I_DP contract (P3 nodal post-check)
# ---------------------------------------------------------------------------

IDP_CONTRACT = {
    "constructor": "qqideal.double_point_ideal(p, q, ring=Ring('t'), names=('s','t'))",
    "builds": "(p(s)-p(t), q(s)-q(t)) : (s-t)^oo as Rabinowitsch in QQ[s,t,u]",
    "our_I_DP": (
        "unordered scheme in (sig, Pi) via divided differences; tests: "
        "reduced, length==delta_aff, immersive (gcd(p',q')=1), distinct "
        "tangents (Wsym), no reused parameter (F square-free). "
        "Source: msolve-prep §12; corrected_964.m2:114-149; audit 7.1:501-504."
    ),
    "does_check": [
        "ordered pairs s!=t with p(s)=p(t) and q(s)=q(t)",
        "emptiness / Krull dimension / 0-dim ordered degree of that locus",
    ],
    "does_not_check": [
        "reduced (v0.1 has radical_member only; Ideal.radical raises)",
        "length == delta_aff (ours is unordered; ordinary n-node => ordered degree 2n)",
        "immersive (gcd(p',q')=1; the cusp is injective with empty I_DP)",
        "distinct tangents (no Wsym)",
        "no reused parameter / triple fibre (no F(X))",
    ],
    "degree_translation": (
        "ordinary 6-node curve: unordered length 6, ordered degree 12. "
        "Library node (t^2-1, t^3-t): ordered (dim,degree)=(0,2)."
    ),
}


def p3_idp_verdict_for_closed_point(
    p: str,
    q: str,
    timeout: float = 60,
    binary: Optional[str] = None,
) -> Tuple[object, dict]:
    """I_DP construction + verdict for a closed parametrization in QQ[t].

    Uses qqideal.double_point_ideal. Also reports the resultant of
    (p', q') as an immersive probe (0 iff not immersive). Does not
    claim reduced / length==6 / distinct tangents.

    dimdeg is read off the leading monomials of the Rabinowitsch ideal
    in QQ[s,t,u] (three variables: the graph of the ordered pairs).
    """
    _prepare_msolve_path(binary)
    st = _import_stack()
    Ring = st["Ring"]
    double_point_ideal = st["double_point_ideal"]
    Kind = st["Kind"]
    dimdeg = st["dimdeg"]

    Rt = Ring("t")
    poly_p = Rt(p)
    poly_q = Rt(q)
    dp = _poly_diff_univariate(poly_p, "t")
    dq = _poly_diff_univariate(poly_q, "t")
    res = Rt.resultant(dp, dq, "t")
    # resultant wrt the only variable is a constant polynomial
    immersive = not res.is_zero()

    idp = double_point_ideal(poly_p, poly_q, names=("s", "t"))
    started = time.monotonic()
    verdict = idp.verdict(timeout=timeout)
    wall = time.monotonic() - started
    dd = None
    if verdict.kind is Kind.NONEMPTY or verdict.kind is Kind.EMPTY:
        try:
            leading = idp.leading_monomials(timeout=timeout)
            dd = dimdeg.dim_and_degree(leading, idp.ring.nvars)
        except Exception as exc:  # noqa: BLE001 — record, do not guess
            dd = ("OPEN", str(exc))
    notes = {
        "idp_ring": list(idp.ring.names),
        "immersive_resultant_nonzero": immersive,
        "immersive_note": (
            "resultant(p',q') != 0 over QQ iff gcd(p',q')=1. "
            "This is NOT checked by double_point_ideal itself."
        ),
        "dimdeg_from_leading": dd,
        "wall_seconds": wall,
        "msolve_version": verdict.msolve_version,
        "contract": IDP_CONTRACT,
        "delta_aff_target": 6,
        "ordered_degree_if_six_ordinary_nodes": 12,
    }
    return verdict, notes
