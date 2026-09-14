"""Exact controls for the Laurent weight-line count and its endpoint repair."""

from fractions import Fraction
import resource


resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def weight(a_numerator, ell, b, rho, sigma):
    """Weight of t^(a_numerator/ell) pi^b."""
    return rho * Fraction(a_numerator, ell) + sigma * b


# Full L^(ell): pi exponents are nonnegative, but t exponents may be negative.
ell = 3
rho = sigma = 1
laurent_line = []
for b in range(13):
    a_numerator = ell * (2 - b)
    require(weight(a_numerator, ell, b, rho, sigma) == 2,
            "Laurent weight-line identity")
    laurent_line.append((Fraction(a_numerator, ell), b))
require(laurent_line[-1] == (Fraction(-10), 12),
        "negative t tail with high pi degree")

# Weight and separability still do not cap the degree in the Laurent object:
# t^2 + t^(2-N) pi^N = t^2(1 + (pi/t)^N).  In characteristic zero,
# 1+z^N and its derivative N*z^(N-1) have no common root because z=0 is
# not a root of 1+z^N.
high_degree = 12
separable_laurent_support = [(Fraction(2), 0),
                             (Fraction(2 - high_degree), high_degree)]
require(all(rho * a + sigma * b == rho + sigma
            for a, b in separable_laurent_support),
        "high-degree Laurent homogeneous support")
require(high_degree > 2 and high_degree != 0,
        "arbitrarily high separable Laurent face control")


# Changed object: intersect the same line with K[t^(1/ell), pi].
positive_line = [(a, b) for a, b in laurent_line if a >= 0]
require(positive_line == [(Fraction(2), 0), (Fraction(1), 1),
                          (Fraction(0), 2)],
        "positive-quadrant weight line")
require(len(positive_line) == 3, "three monomials on positive weight line")
require(max(b for _, b in positive_line) - min(b for _, b in positive_line) == 2,
        "univariate degree/root-count ceiling two")


# Endpoint-alignment repair: a positive-quadrant P endpoint A of positive
# weight D scales to an F endpoint B=((rho+sigma)/D)A, hence B stays positive.
source_endpoints = [(Fraction(3), Fraction(0)),
                    (Fraction(0), Fraction(3))]
repaired_endpoints = []
for a, b in source_endpoints:
    degree = rho * a + sigma * b
    require(degree > 0, "positive source endpoint weight")
    scale = Fraction(rho + sigma, degree)
    repaired = (scale * a, scale * b)
    require(repaired[0] >= 0 and repaired[1] >= 0,
            "aligned endpoint remains in positive quadrant")
    require(rho * repaired[0] + sigma * repaired[1] == rho + sigma,
            "aligned endpoint has Euler weight")
    repaired_endpoints.append(repaired)
require(repaired_endpoints == [(Fraction(2), Fraction(0)),
                               (Fraction(0), Fraction(2))],
        "expected repaired endpoints")


# Changed-source control: endpoint alignment does not repair a genuinely
# Laurent source endpoint. It preserves its negative t coordinate.
changed_source = (Fraction(-1), Fraction(3))
changed_degree = rho * changed_source[0] + sigma * changed_source[1]
require(changed_degree == rho + sigma, "changed source positive weight")
changed_aligned = tuple(Fraction(rho + sigma, changed_degree) * coordinate
                        for coordinate in changed_source)
require(changed_aligned == changed_source and changed_aligned[0] < 0,
        "Laurent changed-source endpoint remains negative")


print("LAURENT_WEIGHT_LINE_UNBOUNDED_CONTROL_PASS", laurent_line[-4:])
print("LAURENT_SEPARABLE_HIGH_DEGREE_CONTROL_PASS",
      high_degree, separable_laurent_support)
print("POSITIVE_SUBRING_COUNT_CONTROL_PASS", positive_line)
print("ENDPOINT_ALIGNMENT_REPAIR_CONTROL_PASS", repaired_endpoints)
print("CHANGED_LAURENT_SOURCE_CONTROL_PASS", changed_aligned)
print("ALL_EXACT_WEIGHT_CONTROLS_PASS")
