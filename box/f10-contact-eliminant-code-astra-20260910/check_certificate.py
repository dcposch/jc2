"""SOURCE ONLY; not executed, imported, compiled, AST- or syntax-tested.

Independent exact sparse Q[z,V,W,X] identity checker. No Singular, eval,
producer import, emitted ideal, GB claim, or polynomial-expression parser.
Future invocation: python3 check_certificate.py PATH_TO_CERTIFICATE
ROOT must separately register resource caps and pin this source/runtime.
"""

from fractions import Fraction
import hashlib
import re
import sys

INTERFACE = "c1ec52ca1b71295b44c99fbcdaec5c05d3c47f24cd468f2669888ca96950fdd3"
GATE = "76d25dfe462a44b5c7df06245fb55486a8b80aa037e818bda38cdb893f1be047"
ZERO = (0, 0, 0, 0)
MAX_BYTES = 64 * 1024 * 1024  # Refusal bound, not a mathematical degree claim.
INTEGER = re.compile(r"-?(?:0|[1-9][0-9]*)\Z")


class Poly:
    def __init__(self, terms=None):
        self.terms = {e: Fraction(c) for e, c in (terms or {}).items() if c}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({ZERO: Fraction(value)})

    def __add__(self, other):
        out = dict(self.terms)
        for e, c in self.coerce(other).terms.items():
            out[e] = out.get(e, Fraction(0)) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        out = {}
        for e, a in self.terms.items():
            for f, b in self.coerce(other).terms.items():
                exponent = tuple(e[k] + f[k] for k in range(4))
                out[exponent] = out.get(exponent, Fraction(0)) + a * b
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("non-polynomial power")
        result = Poly.coerce(1)
        for _ in range(power):
            result = result * self
        return result


def literal_generators():
    # Separate reconstruction: use BOTH literal quartics and subtract
    # their coefficients, rather than reading the producer's d,e,f.
    variables = [Poly({tuple(int(k == i) for k in range(4)): 1}) for i in range(4)]
    z, V, W, X = variables
    a3 = 30*V - 14
    a2 = 71 - 270*V + 180*V**2 + 120*W
    a1 = -154 + 780*V - 900*V**2 + 120*V**3 - 600*W + 720*V*W
    a0 = 120 - 720*V + 1080*V**2 - 240*V**3 + 720*W - 1440*V*W + 360*W**2
    b3 = 42*V - 18
    b2 = 119 - 504*V + 420*V**2 + 210*W
    b1 = -342 + 1974*V - 2940*V**2 + 840*V**3 - 1470*W + 2520*V*W
    b0 = (360 - 2520*V + 5040*V**2 - 2520*V**3
          + 2520*W - 7560*V*W + 2520*V**2*W + 2520*W**2)
    c, d, e, f = a3-b3, a2-b2, a1-b1, a0-b0
    g = d-c*a3
    A = c**2*a2-c*e+d*g
    B = c**2*a1-c*f+e*g
    C = c**2*a0+f*g
    return (c*A*C-c*B**2+d*A*B-e*A**2,
            d*A*C-c*B*C-f*A**2,
            A*X**2+B*X+C,
            z*c*A-1)


def parse_certificate(raw):
    tokens = raw.decode("ascii").split()
    position = 0

    def take():
        nonlocal position
        if position >= len(tokens):
            raise ValueError("truncated certificate")
        token = tokens[position]
        position += 1
        return token

    def expect(token):
        if take() != token:
            raise ValueError("schema/source/ring/block mismatch: " + token)

    def integer():
        token = take()
        if not INTEGER.fullmatch(token):
            raise ValueError("not a decimal integer")
        value = int(token)
        if str(value) != token:
            raise ValueError("noncanonical decimal integer")
        return value

    header = ("JC2_CONTACT_CERT_V1", "interface", INTERFACE, "gate", GATE,
              "ring", "Q", "z", "V", "W", "X", "dp",
              "generators", "I1", "I2", "I3", "I4")
    for token in header:
        expect(token)
    result = {}
    for name in ("F", "H1", "H2", "H3", "H4"):
        expect("poly")
        expect(name)
        terms = {}
        while True:
            tag = take()
            if tag == "endpoly":
                break
            if tag != "term":
                raise ValueError("unexpected polynomial token")
            numerator, denominator = integer(), integer()
            exponent = tuple(integer() for _ in range(4))
            if denominator <= 0 or numerator == 0 or min(exponent) < 0:
                raise ValueError("invalid rational term or negative exponent")
            coefficient = Fraction(numerator, denominator)
            if (coefficient.numerator != numerator or
                    coefficient.denominator != denominator):
                raise ValueError("non-reduced rational coefficient")
            if exponent in terms:
                raise ValueError("duplicate monomial")
            terms[exponent] = coefficient
        result[name] = Poly(terms)
    expect("endcert")
    if position != len(tokens):
        raise ValueError("trailing data")
    return result


def check(raw):
    if len(raw) > MAX_BYTES:
        raise ValueError("certificate exceeds byte refusal bound")
    certificate = parse_certificate(raw)
    F = certificate["F"]
    if not F.terms:
        raise ValueError("F is zero")
    if any(exponent[:3] != (0, 0, 0) for exponent in F.terms):
        raise ValueError("F is not in Q[X]")
    residual = F
    for index, generator in enumerate(literal_generators(), 1):
        residual = residual-certificate["H" + str(index)]*generator
    if residual.terms:
        raise ValueError("exact polynomial identity is nonzero")
    return hashlib.sha256(raw).hexdigest()


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: check_certificate.py CERTIFICATE")
        # Exact integer text may exceed CPython's optional decimal limit;
        # the byte bound and future external resource caps remain mandatory.
        if hasattr(sys, "set_int_max_str_digits"):
            sys.set_int_max_str_digits(0)
        with open(sys.argv[1], "rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
        digest = check(raw)
    except Exception as error:
        print("CHECK_FAIL " + str(error), file=sys.stderr)
        return 2
    print("CHECK_OK sha256=" + digest + " identity=exact_Q[z,V,W,X]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
